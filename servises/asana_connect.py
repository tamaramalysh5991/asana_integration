import logging
from requests.exceptions import ChunkedEncodingError

from asana import Client as AsanaClient
from asana.error import ServerError
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)


def get_workspace(client):
    """Try to get workspace from client or settings
    Every project is required to be created in a specific workspace or
    organization, and this cannot be changed once set.
    https://developers.asana.com/docs/create-a-project
    """
    workspace = getattr(settings, 'ASANA_WORKSPACE', None)
    if not workspace:
        workspaces = [
            workspace for workspace in client.workspaces.find_all(item_limit=1)
        ]
        if not workspaces:
            logger.error('Any workspaces was not found')
            return
        workspace = workspaces[0]['gid']
    return workspace


class Client(AsanaClient, object):
    """An http client for making requests to an Asana
    API and receiving responses."""

    def request(self, method, path, **options):
        logger.debug('%s, %s', method, path)
        try:
            return super(Client, self).request(method, path, **options)
        except (SystemExit, ServerError, ChunkedEncodingError):
            logger.error(
                'Error for %s, %s with options %s', method, path, options
            )
            # Try once more
            return super(Client, self).request(method, path, **options)


def client_connect():
    if not getattr(settings, 'ASANA_ACCESS_TOKEN', None):
        raise ImproperlyConfigured(
            'It is required to set the ASANA_ACCESS_TOKEN or '
            'the three OAuth2 settings ' +
            'ASANA_CLIENT_ID, ASANA_CLIENT_SECRET, '
            'and ASANA_OAUTH_REDIRECT_URI.'
        )
    client = Client.access_token(settings.ASANA_ACCESS_TOKEN)
    return client
