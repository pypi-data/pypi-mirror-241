# Constraint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**column_names** | **List[str]** |  | [optional] 
**constraint_type** | **str** |  | [optional] 

## Example

```python
from snowflake.core.table._generated.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print Constraint.to_json()

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_form_dict = constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


