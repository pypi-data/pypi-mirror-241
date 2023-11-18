# Service


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**compute_pool** | **str** |  | 
**min_instances** | **int** |  | 
**max_instances** | **int** |  | 
**database_name** | **str** |  | [optional] 
**schema_name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] [readonly] 
**dns_name** | **str** |  | [optional] [readonly] 
**public_endpoints** | **str** |  | [optional] [readonly] 
**spec** | [**ServiceSpecification**](ServiceSpecification.md) |  | [optional] 

## Example

```python
from snowflake.core.service._generated.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


