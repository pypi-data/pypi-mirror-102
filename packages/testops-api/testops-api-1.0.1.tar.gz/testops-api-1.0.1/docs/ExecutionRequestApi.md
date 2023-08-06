# testops_api.ExecutionRequestApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download3**](ExecutionRequestApi.md#download3) | **GET** /api/v1/requests/{id}/download | Downloads an Execution Request report. Returns the report file.
[**get_execution_request**](ExecutionRequestApi.md#get_execution_request) | **GET** /api/v1/requests/{id} | Returns an Execution Request detail.


# **download3**
> download3(id)

Downloads an Execution Request report. Returns the report file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_request_api
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
    api_instance = execution_request_api.ExecutionRequestApi(api_client)
    id = 1 # int | 
    file_type = "har" # str |  (optional) if omitted the server will use the default value of "har"

    # example passing only required values which don't have defaults set
    try:
        # Downloads an Execution Request report. Returns the report file.
        api_instance.download3(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionRequestApi->download3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Downloads an Execution Request report. Returns the report file.
        api_instance.download3(id, file_type=file_type)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionRequestApi->download3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **file_type** | **str**|  | [optional] if omitted the server will use the default value of "har"

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_request**
> ExecutionRequestResource get_execution_request(id)

Returns an Execution Request detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_request_api
from testops_api.model.execution_request_resource import ExecutionRequestResource
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
    api_instance = execution_request_api.ExecutionRequestApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an Execution Request detail.
        api_response = api_instance.get_execution_request(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionRequestApi->get_execution_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionRequestResource**](ExecutionRequestResource.md)

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

