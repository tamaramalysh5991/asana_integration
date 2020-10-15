import logging
from requests.exceptions import ChunkedEncodingError

from asana import Client as AsanaClient
from asana.error import ServerError
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


logger = logging.getLogger(__name__)


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
    if getattr(settings, 'ASANA_WORKSPACE', None):
        client.options['workspace_id'] = settings.ASANA_WORKSPACE
        # workspaces = client.workspaces.find_all()
        # for workspace in workspaces:
        #     if settings.ASANA_WORKSPACE == workspace['name']:
        #         client.options['workspace_id'] = workspace['gid']
    client.options['Asana-Fast-Api'] = 'true'
    return client