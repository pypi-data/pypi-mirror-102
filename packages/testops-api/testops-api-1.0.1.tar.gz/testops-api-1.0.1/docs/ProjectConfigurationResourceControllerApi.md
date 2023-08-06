# testops_api.ProjectConfigurationResourceControllerApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get14**](ProjectConfigurationResourceControllerApi.md#get14) | **GET** /api/v1/project-configurations/{id} | 
[**list_time_zones**](ProjectConfigurationResourceControllerApi.md#list_time_zones) | **GET** /api/v1/time-zones | 
[**update10**](ProjectConfigurationResourceControllerApi.md#update10) | **POST** /api/v1/project-configurations/{id} | 


# **get14**
> ProjectConfigurationResource get14(id, name)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_configuration_resource_controller_api
from testops_api.model.project_configuration_resource import ProjectConfigurationResource
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
    api_instance = project_configuration_resource_controller_api.ProjectConfigurationResourceControllerApi(api_client)
    id = 1 # int | 
    name = "TIMEZONE" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get14(id, name)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectConfigurationResourceControllerApi->get14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **name** | **str**|  |

### Return type

[**ProjectConfigurationResource**](ProjectConfigurationResource.md)

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

# **list_time_zones**
> [TimeZoneResource] list_time_zones()



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_configuration_resource_controller_api
from testops_api.model.time_zone_resource import TimeZoneResource
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
    api_instance = project_configuration_resource_controller_api.ProjectConfigurationResourceControllerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_time_zones()
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectConfigurationResourceControllerApi->list_time_zones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[TimeZoneResource]**](TimeZoneResource.md)

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

# **update10**
> ProjectConfigurationResource update10(id, project_configuration_resource)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import project_configuration_resource_controller_api
from testops_api.model.project_configuration_resource import ProjectConfigurationResource
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
    api_instance = project_configuration_resource_controller_api.ProjectConfigurationResourceControllerApi(api_client)
    id = 1 # int | 
    project_configuration_resource = ProjectConfigurationResource(
        name="TIMEZONE",
        value="value_example",
    ) # ProjectConfigurationResource | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update10(id, project_configuration_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ProjectConfigurationResourceControllerApi->update10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **project_configuration_resource** | [**ProjectConfigurationResource**](ProjectConfigurationResource.md)|  |

### Return type

[**ProjectConfigurationResource**](ProjectConfigurationResource.md)

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

