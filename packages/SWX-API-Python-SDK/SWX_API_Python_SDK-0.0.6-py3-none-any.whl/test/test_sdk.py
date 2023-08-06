"""Module to test PythonApiClient"""

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
from swx_sdk.api import things_api
from swx_sdk.model.thing_request import ThingRequest
from swx_sdk.model.thing_update_request import ThingUpdateRequest
from swx_sdk.api import properties_api
from swx_sdk.model.model_property import ModelProperty


# initialize variables or read from environment
pytest.CLIENT_ID = environ.get('CLIENT_ID', None).strip()
pytest.CLIENT_SECRET = environ.get('CLIENT_SECRET', None).strip()
pytest.SCOPE = environ.get('SCOPE', None).strip()                   # "collection data label thing model"
pytest.SPACE = environ.get('SPACE', None).strip()
pytest.SWX_HOST = environ.get('SWX_HOST', None).strip()
pytest.HTTP_CODE_SUPPORTED = bool(environ.get('HTTP_CODE_SUPPORTED', False))  # the actual http status codes are set in the resp header
pytest.THING_ID = ""
COLLECTION_NEW = 'collnew1'
THING_TITLE_NEW = 'thingnew1'
MODEL_NAME_NEW = 'modelnew1'

class ClientAPIInstance():
    """ClientAPIInstance creates environment based instance of API client"""

    def __init__(self):
        self.client_id = pytest.CLIENT_ID
        self.client_secret = pytest.CLIENT_SECRET
        self.scope = pytest.SCOPE
        self.host = pytest.SWX_HOST
        self.configuration = swx_sdk.Configuration(
            host=pytest.SWX_HOST
        )

        if environ.get('VERIFY_SSL', True) in ['False', 'false']:
            self.configuration.verify_ssl = False

    def get_swxclient(self):
        client_id = self.client_id
        client_secret = self.client_secret
        scope = self.scope
        defer_auth = False

        """Create and return an instance of API client"""
        return SwxApiClient(
            configuration=self.configuration,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            defer_auth=defer_auth
        )

    def get_api_instance(self, api_name):
        """Create and return an instance of required API class"""
        api_client_config = self.get_swxclient()
        if api_name == 'collections':
            return collections_api.CollectionsApi(api_client=api_client_config)
        elif api_name == 'models':
            return models_api.ModelsApi(api_client=api_client_config)
        elif api_name == 'things':
            return things_api.ThingsApi(api_client=api_client_config)
        elif api_name == 'properties':
            return properties_api.PropertiesApi(api_client=api_client_config)
        else:
            return None

