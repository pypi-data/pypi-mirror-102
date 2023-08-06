# testops_api.ExecutionTestResultApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get17**](ExecutionTestResultApi.md#get17) | **GET** /api/v1/test-results/{id} | Returns an Execution Test Result detail.
[**get_stdout**](ExecutionTestResultApi.md#get_stdout) | **GET** /api/v1/test-results/logs/{id} | Downloads a test result&#39;s log. Returns the log file.
[**link_incidents**](ExecutionTestResultApi.md#link_incidents) | **POST** /api/v1/test-results/{id}/incidents | Link an Execution Test Result to a Task. Returns the created binding detail.
[**mark_as_retested**](ExecutionTestResultApi.md#mark_as_retested) | **POST** /api/v1/test-results/{id}/mask-as-retested | 
[**unlink_incidents**](ExecutionTestResultApi.md#unlink_incidents) | **DELETE** /api/v1/test-results/{id}/incidents | Unlink an Execution Test Result to a Task. Returns the deleted binding detail.


# **get17**
> ExecutionTestResultResource get17(id)

Returns an Execution Test Result detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_test_result_api
from testops_api.model.execution_test_result_resource import ExecutionTestResultResource
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
    api_instance = execution_test_result_api.ExecutionTestResultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an Execution Test Result detail.
        api_response = api_instance.get17(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionTestResultApi->get17: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ExecutionTestResultResource**](ExecutionTestResultResource.md)

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

# **get_stdout**
> str get_stdout(id)

Downloads a test result's log. Returns the log file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_test_result_api
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
    api_instance = execution_test_result_api.ExecutionTestResultApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Downloads a test result's log. Returns the log file.
        api_response = api_instance.get_stdout(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionTestResultApi->get_stdout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

**str**

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_incidents**
> IncidentExecutionTestResultResource link_incidents(id, incident_execution_test_result_resource)

Link an Execution Test Result to a Task. Returns the created binding detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_test_result_api
from testops_api.model.incident_execution_test_result_resource import IncidentExecutionTestResultResource
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
    api_instance = execution_test_result_api.ExecutionTestResultApi(api_client)
    id = "id_example" # str | 
    incident_execution_test_result_resource = IncidentExecutionTestResultResource(
        id=1,
        incident_id=1,
        project_id=1,
        incident_order=1,
        execution_test_result_id=1,
    ) # IncidentExecutionTestResultResource | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution Test Result to a Task. Returns the created binding detail.
        api_response = api_instance.link_incidents(id, incident_execution_test_result_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionTestResultApi->link_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_execution_test_result_resource** | [**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)|  |

### Return type

[**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)

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

# **mark_as_retested**
> ExecutionTestResultResource mark_as_retested(id)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_test_result_api
from testops_api.model.execution_test_result_resource import ExecutionTestResultResource
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
    api_instance = execution_test_result_api.ExecutionTestResultApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_as_retested(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionTestResultApi->mark_as_retested: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ExecutionTestResultResource**](ExecutionTestResultResource.md)

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

# **unlink_incidents**
> IncidentExecutionTestResultResource unlink_incidents(id, incident_execution_test_result_resource)

Unlink an Execution Test Result to a Task. Returns the deleted binding detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_test_result_api
from testops_api.model.incident_execution_test_result_resource import IncidentExecutionTestResultResource
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
    api_instance = execution_test_result_api.ExecutionTestResultApi(api_client)
    id = "id_example" # str | 
    incident_execution_test_result_resource = IncidentExecutionTestResultResource(
        id=1,
        incident_id=1,
        project_id=1,
        incident_order=1,
        execution_test_result_id=1,
    ) # IncidentExecutionTestResultResource | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Execution Test Result to a Task. Returns the deleted binding detail.
        api_response = api_instance.unlink_incidents(id, incident_execution_test_result_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionTestResultApi->unlink_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_execution_test_result_resource** | [**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)|  |

### Return type

[**IncidentExecutionTestResultResource**](IncidentExecutionTestResultResource.md)

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

