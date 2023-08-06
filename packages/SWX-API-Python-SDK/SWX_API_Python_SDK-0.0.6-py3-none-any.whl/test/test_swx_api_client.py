"""Module to test SwxApiClient"""

from os import environ
import unittest
import pytest
import swx_sdk
from swx_sdk.swx_api_client import SwxApiClient
from swx_sdk.api import collections_api
from swx_sdk.model.collection_request import CollectionRequest
from swx_sdk.model.collection_update_request import CollectionUpdateRequest
from swx_sdk.api import models_api
from swx_sdk.model.model_request import ModelRequest
from swx_sdk.model.model_update_request import ModelUpdateRequest


CONFIGURATION = swx_sdk.Configuration(
    host=environ.get('SWX_HOST', None)
)
if environ.get('VERIFY_SSL', True) in ['False', 'false']:
    CONFIGURATION.verify_ssl = False


def get_swxclient(
        client_id=environ.get('CLIENT_ID', None),
        client_secret=environ.get('CLIENT_SECRET', None),
        scope=environ.get('SCOPE', None),
        defer_auth=False
):
    """Create and return an instance of API client"""
    return SwxApiClient(
        configuration=CONFIGURATION,
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        defer_auth=defer_auth
    )

def get_api_instance(api_name):
    """Create and return an instance of required API class"""
    if api_name == 'collections':
        return collections_api.CollectionsApi(api_client=get_swxclient())
    elif api_name == 'models':
        return models_api.ModelsApi(api_client=get_swxclient())
    else:
        return None

class PositiveSwxApiClientTestClass(unittest.TestCase):
    """Class that tests positive test cases for SwxApiClient"""

    @pytest.mark.run(order=1)
    def test_implicit_do_auth(self):
        """Testing SwxApiClient implicit do_auth()"""
        try:
            # Create an instance of API client
            swxclient = get_swxclient()
            print(swxclient.default_headers)
            assert swxclient.default_headers['Authorization'] is not None
        except Exception as error:
            raise Exception('While executing test_do_auth(): {}'
                            .format(error))

    @pytest.mark.run(order=2)
    def test_explicit_do_auth(self):
        """Testing SwxApiClient explicit do_auth()"""
        try:
            # Create an instance of API client
            swxclient = get_swxclient(defer_auth=True)
            print(swxclient.default_headers)
            assert 'Authorization' not in swxclient.default_headers
            swxclient.do_auth()
            assert swxclient.default_headers['Authorization'] is not None
        except Exception as error:
            raise Exception('While executing test_do_auth(): {}'
                            .format(error))


class NegativeSwxApiClientTestClass(unittest.TestCase):
    """Class that tests negative test cases for SwxApiClient"""

    def test_do_auth_error1(self):
        """Testing SwxApiClient do_auth() error"""
        exception = False
        try:
            # Create an instance of API client with incorrect client_id
            get_swxclient(client_id='test')
        except Exception as error:
            print(error)
            exception = True

        self.assertEqual(exception, True)

    def test_do_auth_error2(self):
        """Testing SwxApiClient do_auth() error"""
        expected_error_msg = 'While initializing SwxApiClient: ' \
            'Cannot initialize SwxApiClient with [client_id, client_secret, scope]={}'.format(
                [environ.get('CLIENT_ID', None), None, environ.get('SCOPE', None)])
        try:
            # Instantiate API client without passing all parameters
            # client_secret not passed here
            SwxApiClient(
                configuration=CONFIGURATION,
                client_id=environ.get('CLIENT_ID', None),
                scope=environ.get('SCOPE', None)
            )
        except Exception as error:
            print(error)
            assert '{}'.format(error) == expected_error_msg
