# Table


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | **str** |  | [optional] 
**cluster_by** | **List[str]** |  | [optional] 
**enable_schema_evolution** | **bool** |  | [optional] 
**change_tracking** | **bool** |  | [optional] 
**data_retention_time_in_days** | **int** |  | [optional] 
**max_data_extension_time_in_days** | **int** |  | [optional] 
**default_ddl_collation** | **str** |  | [optional] 
**columns** | [**List[TableColumn]**](TableColumn.md) |  | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**database_name** | **str** |  | [optional] 
**schema_name** | **str** |  | [optional] 
**rows** | **int** |  | [optional] 
**bytes** | **int** |  | [optional] 
**owner** | **str** |  | [optional] 
**dropped_on** | **datetime** |  | [optional] 
**automatic_clustering** | **bool** |  | [optional] 
**search_optimization** | **bool** |  | [optional] 
**search_optimization_progress** | **float** |  | [optional] 
**search_optimization_bytes** | **int** |  | [optional] 
**owner_role_type** | **str** |  | [optional] 

## Example

```python
from snowflake.core.table._generated.models.table import Table

# TODO update the JSON string below
json = "{}"
# create an instance of Table from a JSON string
table_instance = Table.from_json(json)
# print the JSON string representation of the object
print Table.to_json()

# convert the object into a dict
table_dict = table_instance.to_dict()
# create an instance of Table from a dict
table_form_dict = table.from_dict(table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


