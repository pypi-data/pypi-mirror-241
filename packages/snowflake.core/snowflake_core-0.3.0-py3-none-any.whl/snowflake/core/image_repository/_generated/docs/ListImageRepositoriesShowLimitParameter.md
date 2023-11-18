# ListImageRepositoriesShowLimitParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **int** |  | 
**name_string** | **str** |  | [optional] 

## Example

```python
from snowflake.core.image_repository._generated.models.list_image_repositories_show_limit_parameter import ListImageRepositoriesShowLimitParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ListImageRepositoriesShowLimitParameter from a JSON string
list_image_repositories_show_limit_parameter_instance = ListImageRepositoriesShowLimitParameter.from_json(json)
# print the JSON string representation of the object
print ListImageRepositoriesShowLimitParameter.to_json()

# convert the object into a dict
list_image_repositories_show_limit_parameter_dict = list_image_repositories_show_limit_parameter_instance.to_dict()
# create an instance of ListImageRepositoriesShowLimitParameter from a dict
list_image_repositories_show_limit_parameter_form_dict = list_image_repositories_show_limit_parameter.from_dict(list_image_repositories_show_limit_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


