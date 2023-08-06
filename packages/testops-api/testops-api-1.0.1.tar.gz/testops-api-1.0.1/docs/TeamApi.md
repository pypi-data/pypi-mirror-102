# testops_api.TeamApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](TeamApi.md#create3) | **POST** /api/v1/teams | Creates a new Team. Returns the created Team detail.
[**delete3**](TeamApi.md#delete3) | **DELETE** /api/v1/teams/{id} | Delete a Team. Returns the delete Team detail.
[**get4**](TeamApi.md#get4) | **GET** /api/v1/teams/{id} | Returns a Team detail.
[**list1**](TeamApi.md#list1) | **GET** /api/v1/teams | Returns all Teams of the current User.
[**update4**](TeamApi.md#update4) | **PUT** /api/v1/teams | Updates a Team detail. Returns the updated Team detail.
[**update_user_team**](TeamApi.md#update_user_team) | **PUT** /api/v1/permission/team/user | Updates the role of a User in a Team. Returns the updated detail.


# **create3**
> TeamResource create3(team_resource)

Creates a new Team. Returns the created Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    team_resource = TeamResource(
        id=1,
        name="name_example",
        role="OWNER",
        users=[
            UserResource(
                id=1,
                email="email_example",
                first_name="first_name_example",
                last_name="last_name_example",
                password="password_example",
                inviting_url="inviting_url_example",
                avatar="avatar_example",
                configs=ConfigResource(
                    web_socket_url="web_socket_url_example",
                    store_url="store_url_example",
                    profiles=[
                        "profiles_example",
                    ],
                    stripe_public_api="stripe_public_api_example",
                    build_version="build_version_example",
                    commit_id="commit_id_example",
                    sentry_dsn="sentry_dsn_example",
                    sentry_env="sentry_env_example",
                    server_url="server_url_example",
                    io_server_url="io_server_url_example",
                    max_execution_comparison=1,
                    max_execution_download=1,
                    agent_download_urls={
                        "key": "key_example",
                    },
                    report_uploader_download_url="report_uploader_download_url_example",
                    report_uploader_latest_version="report_uploader_latest_version_example",
                    sub_domain_pattern="sub_domain_pattern_example",
                    cancellation_survey_url="cancellation_survey_url_example",
                    advanced_feature_enabled=True,
                    using_sub_domain=True,
                    frameworks_integration_enabled=True,
                ),
                projects=[
                    ProjectResource(
                        id=1,
                        name="name_example",
                        team_id=1,
                        team=TeamResource(TeamResource),
                        timezone="timezone_example",
                        status="ARCHIVE",
                    ),
                ],
                teams=[
                    TeamResource(TeamResource),
                ],
                organizations=[
                    OrganizationResource(
                        id=1,
                        name="name_example",
                        role="OWNER",
                        org_feature_flag=OrganizationFeatureFlagResource(
                            organization_id=1,
                            sub_domain=True,
                            strict_domain=True,
                            sso=True,
                            circle_ci=True,
                        ),
                        quota_kse=1,
                        machine_quota_kse=1,
                        quota_engine=1,
                        machine_quota_engine=1,
                        used_kse=1,
                        used_engine=1,
                        quota_test_ops=1,
                        used_test_ops=1,
                        number_user=1,
                        quota_floating_engine=1,
                        used_floating_engine=1,
                        can_create_offline_kse=True,
                        can_create_offline_re=True,
                        subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscribed=True,
                        kse_paygo=True,
                        kre_paygo=True,
                        paygo_quota=1,
                        domain="domain_example",
                        subdomain_url="subdomain_url_example",
                        strict_domain=True,
                        logo_url="logo_url_example",
                        saml_sso=True,
                        kre_license=True,
                        test_ops_package="BASIC",
                        most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ],
                organization_feature=[
                    UserOrganizationFeatureResource(
                        user=UserResource(UserResource),
                        user_id=1,
                        organization_id=1,
                        user_email="user_email_example",
                        organization=OrganizationResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            org_feature_flag=OrganizationFeatureFlagResource(
                                organization_id=1,
                                sub_domain=True,
                                strict_domain=True,
                                sso=True,
                                circle_ci=True,
                            ),
                            quota_kse=1,
                            machine_quota_kse=1,
                            quota_engine=1,
                            machine_quota_engine=1,
                            used_kse=1,
                            used_engine=1,
                            quota_test_ops=1,
                            used_test_ops=1,
                            number_user=1,
                            quota_floating_engine=1,
                            used_floating_engine=1,
                            can_create_offline_kse=True,
                            can_create_offline_re=True,
                            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscribed=True,
                            kse_paygo=True,
                            kre_paygo=True,
                            paygo_quota=1,
                            domain="domain_example",
                            subdomain_url="subdomain_url_example",
                            strict_domain=True,
                            logo_url="logo_url_example",
                            saml_sso=True,
                            kre_license=True,
                            test_ops_package="BASIC",
                            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                        feature="KSE",
                    ),
                ],
                trial_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                system_role="USER",
                business_user=True,
                can_create_offline_kse=True,
                can_create_offline_re=True,
                saml_sso=True,
                full_name="full_name_example",
            ),
        ],
        organization=OrganizationResource(
            id=1,
            name="name_example",
            role="OWNER",
            org_feature_flag=OrganizationFeatureFlagResource(
                organization_id=1,
                sub_domain=True,
                strict_domain=True,
                sso=True,
                circle_ci=True,
            ),
            quota_kse=1,
            machine_quota_kse=1,
            quota_engine=1,
            machine_quota_engine=1,
            used_kse=1,
            used_engine=1,
            quota_test_ops=1,
            used_test_ops=1,
            number_user=1,
            quota_floating_engine=1,
            used_floating_engine=1,
            can_create_offline_kse=True,
            can_create_offline_re=True,
            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscribed=True,
            kse_paygo=True,
            kre_paygo=True,
            paygo_quota=1,
            domain="domain_example",
            subdomain_url="subdomain_url_example",
            strict_domain=True,
            logo_url="logo_url_example",
            saml_sso=True,
            kre_license=True,
            test_ops_package="BASIC",
            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        organization_id=1,
    ) # TeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Team. Returns the created Team detail.
        api_response = api_instance.create3(team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->create3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_resource** | [**TeamResource**](TeamResource.md)|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **delete3**
> TeamResource delete3(id)

Delete a Team. Returns the delete Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Team. Returns the delete Team detail.
        api_response = api_instance.delete3(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **get4**
> TeamResource get4(id)

Returns a Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a Team detail.
        api_response = api_instance.get4(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **list1**
> PageTeamResource list1(pageable)

Returns all Teams of the current User.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.pageable import Pageable
from testops_api.model.page_team_resource import PageTeamResource
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
    api_instance = team_api.TeamApi(api_client)
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
        # Returns all Teams of the current User.
        api_response = api_instance.list1(pageable)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | **Pageable**|  |

### Return type

[**PageTeamResource**](PageTeamResource.md)

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

# **update4**
> TeamResource update4(team_resource)

Updates a Team detail. Returns the updated Team detail.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.team_resource import TeamResource
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
    api_instance = team_api.TeamApi(api_client)
    team_resource = TeamResource(
        id=1,
        name="name_example",
        role="OWNER",
        users=[
            UserResource(
                id=1,
                email="email_example",
                first_name="first_name_example",
                last_name="last_name_example",
                password="password_example",
                inviting_url="inviting_url_example",
                avatar="avatar_example",
                configs=ConfigResource(
                    web_socket_url="web_socket_url_example",
                    store_url="store_url_example",
                    profiles=[
                        "profiles_example",
                    ],
                    stripe_public_api="stripe_public_api_example",
                    build_version="build_version_example",
                    commit_id="commit_id_example",
                    sentry_dsn="sentry_dsn_example",
                    sentry_env="sentry_env_example",
                    server_url="server_url_example",
                    io_server_url="io_server_url_example",
                    max_execution_comparison=1,
                    max_execution_download=1,
                    agent_download_urls={
                        "key": "key_example",
                    },
                    report_uploader_download_url="report_uploader_download_url_example",
                    report_uploader_latest_version="report_uploader_latest_version_example",
                    sub_domain_pattern="sub_domain_pattern_example",
                    cancellation_survey_url="cancellation_survey_url_example",
                    advanced_feature_enabled=True,
                    using_sub_domain=True,
                    frameworks_integration_enabled=True,
                ),
                projects=[
                    ProjectResource(
                        id=1,
                        name="name_example",
                        team_id=1,
                        team=TeamResource(TeamResource),
                        timezone="timezone_example",
                        status="ARCHIVE",
                    ),
                ],
                teams=[
                    TeamResource(TeamResource),
                ],
                organizations=[
                    OrganizationResource(
                        id=1,
                        name="name_example",
                        role="OWNER",
                        org_feature_flag=OrganizationFeatureFlagResource(
                            organization_id=1,
                            sub_domain=True,
                            strict_domain=True,
                            sso=True,
                            circle_ci=True,
                        ),
                        quota_kse=1,
                        machine_quota_kse=1,
                        quota_engine=1,
                        machine_quota_engine=1,
                        used_kse=1,
                        used_engine=1,
                        quota_test_ops=1,
                        used_test_ops=1,
                        number_user=1,
                        quota_floating_engine=1,
                        used_floating_engine=1,
                        can_create_offline_kse=True,
                        can_create_offline_re=True,
                        subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        subscribed=True,
                        kse_paygo=True,
                        kre_paygo=True,
                        paygo_quota=1,
                        domain="domain_example",
                        subdomain_url="subdomain_url_example",
                        strict_domain=True,
                        logo_url="logo_url_example",
                        saml_sso=True,
                        kre_license=True,
                        test_ops_package="BASIC",
                        most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ],
                organization_feature=[
                    UserOrganizationFeatureResource(
                        user=UserResource(UserResource),
                        user_id=1,
                        organization_id=1,
                        user_email="user_email_example",
                        organization=OrganizationResource(
                            id=1,
                            name="name_example",
                            role="OWNER",
                            org_feature_flag=OrganizationFeatureFlagResource(
                                organization_id=1,
                                sub_domain=True,
                                strict_domain=True,
                                sso=True,
                                circle_ci=True,
                            ),
                            quota_kse=1,
                            machine_quota_kse=1,
                            quota_engine=1,
                            machine_quota_engine=1,
                            used_kse=1,
                            used_engine=1,
                            quota_test_ops=1,
                            used_test_ops=1,
                            number_user=1,
                            quota_floating_engine=1,
                            used_floating_engine=1,
                            can_create_offline_kse=True,
                            can_create_offline_re=True,
                            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            subscribed=True,
                            kse_paygo=True,
                            kre_paygo=True,
                            paygo_quota=1,
                            domain="domain_example",
                            subdomain_url="subdomain_url_example",
                            strict_domain=True,
                            logo_url="logo_url_example",
                            saml_sso=True,
                            kre_license=True,
                            test_ops_package="BASIC",
                            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
                        feature="KSE",
                    ),
                ],
                trial_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                system_role="USER",
                business_user=True,
                can_create_offline_kse=True,
                can_create_offline_re=True,
                saml_sso=True,
                full_name="full_name_example",
            ),
        ],
        organization=OrganizationResource(
            id=1,
            name="name_example",
            role="OWNER",
            org_feature_flag=OrganizationFeatureFlagResource(
                organization_id=1,
                sub_domain=True,
                strict_domain=True,
                sso=True,
                circle_ci=True,
            ),
            quota_kse=1,
            machine_quota_kse=1,
            quota_engine=1,
            machine_quota_engine=1,
            used_kse=1,
            used_engine=1,
            quota_test_ops=1,
            used_test_ops=1,
            number_user=1,
            quota_floating_engine=1,
            used_floating_engine=1,
            can_create_offline_kse=True,
            can_create_offline_re=True,
            subscription_expiry_date_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_kse=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_floating_engine=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscription_expiry_date_test_ops=dateutil_parser('1970-01-01T00:00:00.00Z'),
            subscribed=True,
            kse_paygo=True,
            kre_paygo=True,
            paygo_quota=1,
            domain="domain_example",
            subdomain_url="subdomain_url_example",
            strict_domain=True,
            logo_url="logo_url_example",
            saml_sso=True,
            kre_license=True,
            test_ops_package="BASIC",
            most_recent_project_accessed_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        organization_id=1,
    ) # TeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a Team detail. Returns the updated Team detail.
        api_response = api_instance.update4(team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->update4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_resource** | [**TeamResource**](TeamResource.md)|  |

### Return type

[**TeamResource**](TeamResource.md)

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

# **update_user_team**
> UserTeamResource update_user_team(user_team_resource)

Updates the role of a User in a Team. Returns the updated detail.

The user issuing this request must be the Admin of the team.

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import team_api
from testops_api.model.user_team_resource import UserTeamResource
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
    api_instance = team_api.TeamApi(api_client)
    user_team_resource = UserTeamResource(
        id=1,
        user_id=1,
        team_id=1,
        role="OWNER",
    ) # UserTeamResource | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the role of a User in a Team. Returns the updated detail.
        api_response = api_instance.update_user_team(user_team_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling TeamApi->update_user_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_team_resource** | [**UserTeamResource**](UserTeamResource.md)|  |

### Return type

[**UserTeamResource**](UserTeamResource.md)

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

