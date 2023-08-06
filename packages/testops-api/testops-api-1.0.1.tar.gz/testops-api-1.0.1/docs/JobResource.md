# JobResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**build_number** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**stop_time** | **datetime** |  | [optional] 
**test_project** | [**TestProjectResource**](TestProjectResource.md) |  | [optional] 
**execution** | [**ExecutionResource**](ExecutionResource.md) |  | [optional] 
**agent** | [**AgentResource**](AgentResource.md) |  | [optional] 
**k8s_agent** | [**K8SAgentResource**](K8SAgentResource.md) |  | [optional] 
**circle_ci_agent** | [**CircleCIAgentResource**](CircleCIAgentResource.md) |  | [optional] 
**run_configuration** | [**RunConfigurationResource**](RunConfigurationResource.md) |  | [optional] 
**order** | **int** |  | [optional] 
**parameter** | [**TriggerBuildParameter**](TriggerBuildParameter.md) |  | [optional] 
**trigger_by** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**trigger_at** | **datetime** |  | [optional] 
**user** | [**UserResource**](UserResource.md) |  | [optional] 
**scheduler** | [**SchedulerResource**](SchedulerResource.md) |  | [optional] 
**project** | [**ProjectResource**](ProjectResource.md) |  | [optional] 
**process_id** | **int** |  | [optional] 
**node_status** | **str** |  | [optional] 
**run_configuration_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


