# ExecutionTestResultResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**test_case** | [**TestCaseResource**](TestCaseResource.md) |  | [optional] 
**execution** | [**ExecutionResource**](ExecutionResource.md) |  | [optional] 
**platform** | [**PlatformResource**](PlatformResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**same_status_period** | **int** |  | [optional] 
**error_details_id** | **int** |  | [optional] 
**stdout_id** | **int** |  | [optional] 
**description_id** | **int** |  | [optional] 
**log_id** | **int** |  | [optional] 
**attachments** | [**[FileResource]**](FileResource.md) |  | [optional] 
**test_result_assertions_failed** | [**[TestResultAssertionFailedResource]**](TestResultAssertionFailedResource.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**duration** | **int** |  | [optional] 
**same_failure_results** | [**[ExecutionTestResultIdentifyResource]**](ExecutionTestResultIdentifyResource.md) |  | [optional] 
**test_suite** | [**TestSuiteResource**](TestSuiteResource.md) |  | [optional] 
**execution_test_suite** | [**ExecutionTestSuiteResource**](ExecutionTestSuiteResource.md) |  | [optional] 
**incidents** | [**[IncidentResource]**](IncidentResource.md) |  | [optional] 
**profile** | **str** |  | [optional] 
**has_comment** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_detail** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**external_issues** | [**[ExternalIssueResource]**](ExternalIssueResource.md) |  | [optional] 
**failed_test_result_category** | **str** |  | [optional] 
**total_test_object** | **int** |  | [optional] 
**total_defects** | **int** |  | [optional] 
**total_assertion** | **int** |  | [optional] 
**passed_assertion** | **int** |  | [optional] 
**failed_assertion** | **int** |  | [optional] 
**url_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


