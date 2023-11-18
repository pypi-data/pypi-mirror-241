# TaskSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_type** | **str** |  | [optional] 

## Example

```python
from snowflake.core.task._generated.models.task_schedule import TaskSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSchedule from a JSON string
task_schedule_instance = TaskSchedule.from_json(json)
# print the JSON string representation of the object
print TaskSchedule.to_json()

# convert the object into a dict
task_schedule_dict = task_schedule_instance.to_dict()
# create an instance of TaskSchedule from a dict
task_schedule_form_dict = task_schedule.from_dict(task_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


