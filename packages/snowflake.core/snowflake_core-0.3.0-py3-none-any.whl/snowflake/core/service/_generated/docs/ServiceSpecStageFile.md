# ServiceSpecStageFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_location** | **str** |  | 
**spec_file** | **str** |  | [optional] 

## Example

```python
from snowflake.core.service._generated.models.service_spec_stage_file import ServiceSpecStageFile

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSpecStageFile from a JSON string
service_spec_stage_file_instance = ServiceSpecStageFile.from_json(json)
# print the JSON string representation of the object
print ServiceSpecStageFile.to_json()

# convert the object into a dict
service_spec_stage_file_dict = service_spec_stage_file_instance.to_dict()
# create an instance of ServiceSpecStageFile from a dict
service_spec_stage_file_form_dict = service_spec_stage_file.from_dict(service_spec_stage_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


