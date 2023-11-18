# TableColumn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**datatype** | **str** |  | 
**nullable** | **bool** |  | [optional] [default to True]
**collate** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**identity** | **bool** |  | [optional] 
**identity_start** | **int** |  | [optional] 
**identity_increment** | **int** |  | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from snowflake.core.table._generated.models.table_column import TableColumn

# TODO update the JSON string below
json = "{}"
# create an instance of TableColumn from a JSON string
table_column_instance = TableColumn.from_json(json)
# print the JSON string representation of the object
print TableColumn.to_json()

# convert the object into a dict
table_column_dict = table_column_instance.to_dict()
# create an instance of TableColumn from a dict
table_column_form_dict = table_column.from_dict(table_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


