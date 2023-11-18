# TableObjectParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_rentention_time_in_days** | **int** |  | [optional] 
**max_data_extension_time_in_days** | **int** |  | [optional] 
**default_ddl_collation** | **str** |  | [optional] 

## Example

```python
from snowflake.core.table._generated.models.table_object_parameters import TableObjectParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TableObjectParameters from a JSON string
table_object_parameters_instance = TableObjectParameters.from_json(json)
# print the JSON string representation of the object
print TableObjectParameters.to_json()

# convert the object into a dict
table_object_parameters_dict = table_object_parameters_instance.to_dict()
# create an instance of TableObjectParameters from a dict
table_object_parameters_form_dict = table_object_parameters.from_dict(table_object_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


