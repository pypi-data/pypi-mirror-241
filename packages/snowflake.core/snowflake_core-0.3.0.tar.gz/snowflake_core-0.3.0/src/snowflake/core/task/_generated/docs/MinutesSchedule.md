# MinutesSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | **int** |  | 

## Example

```python
from snowflake.core.task._generated.models.minutes_schedule import MinutesSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of MinutesSchedule from a JSON string
minutes_schedule_instance = MinutesSchedule.from_json(json)
# print the JSON string representation of the object
print MinutesSchedule.to_json()

# convert the object into a dict
minutes_schedule_dict = minutes_schedule_instance.to_dict()
# create an instance of MinutesSchedule from a dict
minutes_schedule_form_dict = minutes_schedule.from_dict(minutes_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


