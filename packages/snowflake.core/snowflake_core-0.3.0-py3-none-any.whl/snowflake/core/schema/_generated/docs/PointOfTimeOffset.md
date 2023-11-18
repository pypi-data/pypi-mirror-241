# PointOfTimeOffset

A point of time that is identified by an offset in reference to right now.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from snowflake.core.schema._generated.models.point_of_time_offset import PointOfTimeOffset

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfTimeOffset from a JSON string
point_of_time_offset_instance = PointOfTimeOffset.from_json(json)
# print the JSON string representation of the object
print PointOfTimeOffset.to_json()

# convert the object into a dict
point_of_time_offset_dict = point_of_time_offset_instance.to_dict()
# create an instance of PointOfTimeOffset from a dict
point_of_time_offset_form_dict = point_of_time_offset.from_dict(point_of_time_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


