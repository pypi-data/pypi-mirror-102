"""Module to test SWX-SDK Data API"""

from os import environ
import unittest
import pytest
import swx_sdk
from swx_sdk.swx_api_client import SwxApiClient
from swx_sdk.api import data_api

pytest.SPACE = environ.get('SPACE', None).strip()
pytest.SOURCE = environ.get('SOURCE', None).strip()
pytest.NEG_SPACE = "test1negative2space3"
pytest.NEG_DATA_ID = "00TEST00NEGATIVE00DATAID00"
pytest.data_source = None

class ClientAPIInstance():
    """ClientAPIInstance creates environment based instance of API client"""

    def __init__(self):

        # initialize variables or read from environment
        self.SWX_HOST = environ.get('SWX_HOST', None).strip()
        self.CLIENT_ID = environ.get('CLIENT_ID', None).strip()
        self.CLIENT_SECRET = environ.get('CLIENT_SECRET', None).strip()
        self.SCOPE = environ.get('SCOPE', None).strip()

        self.CONFIGURATION = swx_sdk.Configuration(
            host=self.SWX_HOST
        )

        if environ.get('VERIFY_SSL', True) in ['False', 'false']:
            self.CONFIGURATION.verify_ssl = False

    def get_swxclient(self, defer_auth=False):
        """Create and return an instance of API client"""
        return SwxApiClient(
            configuration=self.CONFIGURATION,
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            scope=self.SCOPE,
            defer_auth=defer_auth
        )

    def get_api_instance(self):
        """Create and return an instance of Data API class"""
        return data_api.DataApi(api_client=self.get_swxclient())

class CreateDataTestClass(unittest.TestCase):

    @pytest.mark.order(3)
    def test_negative_create_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.create_data(
                pytest.NEG_SPACE, None, _return_http_data_only=False
            )
            print(f'Response from DataApi->create_data: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->create_data: %s\n" % e)
            assert e.status == 403 and 'error' in e.body

    @pytest.mark.order(4)
    def test_positive_create_data(self):
        contents = [{
            'cpu': {'percentage': '10.7'},
            'disk': {'percentage': '52.1'},
            'memory': {'percentage': '65.9'},
        }, "{\n  \"hello\": \"world\"\n}", 12345, False, None, {'hello': 'world'}]

        api_instance = ClientAPIInstance().get_api_instance()
        try:
            for content in contents:
                body, status, headers = api_instance.create_data(
                    pytest.SPACE, content, _return_http_data_only=False
                )
                print(f'Response from DataApi->create_data: ({status}) {body}')
                assert status == 201 and body is not None and 'result' in body
                pytest.data_source = body.result
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->create_data: %s\n" % e)
            assert False

class ListDataTestClass(unittest.TestCase):

    @pytest.mark.order(5)
    def test_negative_list_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.list_data(
                pytest.NEG_SPACE, pytest.SOURCE, _return_http_data_only=False
            )
            print(f'Response from DataApi->list_data: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->list_data: %s\n" % e)
            assert e.status == 403 and 'error' in e.body

    @pytest.mark.order(6)
    def test_positive_list_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.list_data(
                pytest.SPACE, pytest.SOURCE, _return_http_data_only=False
            )
            print(f'Response from DataApi->list_data: ({status}) {body}')
            assert status == 200 and body is not None and 'collection' in body
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->list_data: %s\n" % e)
            assert False

class DeleteDataFromSourceTestClass(unittest.TestCase):

    @pytest.mark.order(11)
    def test_negative_delete_data_from_source(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.delete_data_from_source(
                pytest.NEG_SPACE, pytest.SOURCE, _return_http_data_only=False
            )
            print(f'Response from DataApi->delete_data_from_source: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->delete_data_from_source: %s\n" % e)
            assert e.status == 403 and 'error' in e.body

    @pytest.mark.order(12)
    def test_positive_delete_data_from_source(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.delete_data_from_source(
                pytest.SPACE, pytest.SOURCE, _return_http_data_only=False
            )
            print(f'Response from DataApi->delete_data_from_source: ({status}) {body}')
            assert status == 204 and body is None
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->delete_data_from_source: %s\n" % e)
            assert False

class ShowDataTestClass(unittest.TestCase):

    @pytest.mark.order(7)
    def test_negative_show_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            # Negative space
            body, status, headers = api_instance.show_data(
                pytest.NEG_SPACE, pytest.SOURCE, _return_http_data_only=False
            )
            print(f'Response from DataApi->show_data: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->show_data: %s\n" % e)
            assert e.status == 403 and 'error' in e.body

        try:
            # Negative data_id
            body, status, headers = api_instance.show_data(
                pytest.SPACE, pytest.NEG_DATA_ID, _return_http_data_only=False
            )
            print(f'Response from DataApi->show_data: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->show_data: %s\n" % e)
            assert e.status == 404 and 'error' in e.body

    @pytest.mark.order(8)
    def test_positive_show_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.show_data(
                pytest.SPACE, pytest.data_source, _return_http_data_only=False
            )
            print(f'Response from DataApi->show_data: ({status}) {body}')
            assert(status == 200 and body is not None and 'at' in body
                and 'id' in body and 'content' in body
                and 'source_id' in body)

            # with Download
            body, status, headers = api_instance.show_data(
                pytest.SPACE, pytest.data_source, download=True, _return_http_data_only=False
            )
            print(f'Response from DataApi->show_data: ({status}) {body}')
            assert status == 200 and body is not None

            # with Metadata
            body, status, headers = api_instance.show_data(
                pytest.SPACE, pytest.data_source, metadata=True, _return_http_data_only=False
            )
            print(f'Response from DataApi->show_data: ({status}) {body}')
            assert(status == 200 and body is not None and 'Metadata' in body
                and 'at' in body and 'id' in body
                and 'content' in body and 'source_id' in body)
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->show_data: %s\n" % e)
            assert False

class DeleteDataTestClass(unittest.TestCase):

    @pytest.mark.order(9)
    def test_negative_delete_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.delete_data(
                pytest.NEG_SPACE, pytest.data_source, _return_http_data_only=False
            )
            print(f'Response from DataApi->delete_data: ({status}) {body}')
            assert False
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->delete_data: %s\n" % e)
            assert e.status == 403 and 'error' in e.body

    @pytest.mark.order(10)
    def test_positive_delete_data(self):
        api_instance = ClientAPIInstance().get_api_instance()
        try:
            body, status, headers = api_instance.delete_data(
                pytest.SPACE, pytest.data_source, _return_http_data_only=False
            )
            print(f'Response from DataApi->delete_data: ({status}) {body}')
            assert status == 204 and body is None
        except swx_sdk.ApiException as e:
            print("Exception when calling DataApi->delete_data: %s\n" % e)
            assert False
