# FetchComputePoolsShowLimitParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **int** |  | 
**name_string** | **str** |  | [optional] 

## Example

```python
from snowflake.core.compute_pool._generated.models.fetch_compute_pools_show_limit_parameter import FetchComputePoolsShowLimitParameter

# TODO update the JSON string below
json = "{}"
# create an instance of FetchComputePoolsShowLimitParameter from a JSON string
fetch_compute_pools_show_limit_parameter_instance = FetchComputePoolsShowLimitParameter.from_json(json)
# print the JSON string representation of the object
print FetchComputePoolsShowLimitParameter.to_json()

# convert the object into a dict
fetch_compute_pools_show_limit_parameter_dict = fetch_compute_pools_show_limit_parameter_instance.to_dict()
# create an instance of FetchComputePoolsShowLimitParameter from a dict
fetch_compute_pools_show_limit_parameter_form_dict = fetch_compute_pools_show_limit_parameter.from_dict(fetch_compute_pools_show_limit_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


