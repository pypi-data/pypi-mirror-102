# testops_api.OrganizationTrialRequestResourceControllerApi

All URIs are relative to *https://testops.katalon.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trial_request**](OrganizationTrialRequestResourceControllerApi.md#get_trial_request) | **GET** /api/v1/organizations/{id}/trial-request | Get organization trial request data
[**submit_trial_request**](OrganizationTrialRequestResourceControllerApi.md#submit_trial_request) | **POST** /api/v1/organizations/{id}/trial-request | Submit organization trial request


# **get_trial_request**
> OrganizationTrialRequestResource get_trial_request(id)

Get organization trial request data

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import organization_trial_request_resource_controller_api
from testops_api.model.organization_trial_request_resource import OrganizationTrialRequestResource
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
    api_instance = organization_trial_request_resource_controller_api.OrganizationTrialRequestResourceControllerApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get organization trial request data
        api_response = api_instance.get_trial_request(id)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling OrganizationTrialRequestResourceControllerApi->get_trial_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**OrganizationTrialRequestResource**](OrganizationTrialRequestResource.md)

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

# **submit_trial_request**
> OrganizationTrialRequestResource submit_trial_request(id, organization_trial_request_resource)

Submit organization trial request

### Example

* Basic Authentication (basicScheme):
```python
import time
import testops_api
from testops_api.api import organization_trial_request_resource_controller_api
from testops_api.model.organization_trial_request_resource import OrganizationTrialRequestResource
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
    api_instance = organization_trial_request_resource_controller_api.OrganizationTrialRequestResourceControllerApi(api_client)
    id = 1 # int | 
    organization_trial_request_resource = OrganizationTrialRequestResource(
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
        user_request=UserResource(
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
                    team=TeamResource(
                        id=1,
                        name="name_example",
                        role="OWNER",
                        users=[
                            UserResource(UserResource),
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
                    ),
                    timezone="timezone_example",
                    status="ARCHIVE",
                ),
            ],
            teams=[
                TeamResource(
                    id=1,
                    name="name_example",
                    role="OWNER",
                    users=[],
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
                ),
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
        status="PENDING",
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        form_request="form_request_example",
    ) # OrganizationTrialRequestResource | 

    # example passing only required values which don't have defaults set
    try:
        # Submit organization trial request
        api_response = api_instance.submit_trial_request(id, organization_trial_request_resource)
        pprint(api_response)
    except testops_api.ApiException as e:
        print("Exception when calling OrganizationTrialRequestResourceControllerApi->submit_trial_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **organization_trial_request_resource** | [**OrganizationTrialRequestResource**](OrganizationTrialRequestResource.md)|  |

### Return type

[**OrganizationTrialRequestResource**](OrganizationTrialRequestResource.md)

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

