# ImageRepository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**database_name** | **str** |  | [optional] 
**schema_name** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] [readonly] 
**repository_url** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**owner_role_type** | **str** |  | [optional] [readonly] 

## Example

```python
from snowflake.core.image_repository._generated.models.image_repository import ImageRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ImageRepository from a JSON string
image_repository_instance = ImageRepository.from_json(json)
# print the JSON string representation of the object
print ImageRepository.to_json()

# convert the object into a dict
image_repository_dict = image_repository_instance.to_dict()
# create an instance of ImageRepository from a dict
image_repository_form_dict = image_repository.from_dict(image_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


