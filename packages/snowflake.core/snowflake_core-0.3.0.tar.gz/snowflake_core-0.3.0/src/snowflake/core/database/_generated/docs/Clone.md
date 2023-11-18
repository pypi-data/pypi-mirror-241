# Clone

When cloning an obejct we need the source's name and a point of time that we want to clone at.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**point_of_time** | [**PointOfTime**](PointOfTime.md) |  | [optional] 

## Example

```python
from snowflake.core.database._generated.models.clone import Clone

# TODO update the JSON string below
json = "{}"
# create an instance of Clone from a JSON string
clone_instance = Clone.from_json(json)
# print the JSON string representation of the object
print Clone.to_json()

# convert the object into a dict
clone_dict = clone_instance.to_dict()
# create an instance of Clone from a dict
clone_form_dict = clone.from_dict(clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


