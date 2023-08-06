# testops_api.ExecutionApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_download**](ExecutionApi.md#bulk_download) | **GET** /api/v1/executions/download | Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
[**delete2**](ExecutionApi.md#delete2) | **DELETE** /api/v1/executions | Deletes multiple Executions. Returns the deleted Execution details.
[**download1**](ExecutionApi.md#download1) | **GET** /api/v1/executions/{id}/download | Exports and downloads an Execution. Returns the Execution summary file.
[**download_file**](ExecutionApi.md#download_file) | **GET** /api/v1/executions/{id}/download-file | Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution&#39;s files.
[**get3**](ExecutionApi.md#get3) | **GET** /api/v1/executions/{id} | Returns an Execution detail.
[**get_latest_executions**](ExecutionApi.md#get_latest_executions) | **GET** /api/v1/organizations/{id}/latest-executions | 
[**link_release**](ExecutionApi.md#link_release) | **POST** /api/v1/executions/{id}/link-release | Link an Execution to a Release. Returns the updated Execution detail.
[**list**](ExecutionApi.md#list) | **GET** /api/v1/executions | 
[**re_import_execution**](ExecutionApi.md#re_import_execution) | **POST** /api/v1/executions/reimport | Re-imports an Execution. Returns the newly imported Execution detail.
[**rerun_execution**](ExecutionApi.md#rerun_execution) | **POST** /api/v1/executions/{id}/rerun | Rerun an Execution.
[**share_execution_report**](ExecutionApi.md#share_execution_report) | **POST** /api/v1/executions/{id}/share-report | Allow users to send email with attached execution reports [PDF].
[**terminated_execution**](ExecutionApi.md#terminated_execution) | **POST** /api/v1/executions/terminate | Terminates a running Execution. Returns the terminated Execution detail.
[**unlink_release**](ExecutionApi.md#unlink_release) | **POST** /api/v1/executions/{id}/unlink-release | Unlink an Execution to a Release. Returns the updated Execution detail.


# **bulk_download**
> bulk_download(id, project_id)

Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = [
        1,
    ] # [int] | 
    project_id = 1 # int | 
    file_type = "csv" # str |  (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
        api_instance.bulk_download(id, project_id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->bulk_download: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exports and downloads multiple Executions. Returns the archive file comprising the Execution summaries.
        api_instance.bulk_download(id, project_id, file_type=file_type)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->bulk_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **[int]**|  |
 **project_id** | **int**|  |
 **file_type** | **str**|  | [optional] if omitted the server will use the default value of "csv"

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

# **delete2**
> [ExecutionResource] delete2(project_id, order)

Deletes multiple Executions. Returns the deleted Execution details.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    project_id = 1 # int | 
    order = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes multiple Executions. Returns the deleted Execution details.
        api_response = api_instance.delete2(project_id, order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **order** | **[int]**|  |

### Return type

[**[ExecutionResource]**](ExecutionResource.md)

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

# **download1**
> download1(id)

Exports and downloads an Execution. Returns the Execution summary file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    file_type = "csv" # str |  (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # Exports and downloads an Execution. Returns the Execution summary file.
        api_instance.download1(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exports and downloads an Execution. Returns the Execution summary file.
        api_instance.download1(id, file_type=file_type)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **file_type** | **str**|  | [optional] if omitted the server will use the default value of "csv"

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

# **download_file**
> download_file(id)

Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution's files.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Downloads all uploaded files of an Execution. Returns the archive file comprising all Execution's files.
        api_instance.download_file(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->download_file: %s\n" % e)
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

# **get3**
> ExecutionResource get3(id)

Returns an Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an Execution detail.
        api_response = api_instance.get3(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **get_latest_executions**
> PageExecutionResource get_latest_executions(id, pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_execution_resource import PageExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    pageable = Pageable(
        sort=Sort(
            sorted=True,
            unsorted=True,
            empty=True,
        ),
        offset=1,
        page_size=1,
        page_number=1,
        paged=True,
        unpaged=True,
    ) # Pageable | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_latest_executions(id, pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->get_latest_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **pageable** | **Pageable**|  |

### Return type

[**PageExecutionResource**](PageExecutionResource.md)

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

# **link_release**
> ExecutionResource link_release(id, project_id, release_id)

Link an Execution to a Release. Returns the updated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    project_id = 1 # int | 
    release_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Link an Execution to a Release. Returns the updated Execution detail.
        api_response = api_instance.link_release(id, project_id, release_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->link_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **project_id** | **int**|  |
 **release_id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list(pageable)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.pageable import Pageable
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
    api_instance = execution_api.ExecutionApi(api_client)
    pageable = Pageable(
        sort=Sort(
            sorted=True,
            unsorted=True,
            empty=True,
        ),
        offset=1,
        page_size=1,
        page_number=1,
        paged=True,
        unpaged=True,
    ) # Pageable | 
    batch = "batch_example" # str |  (optional)
    project_id = 1 # int |  (optional)
    order = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list(pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list(pageable, batch=batch, project_id=project_id, order=order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | **Pageable**|  |
 **batch** | **str**|  | [optional]
 **project_id** | **int**|  | [optional]
 **order** | **int**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **re_import_execution**
> ExecutionResource re_import_execution(id)

Re-imports an Execution. Returns the newly imported Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Re-imports an Execution. Returns the newly imported Execution detail.
        api_response = api_instance.re_import_execution(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->re_import_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **rerun_execution**
> rerun_execution(id)

Rerun an Execution.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Rerun an Execution.
        api_instance.rerun_execution(id)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->rerun_execution: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_execution_report**
> share_execution_report(id, execution_share_report_resource)

Allow users to send email with attached execution reports [PDF].

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_share_report_resource import ExecutionShareReportResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 
    execution_share_report_resource = ExecutionShareReportResource(
        emails=[
            "emails_example",
        ],
        execution_id=1,
    ) # ExecutionShareReportResource | 

    # example passing only required values which don't have defaults set
    try:
        # Allow users to send email with attached execution reports [PDF].
        api_instance.share_execution_report(id, execution_share_report_resource)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->share_execution_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **execution_share_report_resource** | [**ExecutionShareReportResource**](ExecutionShareReportResource.md)|  |

### Return type

void (empty response body)

### Authorization

[basicScheme](../README.md#basicScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminated_execution**
> ExecutionResource terminated_execution(project_id, order)

Terminates a running Execution. Returns the terminated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    project_id = 1 # int | 
    order = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Terminates a running Execution. Returns the terminated Execution detail.
        api_response = api_instance.terminated_execution(project_id, order)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->terminated_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  |
 **order** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

# **unlink_release**
> ExecutionResource unlink_release(id)

Unlink an Execution to a Release. Returns the updated Execution detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import execution_api
from testops_api.model.execution_resource import ExecutionResource
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
    api_instance = execution_api.ExecutionApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Unlink an Execution to a Release. Returns the updated Execution detail.
        api_response = api_instance.unlink_release(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling ExecutionApi->unlink_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**ExecutionResource**](ExecutionResource.md)

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