class PositivePythonApiClientTestClass(unittest.TestCase):
    """Class that tests positive test cases for PythonApiClient"""

    def setUp(self):

        self.clientAPIInstance = ClientAPIInstance()
        # Set up an instance of the collections API class
        self.collection_api = self.clientAPIInstance.get_api_instance('collections')

        # Set up an instancee of the models API class
        self.model_api = self.clientAPIInstance.get_api_instance('models')

        # Set up an instancee of the things API class
        self.things_api = self.clientAPIInstance.get_api_instance('things')

        # Set up an instancee of the properties API class
        self.properties_api = self.clientAPIInstance.get_api_instance('properties')

        # the actual http status codes are set in the response header
        self.http_code_supported = pytest.HTTP_CODE_SUPPORTED

    @pytest.mark.order(4)
    def test_list_collections(self):
        """Testing list collections request"""
        print("Testing list collections request")

        # Get a list of existing collections for a given space
        space = pytest.SPACE
        try:
            return_data, http_status_code, headers = self.collection_api.list_collections(space, _return_http_data_only=False)
            if self.http_code_supported is True:
                assert(http_status_code == 200)
            else:
                assert(return_data is not None and 'data' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling CollectionsApi->list_collections: %s\n" % e)

    def remove_test_collection(self):
        """Delete test collection"""
        # delete test collection if exists
        try:
            api_response = self.collection_api.list_collections(pytest.SPACE)
            if api_response is not None:
                coll_list = api_response['data']
                for coll in coll_list:
                    if coll['name'] == COLLECTION_NEW:
                        api_response = self.things_api.list_things(pytest.SPACE, COLLECTION_NEW)
                        try:
                            if api_response is not None and 'data' in api_response:
                                things_list = api_response['data']
                                if things_list is not None:
                                    for thing_data in things_list:
                                        pytest.THING_ID = thing_data.get('uid', None)
                                        self.things_api.delete_thing(pytest.SPACE, COLLECTION_NEW, pytest.THING_ID)
                        except swx_sdk.ApiValueError as ve:
                            print("ThingsApi->delete_thing: test things cleanup.  %s\n" % ve)
                        except swx_sdk.ApiAttributeError as ae:
                            print("ThingsApi->delete_thing: test things cleanup.  %s\n" % ae)
                        except swx_sdk.ApiException as e:
                            print("ThingsApi->delete_thing: test things cleanup.  %s\n" % e)
                    self.collection_api.delete_collection(pytest.SPACE, COLLECTION_NEW)
        except swx_sdk.ApiValueError as ve:
            print("CollectionsApi->delete_collection: test collection cleanup.  %s\n" % ve)
        except swx_sdk.ApiAttributeError as ae:
            print("CollectionsApi->delete_collection: test collection cleanup.  %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("CollectionsApi->delete_collection: test collection cleanup.  %s\n" % e)

    @pytest.mark.order(3)
    def test_add_collection(self):
        """Testing add collection request"""
        print("Testing add collections request")
        # Create a collection
        space = pytest.SPACE
        collection_request = CollectionRequest(
            name=COLLECTION_NEW,
            description="description created"
        )
        try:
            # delete test collection if exists
            self.remove_test_collection()
            return_data, http_status_code, headers = self.collection_api.add_collection(
                space,
                collection_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 201 and return_data is not None and 'name' in return_data)
        except swx_sdk.ApiAttributeError as ae:
            print("CollectionsApi->delete_collection: test collection cleanup.  %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling CollectionsApi->add_collection: %s\n" % e)

    @pytest.mark.order(5)
    def test_update_collection(self):
        print("Testing update collections request")

        # Update a collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        collection_update_request = CollectionUpdateRequest(
            description="description updated"
        )
        try:
            return_data, http_status_code, headers = self.collection_api.update_collection(
                space,
                collection_name,
                collection_update_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and \
                   return_data is not None and 'name' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling CollectionsApi->update_collection: %s\n" % e)

    @pytest.mark.order(26)
    def test_delete_collection(self):
        """Testing delete collection request"""
        print("Testing delete collections request")

        # Delete an existing collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        try:
            return_data, http_status_code, headers = self.collection_api.delete_collection(
                space,
                collection_name,
                _return_http_data_only=False
            )
            assert(http_status_code == 204)
        except swx_sdk.ApiException as e:
            print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)

    @pytest.mark.order(7)
    def test_list_models(self):
        """Testing list models request"""
        print("Testing list models request")

        # Get a list of all existing models in a given collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        try:
            return_data, http_status_code, headers = self.model_api.list_models(
                space,
                collection_name,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'data' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling ModelsApi->list_models: %s\n" % e)

    @pytest.mark.order(6)
    def test_add_model(self):
        """Testing add model request"""
        print("Testing add model request")

        # Create a model in a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_request = ModelRequest(
            name=MODEL_NAME_NEW,
            description="test model description"
        )
        try:
            return_data, http_status_code, headers = self.model_api.add_model(
                space,
                collection_name,
                model_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 201 and 'name' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling ModelsApi->add_model: %s\n" % e)

    @pytest.mark.order(8)
    def test_update_model(self):
        """Testing update model request"""
        print("Testing update model request")

        # Update a model in specific space, collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_name = MODEL_NAME_NEW
        model_update_request = ModelUpdateRequest(
            description="model description updated"
        )

        try:
            return_data, http_status_code, headers = self.model_api.update_model(
                space,
                collection_name,
                model_name,
                model_update_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'name' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling ModelsApi->update_model: %s\n" % e)

    @pytest.mark.order(24)
    def test_delete_model(self):
        """Testing delete model request"""
        print("Testing delete model request")

        # Delete a model from a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_name = MODEL_NAME_NEW
        try:
            return_data, http_status_code, headers = self.model_api.delete_model(
                space,
                collection_name,
                model_name,
                _return_http_data_only=False
            )
            print("test_delete_model_not_found return data: {}, http_status_code: {}".format(return_data, http_status_code))
            assert(http_status_code == 204)
        except swx_sdk.ApiException as e:
            print("Exception when calling ModelsApi->delete_model: %s\n" % e)

    @pytest.mark.order(11)
    def test_list_things(self):
        """Testing list things request"""
        print("Testing list things request")

        # Get a list of all existing things in a given collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        try:
            return_data, http_status_code, headers = self.things_api.list_things(
                space,
                collection_name,
                _return_http_data_only=False)
            assert(http_status_code == 200 and return_data is not None and 'data' in return_data)
        except swx_sdk.ApiValueError as ve:
            print("Exception when calling ThingsApi->list_things: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->list_things: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->list_things: %s\n" % e)

    @pytest.mark.order(10)
    def test_show_thing(self):
        """Testing show thing request"""
        print("Testing show thing request")

        # Show a thing given collection name, space, thing_id
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_id = pytest.THING_ID
        try:
            return_data, http_status_code, headers = self.things_api.show_thing(
                space,
                collection_name,
                thing_id,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'uid' in return_data)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling ThingsApi->show_thing: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->show_thing: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->show_thing: %s\n" % e)

    @pytest.mark.order(9)
    def test_add_thing(self):
        """Testing add thing request"""
        print("Testing add thing request")

        # Create a thing in a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_request = ThingRequest(
            title=THING_TITLE_NEW,
            description='thing descr',
            properties={
                "property1": {
                    "description": "property 1 of {}".format(THING_TITLE_NEW),
                    "readOnly": False,
                    "title": "Property 1",
                    "type": "number",
                    "unit": "percent"
                }
            }
        )
        try:
            return_data, http_status_code, headers = self.things_api.add_thing(
                space,
                collection_name,
                thing_request,
                _return_http_data_only=False
            )
            pytest.THING_ID = return_data['uid']
            assert(http_status_code == 201 and return_data is not None and 'uid' in return_data)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->add_thing: %s\n" % e)

    @pytest.mark.order(12)
    def test_update_thing_desc(self):
        """Testing update thing request"""
        print("Testing update thing request")

        # Update a thing of a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_id = pytest.THING_ID
        thing_update_request = ThingUpdateRequest(
            description="updated descr"
        )
        try:
            return_data, http_status_code, headers = self.things_api.update_thing(
                space,
                collection_name,
                thing_id,
                thing_update_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'uid' in return_data)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling ThingsApi->update_thing: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->update_thing: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->update_thing: %s\n" % e)

    @pytest.mark.order(12)
    def test_update_thing_property(self):
        """Testing update thing request for updating thing property"""
        print("Testing update thing request for updating thing property")

        # Update a thing of a given collection and space
        thing_update_request = ThingUpdateRequest(
            title=THING_TITLE_NEW,
            description='thing property updated',
            properties={
                "property1": {
                    "description": "Type changed",
                    "readOnly": False,
                    "title": "Property 1",
                    "type": "string"
                },
                "property2": {
                    "description": "property 2 of {}".format(THING_TITLE_NEW),
                    "readOnly": False,
                    "title": "Property 2",
                    "type": "number",
                    "unit": "percent"
                }
            },
            actions={
                "Action1": {
                    "title": "Action 1",
                    "description": "action 1 on {}".format(THING_TITLE_NEW),
                    "input": {
                        "properties": {
                            "input": {
                                "maximum": 100,
                                "minimum": 3,
                                "type": "number"
                            }
                        }
                    }
                }
            },
            events={
                "Event1": {
                    "title": "Event 1",
                    "description": "Event 1 on {}".format(THING_TITLE_NEW),
                    "data": {
                        "type": "number",
                        "unit": "percent"
                    }
                }
            }
        )
        try:
            return_data, http_status_code, headers = self.things_api.update_thing(
                pytest.SPACE,
                COLLECTION_NEW,
                pytest.THING_ID,
                thing_update_request,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'uid' in return_data)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling ThingsApi->update_thing: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->update_thing: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->update_thing: %s\n" % e)

    @pytest.mark.order(14)
    def test_list_properties(self):
        """Testing list properties request"""
        print("Testing list properties request")

        # Get a list of all existing properties of a given thing in a given collection
        try:
            return_data, http_status_code, headers = self.properties_api.list_properties(
                pytest.SPACE,
                COLLECTION_NEW,
                pytest.THING_ID,
                _return_http_data_only=False
            )
            assert(http_status_code == 200 and return_data is not None and 'error_things_backend' not in return_data)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling PropertiessApi->update_property: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling PropertiessApi->update_property: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling PropertiessApi->update_property: %s\n" % e)

    @pytest.mark.order(14)
    def test_show_property(self):
        """Testing show property request"""
        print("Testing show property request")

        # Show a property of thing given collection name, space, thing_id
        model_property = ModelProperty(
            property2=100.0
        )
        try:
            return_data, http_status_code, headers = self.properties_api.show_property(
                pytest.SPACE,
                COLLECTION_NEW,
                pytest.THING_ID,
                "property2",
                _return_http_data_only=False
            )
            print(return_data)
            assert(http_status_code == 200 and return_data == model_property)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling PropertiessApi->update_property: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling PropertiessApi->update_property: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling PropertiessApi->update_property: %s\n" % e)

    @pytest.mark.order(13)
    def test_update_property(self):
        """Testing update property request"""
        print("Testing update property request")

        # Update property of a thing of a given collection and space
        model_property = ModelProperty(
            property2=100.0
        )
        try:
            return_data, http_status_code, headers = self.properties_api.update_property(
                pytest.SPACE,
                COLLECTION_NEW,
                pytest.THING_ID,
                "property2",
                model_property,
                _return_http_data_only=False
            )
            assert(http_status_code == 201 and return_data == model_property)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling PropertiessApi->update_property: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling PropertiessApi->update_property: %s\n" % ae)
        except swx_sdk.ApiException as e:
            print("Exception when calling PropertiessApi->update_property: %s\n" % e)

    @pytest.mark.order(25)
    def test_delete_thing(self):
        """Testing delete thing request"""
        print("Testing delete thing request")

        # Delete a thing from a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_id = pytest.THING_ID
        try:
            return_data, http_status_code, headers = self.things_api.delete_thing(
                space,
                collection_name,
                thing_id,
                _return_http_data_only=False
            )
            assert(http_status_code == 204)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->delete_thing: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->delete_thing: %s\n" % e)

class NegativePythonApiClientTestClass(unittest.TestCase):
    """Class that tests negative test cases for PythonApiClient"""

    def setUp(self):

        self.clientAPIInstance = ClientAPIInstance()
        # Set up an instance of the collections API class
        self.collection_api = self.clientAPIInstance.get_api_instance('collections')

        # Set up an instancee of the models API class
        self.model_api = self.clientAPIInstance.get_api_instance('models')

        # Set up an instancee of the things API class
        self.things_api = self.clientAPIInstance.get_api_instance('things')

        # Set up an instancee of the properties API class
        self.properties_api = self.clientAPIInstance.get_api_instance('properties')

        # the actual http status codes are set in the response header
        self.http_code_supported = pytest.HTTP_CODE_SUPPORTED

    @pytest.mark.order(13)
    def test_list_collections_space_not_found(self):
        """Testing list collections request"""
        print("Testing list collections request. Space not found")

        # Get a list of existing collections for a given space
        space = "notfound1"
        try:
            self.collection_api.list_collections(space)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling CollectionsApi->list_collections: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling CollectionsApi->list_collections:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 403)
            self.assertEqual(e.reason, "Forbidden")
            self.assertRegex(e.body, "Access credentials are not sufficient to access this resource")

    @pytest.mark.order(14)
    def test_add_collection_already_exists(self):
        """Testing add collection request"""
        print("Testing add collections request. Collection already exists.")

        # Create a collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        collection_request = CollectionRequest(
            name=collection_name,
            description='descr1'
        )
        try:
            self.collection_api.add_collection(space, collection_request)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 400)
            self.assertEqual(e.reason, "Bad Request")
            self.assertRegex(e.body, "the collection already exists")

    @pytest.mark.order(15)
    def test_update_collection_not_found(self):
        """Testing update collection request"""
        print("Testing update collections request. Collection not found.")

        # Update a collection
        space = pytest.SPACE
        collection_name = "notfound1"
        collection_update_request = CollectionUpdateRequest(
            description='descr1'
        )
        try:
            self.collection_api.update_collection(
                space,
                collection_name,
                collection_update_request
            )
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")
            self.assertEqual(e.body, 'null')

    @pytest.mark.order(23)
    def test_delete_collection_not_found(self):
        """Testing delete collection request"""
        print("Testing delete collections request. Collection not found.")

        # Delete an existing collection
        space = pytest.SPACE
        collection_name = 'notfound1'
        try:
            self.collection_api.delete_collection(space, collection_name, _return_http_data_only=False)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")
            self.assertEqual(e.body, 'null')

    @pytest.mark.order(16)
    def test_list_models_collection_not_found(self):
        """Testing list models request"""
        print("Testing list models request. Collection not found")

        # Get a list of all existing models in a given collection
        space = pytest.SPACE
        collection_name = 'notfound1'
        try:
            self.model_api.list_models(space, collection_name, _return_http_data_only=False)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")
            self.assertEqual(e.body, 'null')

    @pytest.mark.order(17)
    def test_add_model_already_exists(self):
        """Testing add model request"""
        print("Testing add model request. Model already exists.")

        # Create a model in a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_request = ModelRequest(
            name=MODEL_NAME_NEW,
            description="model description"
        )
        try:
            self.model_api.add_model(
                space,
                collection_name,
                model_request
            )
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError: unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 400)
            self.assertEqual(e.reason, "Bad Request")
            self.assertEqual(e.body, '{"error":{"message":"the model already exists"}}')

    @pytest.mark.order(18)
    def test_update_model_not_found(self):
        """Testing update model request"""
        print("Testing update model request. Model not found.")
        # Update a model in specific space, collection
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_name = 'notfound1'
        model_update_request = ModelUpdateRequest(
            description="model description update"
        )
        try:
            self.model_api.update_model(
                space,
                collection_name,
                model_name,
                model_update_request
            )
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ModelsApi->update_model:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")
            self.assertEqual(e.body, 'null')

    @pytest.mark.order(19)
    def test_delete_model_not_found(self):
        """Testing delete model request."""
        print("Testing delete model request. Model not found.")
        # Delete a model from a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        model_name = "notfound1"
        try:
            return_data, http_status_code, headers = self.model_api.delete_model(
                space,
                collection_name,
                model_name,
                _return_http_data_only=False
            )
            assert(http_status_code == 204)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ModelsApi->delete_model:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            print("Exception when calling ModelsApi->delete_model: %s\n" % e)

    @pytest.mark.order(20)
    def test_list_things_collection_not_found(self):
        """Testing list things request."""
        print("Testing list things request. Collection not found.")

        # Get a list of all existing things in a given collection
        space = pytest.SPACE
        collection_name = 'notfound1'
        try:
            return_data, http_status_code, headers = self.things_api.list_things(space, collection_name, _return_http_data_only=False)
            assert(http_status_code == 200)
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling CollectionsApi->list_collections: %s\n" % ve)
        except swx_sdk.ApiException as e:
            print("Exception when calling ThingsApi->list_things: %s\n" % e)

    @pytest.mark.order(21)
    def test_add_thing_collection_not_found(self):
        """Testing add thing request"""
        print("Testing add thing request. Collection not found.")

        # Create a thing in a given collection and space
        space = pytest.SPACE
        collection_name = 'notfound1'
        thing_request = ThingRequest(
            title=THING_TITLE_NEW,
            description='thing descr'
        )
        try:
            self.things_api.add_thing(space, collection_name, thing_request)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError: unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 400)
            self.assertEqual(e.reason, "Bad Request")
            self.assertEqual(e.body, '{"error":{"message":"error on finding collection"}}')

    @pytest.mark.order(22)
    def test_update_thing_not_found(self):
        """Testing update thing request"""
        print("Testing update thing request. Thing id not found.")

        # Update a thing of a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_id = 'notfound1'
        thing_update_request = ThingUpdateRequest(
            description="updated descr"
        )
        try:
            self.things_api.update_thing(
                space,
                collection_name,
                thing_id,
                thing_update_request
            )
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->update_thing:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")

    @pytest.mark.order(22)
    def test_update_property_not_found(self):
        """Testing update property request"""
        print("Testing update property request")

        # Update property of a thing of a given collection and space
        model_property = ModelProperty(
            notfound1=100.0
        )
        try:
            self.properties_api.update_property(
                pytest.SPACE,
                COLLECTION_NEW,
                pytest.THING_ID,
                "notfound1",
                model_property
            )
        except swx_sdk.ApiValueError as ve:
            print("ApiValueError when calling PropertiessApi->update_property: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling PropertiessApi->update_property: %s\n" % ae)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 400)
            self.assertEqual(e.reason, "Bad Request")
            self.assertEqual(e.body, '{"error":{"message":"invalid property"}}')

    @pytest.mark.order(23)
    def test_delete_thing_not_found(self):
        """Testing delete thing request"""
        print("Testing delete thing request. Thing id not found")

        # Delete a thing from a given collection and space
        space = pytest.SPACE
        collection_name = COLLECTION_NEW
        thing_id = 'notfound1'
        try:
            self.things_api.delete_thing(
                space,
                collection_name,
                thing_id
            )
        except swx_sdk.ApiValueError as ve:
            print("Exception when calling ThingsApi->delete_thing: %s\n" % ve)
        except swx_sdk.exceptions.ApiAttributeError as ae:
            print("ApiAttributeError when calling ThingsApi->delete_thing:  unsupported attribute error: %s\n" % ae)
            assert(True)
        except swx_sdk.ApiException as e:
            self.assertEqual(e.status, 404)
            self.assertEqual(e.reason, "Not Found")
            self.assertEqual(e.body, '{"error":{"code":404,"message":"Requested url does not match any rules","status":"Not Found"}}')
