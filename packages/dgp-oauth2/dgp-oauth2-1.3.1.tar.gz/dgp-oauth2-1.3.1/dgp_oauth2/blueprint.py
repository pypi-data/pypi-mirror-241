import os

from flask import Blueprint, request, url_for, session
from flask import redirect
from flask_jsonpify import jsonpify

from .controllers import Controllers
from .models import Models
from .credentials import \
    google_key, google_secret, \
    github_key, github_secret, \
    private_key, public_key, \
    private_token, db_connection_string as db_connection_string_

def register_blueprint(controllers: Controllers, register):
    def func(app, options, *args, **kwargs):
        print('AUTH: REGISTERING BLUEPRINT', app)
        controllers.init_app(app)
        return register(app, options, *args, **kwargs)
    return func


def set_session(k, v):
    session[k] = v


def get_session(k):
    return session.get(k)


def make_blueprint(external_address, engine=None, db_connection_string=None):
    """Create blueprint.
    """

    models = Models(db_connection_string or db_connection_string_, engine=engine)
    controllers = Controllers(models,
                              google_key=google_key,
                              google_secret=google_secret,
                              github_key=github_key,
                              github_secret=github_secret,
                              set_session=set_session, get_session=get_session)


    # Create instance
    blueprint = Blueprint('auth', 'auth')

    # Controller Proxies
    authenticate_controller = controllers.authenticate
    update_controller = controllers.update
    authorize_controller = controllers.authorize
    oauth_callback_controller = controllers.oauth_callback
    resolve_username_controller = controllers.resolve_username
    get_profile_by_username_controller = controllers.get_profile_by_username

    def callback_url():
        if external_address.startswith('http'):
            return external_address+url_for('auth.oauth_callback')
        else:
            return 'https://'+external_address+url_for('auth.oauth_callback')

    def authorize_():
        token = request.headers.get('auth-token') or request.values.get('jwt')
        service = request.values.get('service')
        return jsonpify(authorize_controller(token, service, private_key, private_token))

    def check_():
        token = request.headers.get('auth-token') or request.values.get('jwt')
        next_url = request.args.get('next', 'http://example.com')
        return jsonpify(authenticate_controller(token, next_url, callback_url(), private_token))

    def update_():
        token = request.headers.get('auth-token') or request.values.get('jwt')
        username = request.values.get('username')
        return jsonpify(update_controller(token, username, private_token))

    def oauth_callback_():
        state = request.args.get('state')
        return redirect(oauth_callback_controller(state, callback_url(), private_token))

    def public_key_():
        return public_key

    def resolve_username_():
        username = request.values.get('username')
        return jsonpify(resolve_username_controller(username))

    def get_profile_():
        username = request.values.get('username')
        return jsonpify(get_profile_by_username_controller(username))

    # Register routes
    blueprint.add_url_rule(
        'check', 'check', check_, methods=['GET'])
    blueprint.add_url_rule(
        'update', 'update', update_, methods=['POST'])
    blueprint.add_url_rule(
        'authorize', 'authorize', authorize_, methods=['GET'])
    blueprint.add_url_rule(
        'public-key', 'public-key', public_key_, methods=['GET'])
    blueprint.add_url_rule(
        'oauth_callback', 'oauth_callback', oauth_callback_, methods=['GET'])
    blueprint.add_url_rule(
        'resolve', 'resolve', resolve_username_, methods=['GET'])
    blueprint.add_url_rule(
        'get_profile', 'get_profile', get_profile_, methods=['GET'])

    blueprint.register = register_blueprint(controllers, blueprint.register)

    # Return blueprint
    return blueprint
