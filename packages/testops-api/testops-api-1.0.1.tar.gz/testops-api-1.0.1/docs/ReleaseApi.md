# testops_api.ReleaseApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_release**](ReleaseApi.md#active_release) | **POST** /api/v1/releases/{id}/active | Open or close a Release. Returns the updated Release detail.
[**create_or_update2**](ReleaseApi.md#create_or_update2) | **POST** /api/v1/releases | Creates or updates a Release. Returns the Release details.
[**delete5**](ReleaseApi.md#delete5) | **DELETE** /api/v1/releases/{id} | Deletes a Release. Returns the Release details.
[**update8**](ReleaseApi.md#update8) | **PUT** /api/v1/releases | Updates a Release. Returns the Release details.


# **active_release**
> ReleaseResource active_release(id, closed)

Open or close a Release. Returns the updated Release detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 
    closed = True # bool | 

    # example passing only required values which don't have defaults set
    try:
        # Open or close a Release. Returns the updated Release detail.
        api_response = api_instance.active_release(id, closed)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->active_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **closed** | **bool**|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **create_or_update2**
> ReleaseResource create_or_update2(release_resource)

Creates or updates a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    release_resource = ReleaseResource(
        id=1,
        name="name_example",
        start_time=dateutil_parser('1970-01-01').date(),
        end_time=dateutil_parser('1970-01-01').date(),
        description="description_example",
        project_id=1,
        closed=True,
        external_release=ExternalReleaseResource(
            id=1,
            release_id="release_id_example",
            description="description_example",
            name="name_example",
            archived=True,
            released=True,
            external_project=ExternalProjectResource(
                id=1,
                external_project_id="external_project_id_example",
                external_project_key="external_project_key_example",
                name="name_example",
            ),
            web_url="web_url_example",
        ),
        release_statistics=ReleaseStatisticsResource(
            id=1,
            release=ReleaseResource(ReleaseResource),
            total_passed=1,
            total_failed=1,
            total_execution=1,
        ),
    ) # ReleaseResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates or updates a Release. Returns the Release details.
        api_response = api_instance.create_or_update2(release_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->create_or_update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **delete5**
> ReleaseResource delete5(id)

Deletes a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Release. Returns the Release details.
        api_response = api_instance.delete5(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->delete5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

# **update8**
> ReleaseResource update8(release_resource)

Updates a Release. Returns the Release details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import release_api
from testops_api.model.release_resource import ReleaseResource
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
    api_instance = release_api.ReleaseApi(api_client)
    release_resource = ReleaseResource(
        id=1,
        name="name_example",
        start_time=dateutil_parser('1970-01-01').date(),
        end_time=dateutil_parser('1970-01-01').date(),
        description="description_example",
        project_id=1,
        closed=True,
        external_release=ExternalReleaseResource(
            id=1,
            release_id="release_id_example",
            description="description_example",
            name="name_example",
            archived=True,
            released=True,
            external_project=ExternalProjectResource(
                id=1,
                external_project_id="external_project_id_example",
                external_project_key="external_project_key_example",
                name="name_example",
            ),
            web_url="web_url_example",
        ),
        release_statistics=ReleaseStatisticsResource(
            id=1,
            release=ReleaseResource(ReleaseResource),
            total_passed=1,
            total_failed=1,
            total_execution=1,
        ),
    ) # ReleaseResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Release. Returns the Release details.
        api_response = api_instance.update8(release_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ReleaseApi->update8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_resource** | [**ReleaseResource**](ReleaseResource.md)|  |

### Return type

[**ReleaseResource**](ReleaseResource.md)

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

