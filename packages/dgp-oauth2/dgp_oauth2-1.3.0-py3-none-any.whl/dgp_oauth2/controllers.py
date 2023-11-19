import datetime

import urllib.parse as urlparse

import jwt
import requests

from authlib.integrations.flask_client import OAuth, FlaskOAuth2App, OAuthError

from .logger import logger
from .models import Models
from .extensions import on_new_user, on_user_login, on_user_logout
from .permissions import get_token

class RemoteApp():

    def __init__(self, app: FlaskOAuth2App, get_profile, auth_header_prefix) -> None:
        self.app = app
        self.get_profile = get_profile
        self.auth_header_prefix = auth_header_prefix


class Controllers:

    def __init__(self, models, *,
            google_key=None, google_secret=None,
            github_key=None, github_secret=None,
            set_session=lambda k, v: None,
            get_session=lambda k: None):

        self.models = models
        self.remote_apps: dict[str, RemoteApp] = {}
        self.google_key = google_key
        self.google_secret = google_secret
        self.github_key = github_key
        self.github_secret = github_secret
        self.set_session = set_session
        self.get_session = get_session

    def init_app(self, app):        
        self.oauth = OAuth(app)
        # Google
        has_google = all([self.google_key, self.google_secret])
        if has_google:
            self.oauth.register(
                'google',
                server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
                # api_base_url='https://www.googleapis.com/oauth2/v1/',
                # authorization_endpoint='https://accounts.google.com/o/oauth2/auth',
                scope='email profile',
                # token_endpoint='https://accounts.google.com/o/oauth2/token',
                # token_endpoint_auth_method='POST',
                client_id=self.google_key,
                client_secret=self.google_secret
            )
            self.remote_apps['google'] = RemoteApp(
                app=self.oauth.google,
                get_profile='https://www.googleapis.com/oauth2/v1/userinfo',
                auth_header_prefix='OAuth '
            )

        # GitHub
        has_github = all([self.github_key, self.github_secret])
        if has_github:
            self.oauth.register(
                'github',
                api_base_url='https://api.github.com/',
                authorization_endpoint='https://github.com/login/oauth/authorize',
                scope='user:email',
                token_endpoint='https://github.com/login/oauth/access_token',
                # token_endpoint_auth_method='POST',
                client_id=self.github_key,
                client_secret=self.github_secret)
            self.remote_apps['github'] = RemoteApp(
                app=self.oauth.github,
                get_profile='https://api.github.com/user',
                auth_header_prefix='token '
            )

        self.enable_fake = not any([has_google, has_github])
        logger.info(
            'AUTH CONTROLLERS:' + 
            (' google' if has_google else '') + 
            (' github' if has_github else '') + 
            (' fake' if self.enable_fake else '')
        )

    # Public methods
    def authenticate(self, token, next, callback_url, private_token):
        """Check if user is authenticated
        """
        logger.info('AUTH CONTROLLERS: authenticate %s %s %s' % (token is not None, next, callback_url))
        if token is not None:
            try:
                token = jwt.decode(token, private_token, algorithms=['HS256'])
            except jwt.InvalidTokenError:
                logger.info('AUTH CONTROLLERS: invalid token %r' % token)
                token = None

            if token is not None:
                userid = token['userid']
                user = self.models.get_user(userid)
                logger.info('AUTH CONTROLLERS: userid %s found %s' % (userid, user is not None))
                if user is not None:
                    ret = {
                        'authenticated': True,
                        'profile': user
                    }
                    return ret

        # Otherwise - not authenticated
        providers = {}
        state = {
            'next': next,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            'nbf': datetime.datetime.utcnow()
        }
        for provider, params in self.remote_apps.items():
            pstate = dict(provider=provider, **state)
            pstate = jwt.encode(pstate, private_token)
            login = params.app.create_authorization_url(redirect_uri=callback_url)
            login_url = login['url']
            login_state = login['state']
            self.set_session(f'state_{login_state}', pstate)
            logger.debug('AUTH CONTROLLERS STATE: %s, %r -> %r' % (provider, params, login))
            params.app.save_authorize_data(**login)
            providers[provider] = {'url': login_url}
        if self.enable_fake:
            providers = self._fake_providers(next, private_token)
        ret = {
            'authenticated': False,
            'providers': providers
        }
        return ret


    def update(self, token, username, private_token):
        """Update a user
        """
        err = None
        if token is not None:
            try:
                token = jwt.decode(token, private_token, algorithms=['HS256'])
            except jwt.InvalidTokenError:
                token = None
                err = 'Not authenticated'
        else:
            err = 'No token'

        if token is not None:
            userid = token['userid']
            user = self.models.get_user(userid)

            if user is not None:
                dirty = False
                if username is not None:
                    if user.get('username') is None:
                        user['username'] = username
                        dirty = True
                    else:
                        err = 'Cannot modify username, already set'
                if dirty:
                    self.models.save_user(user)
            else:
                err = 'Unknown User'

        ret = {'success': err is None}
        if err is not None:
            ret['error'] = err

        return ret


    def authorize(self, token, service, private_key, private_token):
        """Return user authorization for a service
        """
        if token is not None and service is not None:
            try:
                token = jwt.decode(token, private_token, algorithms=['HS256'])
            except jwt.InvalidTokenError:
                token = None

            if token is not None:
                userid = token['userid']
                permissions = get_token(service, userid)
                ret = {
                    'userid': userid,
                    'permissions': permissions,
                    'service': service
                }
                token = jwt.encode(ret, private_key, algorithm='RS256')
                ret['token'] = token
                return ret

        ret = {
            'permissions': {}
        }
        return ret


    def oauth_callback(self, state, callback_url, private_token):
        """Callback from OAuth
        """
        logger.info('AUTH CONTROLLERS: oauth_callback %s' % state)
        state = self.get_session(f'state_{state}')
        logger.info('AUTH CONTROLLERS: found state %s' % state)
        try:
            state = jwt.decode(state, private_token, algorithms=['HS256'])
        except jwt.InvalidTokenError:
            state = {}
        logger.info('AUTH CONTROLLERS: oauth_callback decoded %r' % state)

        resp = None

        provider = state.get('provider')
        access_token = None
        if provider is not None:
            try:
                app = self.remote_apps[provider].app
                access_token = app.authorize_access_token(redirect_uri=callback_url)
                if access_token is not None:
                    access_token = access_token['access_token']
            except OAuthError as e:
                resp = e
            if isinstance(resp, OAuthError):
                logger.error("OAuthException: %r", access_token, exc_info=resp)
                resp = None
        next_url = self._next_url(state, access_token, private_token)
        logger.info('AUTH CONTROLLERS: oauth_callback next_url %s %s -> %s' % (state, access_token, next_url))
        return next_url


    def resolve_username(self, username):
        """Return userid for given username. If not exist, return None.
        """
        ret = {'userid': None}
        user = self.models.get_user_by_username(username)
        if user is not None:
            ret['userid'] = user['id']
        return ret


    def get_profile_by_username(self, username):
        """Return user profile for given username. If not exist, return None.
        """
        ret = {'found': False, 'profile': None}
        user = self.models.get_user_by_username(username)
        if user is not None:
            ret['found'] = True
            ret['profile'] = {
                'id': user['id'],
                'name': user['name'],
                'join_date': user['join_date'],
                'avatar_url': user['avatar_url'],
                'gravatar': self.models.hash_email(user['email'])
            }
        return ret

    
    # Private methods

    def _get_user_profile(self, provider, access_token):
        if access_token is None:
            return None
        remote_app = self.remote_apps[provider]
        headers = {'Authorization': '{}{}'.format(remote_app.auth_header_prefix, access_token)}
        response = requests.get(remote_app.get_profile,
                                headers=headers)

        if response.status_code == 401:
            return None

        response = response.json()
        # Make sure we have private Emails from github.
        # Also make sure we don't have user registered with other email than primary
        if provider == 'github':
            emails_resp = requests.get(remote_app.get_profile + '/emails', headers=headers)
            for email in emails_resp.json():
                id_ = self.models.hash_email(email['email'])
                user = self.models.get_user(id_)
                if user is not None:
                    response['email'] = email['email']
                    break
                if email.get('primary'):
                    response['email'] = email['email']
        return response


    def _fake_providers(self, next, private_token):
        ret = dict()
        for provider in ('google', 'github'):
            token = self._get_token_from_userid(self.models.FAKE_USER_ID, private_token)
            next = self._update_next_url(next, token)
            ret[provider] = dict(url=next)
        self.models.create_or_get_user(
            self.models.FAKE_USER_ID,
            self.models.FAKE_USER_RECORD['name'],
            self.models.FAKE_USER_RECORD['username'],
            self.models.FAKE_USER_RECORD['email'],
            self.models.FAKE_USER_RECORD['avatar_url'],
        )
        return ret


    def _next_url(self, state, access_token, private_token):
        next_url = '/'
        provider = state.get('provider')
        next_url = state.get('next', next_url)
        if access_token is not None and provider is not None:
            logger.info('Got ACCESS TOKEN %r', access_token)
            profile = self._get_user_profile(provider, access_token)
            logger.info('Got PROFILE %r', profile)
            client_token = self._get_token_from_profile(provider, profile, private_token)
            # Add client token to redirect url
            next_url = self._update_next_url(next_url, client_token)

        return next_url


    def _update_next_url(self, next_url, client_token):
        if client_token is None:
            return next_url

        url_parts = list(urlparse.urlparse(next_url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update({'jwt': client_token})

        url_parts[4] = urlparse.urlencode(query)

        next_url = urlparse.urlunparse(url_parts)
        return next_url


    def _get_token_from_profile(self, provider, profile, private_token):
        norm_profile = self._normalize_profile(provider, profile)
        if norm_profile is None:
            return None
        userid = norm_profile['userid']
        name = norm_profile['name']
        username = norm_profile['username']
        email = norm_profile['email']
        avatar_url = norm_profile['avatar_url']
        user = self.models.create_or_get_user(userid, name, username, email, avatar_url)
        if user.get('new'):
            on_new_user(user)
        logger.info('Got USER %r', user)
        return self._get_token_from_userid(user['id'], private_token)


    def _get_token_from_userid(self, userid, private_token):
        token = {
            'userid': userid,
            'exp': (datetime.datetime.utcnow() +
                    datetime.timedelta(days=14))
        }
        client_token = jwt.encode(token, private_token)
        return client_token


    def _normalize_profile(self, provider, profile):
        if profile is None:
            return None
        provider_id = profile['id']
        name = profile['name']
        email = profile.get('email')
        if email is None:
            return None
        username = email.split('@')[0]
        if provider == 'github':
            username = profile.get('login')
        fixed_username = username
        suffix = 1
        while self.models.get_user_by_username(username) is not None:
            username = '{}{}'.format(fixed_username, suffix)
            suffix += 1
        avatar_url = profile.get('picture', profile.get('avatar_url'))
        userid = '%s:%s' % (provider, provider_id)
        normalized_profile = dict(
            provider_id=provider_id,
            name=name,
            email=email,
            username=username,
            avatar_url=avatar_url,
            userid=userid
        )
        return normalized_profile

