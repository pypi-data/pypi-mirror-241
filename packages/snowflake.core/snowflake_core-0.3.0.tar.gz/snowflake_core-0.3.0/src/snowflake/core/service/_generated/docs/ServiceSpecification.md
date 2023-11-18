# ServiceSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_type** | **str** |  | [optional] 

## Example

```python
from snowflake.core.service._generated.models.service_specification import ServiceSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSpecification from a JSON string
service_specification_instance = ServiceSpecification.from_json(json)
# print the JSON string representation of the object
print ServiceSpecification.to_json()

# convert the object into a dict
service_specification_dict = service_specification_instance.to_dict()
# create an instance of ServiceSpecification from a dict
service_specification_form_dict = service_specification.from_dict(service_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


