# RunConfigurationResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**test_project_id** | **int** |  | [optional] 
**release_id** | **int** |  | [optional] 
**test_suite_collection_id** | **int** |  | [optional] 
**time_out** | **int** |  | [optional] 
**config_type** | **str** |  | [optional] 
**test_project** | [**TestProjectResource**](TestProjectResource.md) |  | [optional] 
**agents** | [**[AgentResource]**](AgentResource.md) |  | [optional] 
**k8s_agents** | [**[K8SAgentResource]**](K8SAgentResource.md) |  | [optional] 
**circle_ci_agents** | [**[CircleCIAgentResource]**](CircleCIAgentResource.md) |  | [optional] 
**cloud_type** | **str** |  | [optional] 
**latest_job** | [**JobResource**](JobResource.md) |  | [optional] 
**generic_command** | **str** |  | [optional] 
**ks_version** | **str** |  | [optional] 
**ks_location** | **str** |  | [optional] 
**next_run_scheduler** | [**SchedulerResource**](SchedulerResource.md) |  | [optional] 
**release** | [**ReleaseResource**](ReleaseResource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


