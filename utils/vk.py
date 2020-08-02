import logging
import webbrowser
from urllib.parse import urlencode, urlparse

logger = logging.getLogger(__name__)


class VkInteractiveTokenAuth:
    OAUTH_AUTHORIZE_URL = 'https://oauth.vk.com/authorize'

    def __init__(self, client_id: int, scope: int = 6121396, redirect_uri: str = 'https://oauth.vk.com/blank.html'):
        self.client_id = client_id
        self.scope = scope
        self.redirect_uri = redirect_uri

    def get_access_token(self):
        self._open_auth_url()

        logger.info(
            'Paste that url you were directed to in order to '
            'complete the authorization'
        )
        response = input("Enter the URL you were redirected to: ")
        token_info = self.parse_auth_response_url(response)

        return token_info["access_token"]

    def _open_auth_url(self):
        auth_url = self._get_authorize_url()
        try:
            webbrowser.open(auth_url)
            logger.info("Opened %s in your browser", auth_url)
        except webbrowser.Error:
            logger.error("Please navigate here: %s", auth_url)

    def _get_authorize_url(self):
        """Gets the URL to use to authorize."""
        payload = {
            "client_id": self.client_id,
            "scope": self.scope,
            "redirect_uri": self.redirect_uri,
            "response_type": "token",
            "display": "page",
        }

        params = urlencode(payload)

        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, params)

    @staticmethod
    def parse_auth_response_url(url: str) -> dict:
        url_components = urlparse(url)
        fragment = url_components.fragment
        pairs = map(lambda x: x.split('='), fragment.split('&'))
        return dict(pairs)
