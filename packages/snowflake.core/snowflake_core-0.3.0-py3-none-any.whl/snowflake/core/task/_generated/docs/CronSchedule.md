# CronSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expr** | **str** |  | 
**timezone** | **str** |  | 

## Example

```python
from snowflake.core.task._generated.models.cron_schedule import CronSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CronSchedule from a JSON string
cron_schedule_instance = CronSchedule.from_json(json)
# print the JSON string representation of the object
print CronSchedule.to_json()

# convert the object into a dict
cron_schedule_dict = cron_schedule_instance.to_dict()
# create an instance of CronSchedule from a dict
cron_schedule_form_dict = cron_schedule.from_dict(cron_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


