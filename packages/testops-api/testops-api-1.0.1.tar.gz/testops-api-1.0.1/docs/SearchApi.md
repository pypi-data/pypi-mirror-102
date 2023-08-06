# testops_api.SearchApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /api/v1/search | Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.
[**search1**](SearchApi.md#search1) | **POST** /api/v1/search | Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.
[**test**](SearchApi.md#test) | **GET** /api/v1/search/info | Returns the search configuration.


# **search**
> PageBaseResource search(q)

Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import search_api
from testops_api.model.page_base_resource import PageBaseResource
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
    api_instance = search_api.SearchApi(api_client)
    q = "q_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.
        api_response = api_instance.search(q)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  |

### Return type

[**PageBaseResource**](PageBaseResource.md)

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

# **search1**
> PageBaseResource search1(search_request)

Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import search_api
from testops_api.model.search_request import SearchRequest
from testops_api.model.page_base_resource import PageBaseResource
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
    api_instance = search_api.SearchApi(api_client)
    search_request = SearchRequest(
        search_request_conditions=[
            SearchRequestCondition(
                key="key_example",
                operator="operator_example",
                value={},
            ),
        ],
        search_request_pagination=SearchRequestPagination(
            page=1,
            size=1,
            sorts=[
                SearchRequestSortOrder(
                    name="name_example",
                    order="order_example",
                ),
            ],
        ),
        search_request_group_bys=[
            "search_request_group_bys_example",
        ],
        search_request_functions=[
            SearchRequestFunction(
                key="key_example",
                function_name="function_name_example",
                parameters=[
                    "parameters_example",
                ],
                time_zone="time_zone_example",
            ),
        ],
        type="type_example",
        search_entity="Execution",
        time_zone="time_zone_example",
    ) # SearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Queries the resources of a specific type by multiple conditions. Returns the pageable resources satisfying the query.
        api_response = api_instance.search1(search_request)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling SearchApi->search1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  |

### Return type

[**PageBaseResource**](PageBaseResource.md)

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

# **test**
> {str: (SearchConfigResource,)} test()

Returns the search configuration.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import search_api
from testops_api.model.search_config_resource import SearchConfigResource
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
    api_instance = search_api.SearchApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the search configuration.
        api_response = api_instance.test()
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling SearchApi->test: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**{str: (SearchConfigResource,)}**](SearchConfigResource.md)

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

