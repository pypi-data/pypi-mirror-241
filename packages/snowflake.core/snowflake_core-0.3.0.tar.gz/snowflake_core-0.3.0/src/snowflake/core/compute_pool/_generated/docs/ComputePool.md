# ComputePool


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**warehouse** | **str** |  | [optional] 
**min_nodes** | **int** |  | 
**max_nodes** | **int** |  | 
**instance_family** | **str** |  | 
**auto_resume** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**state** | **str** |  | [optional] [readonly] 
**num_services** | **int** |  | [optional] [readonly] 
**auto_suspend_secs** | **int** |  | [optional] [readonly] 
**active_nodes** | **int** |  | [optional] [readonly] 
**idle_nodes** | **int** |  | [optional] [readonly] 
**created_on** | **datetime** |  | [optional] [readonly] 
**resumed_on** | **datetime** |  | [optional] [readonly] 
**updated_on** | **datetime** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 

## Example

```python
from snowflake.core.compute_pool._generated.models.compute_pool import ComputePool

# TODO update the JSON string below
json = "{}"
# create an instance of ComputePool from a JSON string
compute_pool_instance = ComputePool.from_json(json)
# print the JSON string representation of the object
print ComputePool.to_json()

# convert the object into a dict
compute_pool_dict = compute_pool_instance.to_dict()
# create an instance of ComputePool from a dict
compute_pool_form_dict = compute_pool.from_dict(compute_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


