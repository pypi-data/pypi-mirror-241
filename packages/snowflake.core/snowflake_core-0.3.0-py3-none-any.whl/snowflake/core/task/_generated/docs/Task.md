# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**warehouse** | **str** |  | [optional] 
**schedule** | [**TaskSchedule**](TaskSchedule.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**config** | **Dict[str, object]** | Task Config | [optional] 
**session_parameters** | **Dict[str, object]** | Session Parameters for the task at runtime. | [optional] 
**definition** | **str** |  | 
**predecessors** | **List[str]** |  | [optional] 
**user_task_managed_initial_warehouse_size** | **str** |  | [optional] 
**user_task_timeout_ms** | **int** |  | [optional] 
**suspend_task_after_num_failures** | **int** |  | [optional] 
**condition** | **str** |  | [optional] 
**allow_overlapping_execution** | **bool** |  | [optional] 
**error_integration** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**owner_role_type** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**last_committed_on** | **datetime** |  | [optional] [readonly] 
**last_suspended_on** | **datetime** |  | [optional] [readonly] 
**database_name** | **str** |  | [optional] [readonly] 
**schema_name** | **str** |  | [optional] [readonly] 

## Example

```python
from snowflake.core.task._generated.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


