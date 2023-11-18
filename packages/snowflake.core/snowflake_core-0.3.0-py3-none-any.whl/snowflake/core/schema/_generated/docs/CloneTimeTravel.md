# CloneTimeTravel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | **str** | The relation to the point of time. At the time of writing at and before are supported. | [optional] 
**point_of_time** | [**CloneTimeTravelPointOfTime**](CloneTimeTravelPointOfTime.md) |  | [optional] 

## Example

```python
from snowflake.core.schema._generated.models.clone_time_travel import CloneTimeTravel

# TODO update the JSON string below
json = "{}"
# create an instance of CloneTimeTravel from a JSON string
clone_time_travel_instance = CloneTimeTravel.from_json(json)
# print the JSON string representation of the object
print CloneTimeTravel.to_json()

# convert the object into a dict
clone_time_travel_dict = clone_time_travel_instance.to_dict()
# create an instance of CloneTimeTravel from a dict
clone_time_travel_form_dict = clone_time_travel.from_dict(clone_time_travel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


