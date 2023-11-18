# TaskRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_task_name** | **str** |  | [readonly] 
**database_name** | **str** |  | [readonly] 
**schema_name** | **str** |  | [readonly] 
**state** | **str** |  | [readonly] 
**first_error_task_name** | **str** |  | [optional] [readonly] 
**first_error_code** | **int** |  | [optional] [readonly] 
**first_error_message** | **str** |  | [optional] [readonly] 
**scheduled_time** | **datetime** |  | [readonly] 
**query_start_time** | **datetime** |  | [optional] [readonly] 
**next_scheduled_time** | **datetime** |  | [readonly] 
**completed_time** | **datetime** |  | [optional] [readonly] 
**root_task_id** | **str** |  | [readonly] 
**graph_version** | **int** |  | [readonly] 
**run_id** | **int** |  | [readonly] 

## Example

```python
from snowflake.core.task._generated.models.task_run import TaskRun

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRun from a JSON string
task_run_instance = TaskRun.from_json(json)
# print the JSON string representation of the object
print TaskRun.to_json()

# convert the object into a dict
task_run_dict = task_run_instance.to_dict()
# create an instance of TaskRun from a dict
task_run_form_dict = task_run.from_dict(task_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


