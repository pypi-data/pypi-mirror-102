# testops_api.FileApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download2**](FileApi.md#download2) | **GET** /api/v1/files/{id} | Downloads a file.
[**get_upload_url**](FileApi.md#get_upload_url) | **GET** /api/v1/files/upload-url | Returns an upload URL.
[**get_upload_urls**](FileApi.md#get_upload_urls) | **GET** /api/v1/files/upload-urls | Returns multiple upload URLs.


# **download2**
> download2(id)

Downloads a file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import file_api
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
    api_instance = file_api.FileApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Downloads a file.
        api_instance.download2(id)
    except testops_api.ApiException as e:
        print("Exception when calling FileApi->download2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **get_upload_url**
> FileResource get_upload_url(project_id)

Returns an upload URL.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import file_api
from testops_api.model.file_resource import FileResource
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
    api_instance = file_api.FileApi(api_client)
    project_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an upload URL.
        api_response = api_instance.get_upload_url(project_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling FileApi->get_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |

### Return type

[**FileResource**](FileResource.md)

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

# **get_upload_urls**
> [FileResource] get_upload_urls(project_id, number_url)

Returns multiple upload URLs.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import file_api
from testops_api.model.file_resource import FileResource
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
    api_instance = file_api.FileApi(api_client)
    project_id = 1 # int | 
    number_url = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns multiple upload URLs.
        api_response = api_instance.get_upload_urls(project_id, number_url)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling FileApi->get_upload_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **number_url** | **int**|  |

### Return type

[**[FileResource]**](FileResource.md)

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

