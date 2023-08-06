# testops_api.AgentApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](AgentApi.md#create1) | **POST** /api/v1/circle-ci-agent | Creates a new CircleCI agent. Returns the created agent detail.
[**create5**](AgentApi.md#create5) | **POST** /api/v1/k8s-agent | Creates a K8S agent. Returns the created agent detail.
[**create6**](AgentApi.md#create6) | **POST** /api/v1/agent | Creates or updates a Local agent. Returns the agent detail.
[**delete7**](AgentApi.md#delete7) | **DELETE** /api/v1/agent/{id} | Deletes a Local agent. Returns the deleted agent detail.
[**generate_agent**](AgentApi.md#generate_agent) | **GET** /api/v1/agent | Generates the configuration file for the Local agent. Returns the configuration file.
[**get12**](AgentApi.md#get12) | **GET** /api/v1/k8s-agent/{id} | Returns a K8S agent detail.
[**get15**](AgentApi.md#get15) | **GET** /api/v1/agent/{id} | Get a Local agent. Returns the agent detail.
[**get2**](AgentApi.md#get2) | **GET** /api/v1/circle-ci-agent/{id} | Returns a CircleCI agent detail.
[**get_followed_projects**](AgentApi.md#get_followed_projects) | **POST** /api/v1/circle-ci-agent/projects | 
[**update2**](AgentApi.md#update2) | **PUT** /api/v1/circle-ci-agent | Updates a CircleCI agent detail. Returns the updated agent detail.
[**update9**](AgentApi.md#update9) | **PUT** /api/v1/k8s-agent | Updates a K8S agent detail. Returns the updated agent detail.
[**update_threshold**](AgentApi.md#update_threshold) | **PUT** /api/v1/agent/threshold | Updates the threshold for Local agent. Returns the agent detail.


# **create1**
> CircleCIAgentResource create1(circle_ci_agent_resource)

Creates a new CircleCI agent. Returns the created agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.circle_ci_agent_resource import CircleCIAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    circle_ci_agent_resource = CircleCIAgentResource(
        id=1,
        name="name_example",
        url="url_example",
        username="username_example",
        token="token_example",
        project="project_example",
        vcs_type="vcs_type_example",
        branch="branch_example",
        team_id=1,
        api_key="api_key_example",
    ) # CircleCIAgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new CircleCI agent. Returns the created agent detail.
        api_response = api_instance.create1(circle_ci_agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->create1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circle_ci_agent_resource** | [**CircleCIAgentResource**](CircleCIAgentResource.md)|  |

### Return type

[**CircleCIAgentResource**](CircleCIAgentResource.md)

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

# **create5**
> K8SAgentResource create5(k8_s_agent_resource)

Creates a K8S agent. Returns the created agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.k8_s_agent_resource import K8SAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    k8_s_agent_resource = K8SAgentResource(
        id=1,
        name="name_example",
        certificate_authority="certificate_authority_example",
        url="url_example",
        namespace="namespace_example",
        username="username_example",
        password="password_example",
        token="token_example",
        cluster="cluster_example",
        region="region_example",
        access_key="access_key_example",
        private_access_key="private_access_key_example",
        team_id=1,
        api_key="api_key_example",
        authentication_type="BASIC_AUTH",
    ) # K8SAgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a K8S agent. Returns the created agent detail.
        api_response = api_instance.create5(k8_s_agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->create5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8_s_agent_resource** | [**K8SAgentResource**](K8SAgentResource.md)|  |

### Return type

[**K8SAgentResource**](K8SAgentResource.md)

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

# **create6**
> AgentResource create6(agent_resource)

Creates or updates a Local agent. Returns the agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.agent_resource import AgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    agent_resource = AgentResource(
        id=1,
        name="name_example",
        ip="ip_example",
        uuid="uuid_example",
        last_ping=dateutil_parser('1970-01-01T00:00:00.00Z'),
        os="os_example",
        team_id=1,
        hostname="hostname_example",
        active=True,
        threshold=1,
        num_executing_jobs=1,
        num_assigned_jobs=1,
        agent_version="agent_version_example",
        deleted=True,
    ) # AgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates or updates a Local agent. Returns the agent detail.
        api_response = api_instance.create6(agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->create6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_resource** | [**AgentResource**](AgentResource.md)|  |

### Return type

[**AgentResource**](AgentResource.md)

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

# **delete7**
> AgentResource delete7(id)

Deletes a Local agent. Returns the deleted agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.agent_resource import AgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Local agent. Returns the deleted agent detail.
        api_response = api_instance.delete7(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->delete7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**AgentResource**](AgentResource.md)

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

# **generate_agent**
> generate_agent(agent_config_resource)

Generates the configuration file for the Local agent. Returns the configuration file.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.agent_config_resource import AgentConfigResource
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
    api_instance = agent_api.AgentApi(api_client)
    agent_config_resource = AgentConfigResource(
        team_id="team_id_example",
        agent_name="agent_name_example",
        api_key="api_key_example",
        os="os_example",
        email="email_example",
    ) # AgentConfigResource | 

    # example passing only required values which don't have defaults set
    try:
        # Generates the configuration file for the Local agent. Returns the configuration file.
        api_instance.generate_agent(agent_config_resource)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->generate_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_config_resource** | **AgentConfigResource**|  |

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

# **get12**
> K8SAgentResource get12(id)

Returns a K8S agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.k8_s_agent_resource import K8SAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a K8S agent detail.
        api_response = api_instance.get12(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->get12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**K8SAgentResource**](K8SAgentResource.md)

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

# **get15**
> AgentResource get15(id)

Get a Local agent. Returns the agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.agent_resource import AgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get a Local agent. Returns the agent detail.
        api_response = api_instance.get15(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->get15: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**AgentResource**](AgentResource.md)

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

# **get2**
> CircleCIAgentResource get2(id)

Returns a CircleCI agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.circle_ci_agent_resource import CircleCIAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a CircleCI agent detail.
        api_response = api_instance.get2(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**CircleCIAgentResource**](CircleCIAgentResource.md)

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

# **get_followed_projects**
> [CircleCIProject] get_followed_projects(circle_ci_connection_resource)



### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.circle_ci_connection_resource import CircleCIConnectionResource
from testops_api.model.circle_ci_project import CircleCIProject
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
    api_instance = agent_api.AgentApi(api_client)
    circle_ci_connection_resource = CircleCIConnectionResource(
        url="url_example",
        username="username_example",
        token="token_example",
        project="project_example",
        vcs_type="vcs_type_example",
        branch="branch_example",
    ) # CircleCIConnectionResource | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_followed_projects(circle_ci_connection_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->get_followed_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circle_ci_connection_resource** | [**CircleCIConnectionResource**](CircleCIConnectionResource.md)|  |

### Return type

[**[CircleCIProject]**](CircleCIProject.md)

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

# **update2**
> CircleCIAgentResource update2(circle_ci_agent_resource)

Updates a CircleCI agent detail. Returns the updated agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.circle_ci_agent_resource import CircleCIAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    circle_ci_agent_resource = CircleCIAgentResource(
        id=1,
        name="name_example",
        url="url_example",
        username="username_example",
        token="token_example",
        project="project_example",
        vcs_type="vcs_type_example",
        branch="branch_example",
        team_id=1,
        api_key="api_key_example",
    ) # CircleCIAgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a CircleCI agent detail. Returns the updated agent detail.
        api_response = api_instance.update2(circle_ci_agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circle_ci_agent_resource** | [**CircleCIAgentResource**](CircleCIAgentResource.md)|  |

### Return type

[**CircleCIAgentResource**](CircleCIAgentResource.md)

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

# **update9**
> K8SAgentResource update9(k8_s_agent_resource)

Updates a K8S agent detail. Returns the updated agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.k8_s_agent_resource import K8SAgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    k8_s_agent_resource = K8SAgentResource(
        id=1,
        name="name_example",
        certificate_authority="certificate_authority_example",
        url="url_example",
        namespace="namespace_example",
        username="username_example",
        password="password_example",
        token="token_example",
        cluster="cluster_example",
        region="region_example",
        access_key="access_key_example",
        private_access_key="private_access_key_example",
        team_id=1,
        api_key="api_key_example",
        authentication_type="BASIC_AUTH",
    ) # K8SAgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a K8S agent detail. Returns the updated agent detail.
        api_response = api_instance.update9(k8_s_agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->update9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8_s_agent_resource** | [**K8SAgentResource**](K8SAgentResource.md)|  |

### Return type

[**K8SAgentResource**](K8SAgentResource.md)

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

# **update_threshold**
> AgentResource update_threshold(agent_resource)

Updates the threshold for Local agent. Returns the agent detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import agent_api
from testops_api.model.agent_resource import AgentResource
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
    api_instance = agent_api.AgentApi(api_client)
    agent_resource = AgentResource(
        id=1,
        name="name_example",
        ip="ip_example",
        uuid="uuid_example",
        last_ping=dateutil_parser('1970-01-01T00:00:00.00Z'),
        os="os_example",
        team_id=1,
        hostname="hostname_example",
        active=True,
        threshold=1,
        num_executing_jobs=1,
        num_assigned_jobs=1,
        agent_version="agent_version_example",
        deleted=True,
    ) # AgentResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the threshold for Local agent. Returns the agent detail.
        api_response = api_instance.update_threshold(agent_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling AgentApi->update_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_resource** | [**AgentResource**](AgentResource.md)|  |

### Return type

[**AgentResource**](AgentResource.md)

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

