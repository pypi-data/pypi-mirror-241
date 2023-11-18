from jupyterhub.handlers import BaseHandler
from jupyterhub.auth import Authenticator
from jupyterhub.auth import LocalAuthenticator
from jupyterhub.utils import url_path_join
from tornado import gen, web
from traitlets import Unicode, Bool
from jose import jwt
import jwt
import requests
import base64
import json

class JSONWebTokenLoginHandler(BaseHandler):

    def get(self):
        header_name = self.authenticator.header_name
        auth_header_content = self.request.headers.get(header_name, "")

        if auth_header_content:
            jwt_headers = auth_header_content.split('.')[0]
            decoded_jwt_headers = base64.b64decode(jwt_headers)
            decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")
            decoded_json = json.loads(decoded_jwt_headers)
            kid = decoded_json['kid']

            url = 'https://public-keys.auth.elb.us-east-1.amazonaws.com/' + kid
            req = requests.get(url)
            pub_key = req.text

            payload = jwt.decode(auth_header_content, pub_key, algorithms=['ES256'])
        else:
           raise web.HTTPError(401)
        
        email = payload.get('email')

        if not email:
           raise web.HTTPError(401)

        user = self.user_from_username(email)
        self.set_login_cookie(user)

        _url = url_path_join(self.hub.server.base_url, 'home')
        next_url = self.get_argument('next', default=False)
        if next_url:
             _url = next_url

        self.redirect(_url)

class JSONWebTokenAuthenticator(Authenticator):
    header_name = Unicode(
        default_value='Authorization',
        config=True,
        help="""HTTP header to inspect for the authenticated JSON Web Token.""")

    def get_handlers(self, app):
        return [
            (r'/login', JSONWebTokenLoginHandler),
        ]

    @gen.coroutine
    def authenticate(self, *args):
        raise NotImplementedError()

class JSONWebTokenLocalAuthenticator(JSONWebTokenAuthenticator, LocalAuthenticator):
    """
    A version of JSONWebTokenAuthenticator that mixes in local system user creation
    """
    pass
