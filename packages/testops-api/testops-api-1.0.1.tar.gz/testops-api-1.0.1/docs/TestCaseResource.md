# TestCaseResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**previous_status** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**test_module_id** | **int** |  | [optional] 
**web_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project** | [**ProjectResource**](ProjectResource.md) |  | [optional] 
**last_execution_test_case** | [**ExecutionTestCaseResource**](ExecutionTestCaseResource.md) |  | [optional] 
**external_issues** | [**[ExternalIssueResource]**](ExternalIssueResource.md) |  | [optional] 
**type** | **str** |  | [optional] 
**average_duration** | **float** |  | [optional] 
**max_duration** | **int** |  | [optional] 
**min_duration** | **int** |  | [optional] 
**flakiness** | **float** |  | [optional] 
**platform_statistics** | [**{str: (TestCasePlatformStatisticsResource,)}**](TestCasePlatformStatisticsResource.md) |  | [optional] 
**maintainer** | [**UserResource**](UserResource.md) |  | [optional] 
**test_result_assertion** | [**TestResultAssertionResource**](TestResultAssertionResource.md) |  | [optional] 
**url_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


