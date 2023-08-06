# testops_api.CommentApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](CommentApi.md#create2) | **POST** /api/v1/comments | Creates a Comment. Returns the created Comment detail.
[**update3**](CommentApi.md#update3) | **PUT** /api/v1/comments | Updates a Comment detail. Returns the updated Comment detail.


# **create2**
> CommentResource create2(comment_resource)

Creates a Comment. Returns the created Comment detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import comment_api
from testops_api.model.comment_resource import CommentResource
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
    api_instance = comment_api.CommentApi(api_client)
    comment_resource = CommentResource(
        id=1,
        object_id=1,
        project_id=1,
        content="content_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        team_id=1,
        object_type="EXECUTION_TEST_SUITE",
        email="email_example",
        display_name="display_name_example",
        display_avatar="display_avatar_example",
        by_system=True,
    ) # CommentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a Comment. Returns the created Comment detail.
        api_response = api_instance.create2(comment_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling CommentApi->create2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_resource** | [**CommentResource**](CommentResource.md)|  |

### Return type

[**CommentResource**](CommentResource.md)

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

# **update3**
> CommentResource update3(comment_resource)

Updates a Comment detail. Returns the updated Comment detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import comment_api
from testops_api.model.comment_resource import CommentResource
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
    api_instance = comment_api.CommentApi(api_client)
    comment_resource = CommentResource(
        id=1,
        object_id=1,
        project_id=1,
        content="content_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        team_id=1,
        object_type="EXECUTION_TEST_SUITE",
        email="email_example",
        display_name="display_name_example",
        display_avatar="display_avatar_example",
        by_system=True,
    ) # CommentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Comment detail. Returns the updated Comment detail.
        api_response = api_instance.update3(comment_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling CommentApi->update3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_resource** | [**CommentResource**](CommentResource.md)|  |

### Return type

[**CommentResource**](CommentResource.md)

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

