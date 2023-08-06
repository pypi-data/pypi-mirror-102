# testops_api.TaskApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_incident**](TaskApi.md#create_incident) | **POST** /api/v1/incidents | Creates a Task for the test results. Returns the created Task detail.
[**get11**](TaskApi.md#get11) | **GET** /api/v1/incidents/{id} | Returns a Task detail.
[**update7**](TaskApi.md#update7) | **PUT** /api/v1/incidents | Updates a Task detail. Returns the updated Task detail.


# **create_incident**
> IncidentResource create_incident(incident_resource)

Creates a Task for the test results. Returns the created Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
from pprint import pprint
# Defining the host is optional and defaults to https://testops.katalon.io
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "https://testops.katalon.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    incident_resource = IncidentResource(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        team_id=1,
        url_ids=[
            "url_ids_example",
        ],
        execution_test_result_ids=[
            1,
        ],
        order=1,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IncidentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a Task for the test results. Returns the created Task detail.
        api_response = api_instance.create_incident(incident_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->create_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_resource** | [**IncidentResource**](IncidentResource.md)|  |

### Return type

[**IncidentResource**](IncidentResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get11**
> IncidentResource get11(id)

Returns a Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
from pprint import pprint
# Defining the host is optional and defaults to https://testops.katalon.io
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "https://testops.katalon.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Task detail.
        api_response = api_instance.get11(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->get11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**IncidentResource**](IncidentResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update7**
> IncidentResource update7(incident_resource)

Updates a Task detail. Returns the updated Task detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import task_api
from testops_api.model.incident_resource import IncidentResource
from pprint import pprint
# Defining the host is optional and defaults to https://testops.katalon.io
# See configuration.py for a list of all supported configuration parameters.
configuration = testops_api.Configuration(
    host = "https://testops.katalon.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicScheme
configuration = testops_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with testops_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    incident_resource = IncidentResource(
        id=1,
        name="name_example",
        description="description_example",
        project_id=1,
        team_id=1,
        url_ids=[
            "url_ids_example",
        ],
        execution_test_result_ids=[
            1,
        ],
        order=1,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IncidentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Task detail. Returns the updated Task detail.
        api_response = api_instance.update7(incident_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TaskApi->update7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_resource** | [**IncidentResource**](IncidentResource.md)|  |

### Return type

[**IncidentResource**](IncidentResource.md)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

