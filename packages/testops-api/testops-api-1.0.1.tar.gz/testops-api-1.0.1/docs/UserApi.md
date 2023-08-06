# testops_api.UserApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_team**](UserApi.md#assign_user_team) | **POST** /api/v1/users/add | Adds users to a Team. Returns the added User detail.
[**change_avatar**](UserApi.md#change_avatar) | **POST** /api/v1/users/avatar | Change the avatar of the current User. Returns the updated User detail.
[**change_name**](UserApi.md#change_name) | **POST** /api/v1/users | Change name for current user.
[**create_or_update**](UserApi.md#create_or_update) | **POST** /api/v1/user-settings | Updates the User Settings detail. Returns the updated User Settings detail.
[**download_avatar**](UserApi.md#download_avatar) | **GET** /api/v1/users/avatar | Downloads the avatar of the current User. Returns the current avatar file.
[**get8**](UserApi.md#get8) | **GET** /api/v1/user-settings | Returns the User Settings detail.
[**get_me**](UserApi.md#get_me) | **GET** /api/v1/users/me | Returns the current User detail.
[**remove_user**](UserApi.md#remove_user) | **DELETE** /api/v1/users/remove | Removes a User from a Team. Returns the removed User detail.


# **assign_user_team**
> [UserResource] assign_user_team(team_id, new_user_ids)

Adds users to a Team. Returns the added User detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    team_id = 1 # int | 
    new_user_ids = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Adds users to a Team. Returns the added User detail.
        api_response = api_instance.assign_user_team(team_id, new_user_ids)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->assign_user_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  |
 **new_user_ids** | **[int]**|  |

### Return type

[**[UserResource]**](UserResource.md)

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

# **change_avatar**
> UserResource change_avatar(uploaded_path)

Change the avatar of the current User. Returns the updated User detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    uploaded_path = "uploadedPath_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Change the avatar of the current User. Returns the updated User detail.
        api_response = api_instance.change_avatar(uploaded_path)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->change_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_path** | **str**|  |

### Return type

[**UserResource**](UserResource.md)

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

# **change_name**
> UserResource change_name(first_name, last_name)

Change name for current user.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    first_name = "firstName_example" # str | 
    last_name = "lastName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Change name for current user.
        api_response = api_instance.change_name(first_name, last_name)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->change_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**|  |
 **last_name** | **str**|  |

### Return type

[**UserResource**](UserResource.md)

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

# **create_or_update**
> UserSettingResource create_or_update(user_setting_resource)

Updates the User Settings detail. Returns the updated User Settings detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_setting_resource import UserSettingResource
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
    api_instance = user_api.UserApi(api_client)
    user_setting_resource = UserSettingResource(
        mail_job_start=True,
        mail_job_end=True,
        mail_execution=True,
        mail_execution_status="mail_execution_status_example",
        mail_weekly_update=True,
    ) # UserSettingResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the User Settings detail. Returns the updated User Settings detail.
        api_response = api_instance.create_or_update(user_setting_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->create_or_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_setting_resource** | [**UserSettingResource**](UserSettingResource.md)|  |

### Return type

[**UserSettingResource**](UserSettingResource.md)

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

# **download_avatar**
> download_avatar()

Downloads the avatar of the current User. Returns the current avatar file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Downloads the avatar of the current User. Returns the current avatar file.
        api_instance.download_avatar()
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->download_avatar: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get8**
> UserSettingResource get8()

Returns the User Settings detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_setting_resource import UserSettingResource
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the User Settings detail.
        api_response = api_instance.get8()
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->get8: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSettingResource**](UserSettingResource.md)

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

# **get_me**
> UserResource get_me()

Returns the current User detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the current User detail.
        api_response = api_instance.get_me()
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResource**](UserResource.md)

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

# **remove_user**
> UserResource remove_user(team_id, user_id)

Removes a User from a Team. Returns the removed User detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import user_api
from testops_api.model.user_resource import UserResource
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
    api_instance = user_api.UserApi(api_client)
    team_id = 1 # int | 
    user_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Removes a User from a Team. Returns the removed User detail.
        api_response = api_instance.remove_user(team_id, user_id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling UserApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**|  |
 **user_id** | **int**|  |

### Return type

[**UserResource**](UserResource.md)

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

