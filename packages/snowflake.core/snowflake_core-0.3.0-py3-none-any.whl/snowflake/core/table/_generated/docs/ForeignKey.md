# ForeignKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referenced_table_name** | **str** |  | 
**referenced_column_names** | **List[str]** |  | 

## Example

```python
from snowflake.core.table._generated.models.foreign_key import ForeignKey

# TODO update the JSON string below
json = "{}"
# create an instance of ForeignKey from a JSON string
foreign_key_instance = ForeignKey.from_json(json)
# print the JSON string representation of the object
print ForeignKey.to_json()

# convert the object into a dict
foreign_key_dict = foreign_key_instance.to_dict()
# create an instance of ForeignKey from a dict
foreign_key_form_dict = foreign_key.from_dict(foreign_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


