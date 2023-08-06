# testops_api.KatalonRecorderApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup**](KatalonRecorderApi.md#backup) | **POST** /api/v1/katalon-recorder/backup | Saves a Katalon Recorder backup detail.
[**download4**](KatalonRecorderApi.md#download4) | **GET** /api/v1/katalon-recorder/backup/{id}/download | Downloads a Katalon Recorder backup. Returns the backup file.
[**upload1**](KatalonRecorderApi.md#upload1) | **POST** /api/v1/katalon-recorder/test-reports | Uploads and processes a Katalon Recorder report.


# **backup**
> backup(uploaded_path)

Saves a Katalon Recorder backup detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import katalon_recorder_api
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
    api_instance = katalon_recorder_api.KatalonRecorderApi(api_client)
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Saves a Katalon Recorder backup detail.
        api_instance.backup(uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling KatalonRecorderApi->backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_path** | **str**|  |

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

# **download4**
> download4(id)

Downloads a Katalon Recorder backup. Returns the backup file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import katalon_recorder_api
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
    api_instance = katalon_recorder_api.KatalonRecorderApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Downloads a Katalon Recorder backup. Returns the backup file.
        api_instance.download4(id)
    except testops_api.ApiException as e:
        print("Exception when calling KatalonRecorderApi->download4: %s\n" % e)
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

# **upload1**
> upload1(project_id, batch, is_end, file_name, uploaded_path)

Uploads and processes a Katalon Recorder report.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import katalon_recorder_api
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
    api_instance = katalon_recorder_api.KatalonRecorderApi(api_client)
    project_id = "projectId_example" # str | 
    batch = "batch_example" # str | 
    is_end = "isEnd_example" # str | 
    file_name = "fileName_example" # str | 
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Uploads and processes a Katalon Recorder report.
        api_instance.upload1(project_id, batch, is_end, file_name, uploaded_path)
    except testops_api.ApiException as e:
        print("Exception when calling KatalonRecorderApi->upload1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **batch** | **str**|  |
 **is_end** | **str**|  |
 **file_name** | **str**|  |
 **uploaded_path** | **str**|  |

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

