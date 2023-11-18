# PointOfTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point_of_time_type** | **str** |  | 
**reference** | **str** | The relation to the point of time. At the time of writing at and before are supported. | [optional] 
**when** | **str** | The actual description of the point of time. | [optional] 

## Example

```python
from snowflake.core.schema._generated.models.point_of_time import PointOfTime

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfTime from a JSON string
point_of_time_instance = PointOfTime.from_json(json)
# print the JSON string representation of the object
print PointOfTime.to_json()

# convert the object into a dict
point_of_time_dict = point_of_time_instance.to_dict()
# create an instance of PointOfTime from a dict
point_of_time_form_dict = point_of_time.from_dict(point_of_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


