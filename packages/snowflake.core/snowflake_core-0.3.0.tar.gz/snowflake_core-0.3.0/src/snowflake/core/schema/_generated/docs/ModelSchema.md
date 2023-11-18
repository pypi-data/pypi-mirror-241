# ModelSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**is_default** | **bool** |  | [optional] [readonly] 
**is_current** | **bool** |  | [optional] [readonly] 
**database_name** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**comment** | **str** |  | [optional] 
**options** | **str** |  | [optional] [readonly] 
**dropped_on** | **datetime** |  | [optional] [readonly] 
**owner_role_type** | **str** |  | [optional] [readonly] 
**data_retention_time_in_days** | **int** |  | [optional] 
**default_ddl_collation** | **str** |  | [optional] 
**log_level** | **str** | Specifies the severity level of messages that should be ingested and made available in the active event table. At the time of writing the supported values are TRACE, DEBUG, INFO, WARN, ERROR, FATAL and OFF. | [optional] 
**pipe_execution_paused** | **bool** |  | [optional] 
**max_data_extension_time_in_days** | **int** |  | [optional] 
**suspend_task_after_num_failures** | **int** |  | [optional] 
**trace_level** | **str** | Controls how trace events are ingested into the event table. At the time of writing the supported values are ALWAYS, ON_EVENT and OFF. | [optional] 
**user_task_managed_initial_warehouse_size** | **str** |  | [optional] 
**user_task_timeout_ms** | **int** |  | [optional] 

## Example

```python
from snowflake.core.schema._generated.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print ModelSchema.to_json()

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_form_dict = model_schema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


