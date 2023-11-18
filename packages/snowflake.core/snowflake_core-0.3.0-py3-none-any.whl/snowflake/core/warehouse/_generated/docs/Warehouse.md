# Warehouse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**warehouse_type** | **str** | Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED | [optional] 
**warehouse_size** | **str** | Size of warehouse, possible sizes: XSMALL, SMALL, MEDIUM, LARGE, XLARGE, XXLARGE, XXXLARGE, X4LARGE, X5LARGE, X6LARGE | [optional] 
**wait_for_completion** | **str** |  | [optional] 
**max_cluster_count** | **int** |  | [optional] 
**min_cluster_count** | **int** |  | [optional] 
**scaling_policy** | **str** | Scaling policy of warehouse, possible scaling policies: STANDARD, ECONOMY | [optional] 
**auto_suspend** | **int** | time in seconds before auto suspend | [optional] 
**auto_resume** | **str** |  | [optional] 
**initially_suspended** | **str** |  | [optional] 
**resource_monitor** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**enable_query_acceleration** | **str** |  | [optional] 
**query_acceleration_max_scale_factor** | **int** |  | [optional] 
**max_concurrency_level** | **int** |  | [optional] 
**statement_queued_timeout_in_seconds** | **int** |  | [optional] 
**statement_timeout_in_seconds** | **int** |  | [optional] 
**tags** | **Dict[str, str]** | &lt;tag_name&gt; &#x3D; &#39;&lt;tag_value&gt;&#39; , ... | [optional] 
**type** | **str** | Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED | [optional] 
**size** | **str** | names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large | [optional] 
**state** | **str** | The state of warehouse, possible states: STARTED, STARTING, DYNAMIC, SUSPENDED, RESIZING, RESUMING, SUSPENDING | [optional] [readonly] 
**started_clusters** | **int** | Number of clusters currently started. | [optional] [readonly] 
**running** | **int** | Number of SQL statements that are being executed by the warehouse. | [optional] [readonly] 
**queued** | **int** | Number of SQL statements that are queued for the warehouse. | [optional] [readonly] 
**is_default** | **str** | Whether the warehouse is the default for the current user. | [optional] [readonly] 
**is_current** | **str** | Whether the warehouse is in use for the session. Only one warehouse can be in use at a time for a session. To specify or change the warehouse for a session, use the USE WAREHOUSE command. | [optional] [readonly] 
**available** | **str** | Percentage of the warehouse compute resources that are provisioned and available. | [optional] [readonly] 
**provisioning** | **str** | Percentage of the warehouse compute resources that are in the process of provisioning. | [optional] [readonly] 
**quiescing** | **str** | Percentage of the warehouse compute resources that are executing SQL statements, but will be shut down once the queries complete. | [optional] [readonly] 
**other** | **str** | Percentage of the warehouse compute resources that are in a state other than available, provisioning, or quiescing. | [optional] [readonly] 
**created_on** | **datetime** | Date and time when the warehouse was created. | [optional] [readonly] 
**resumed_on** | **datetime** | Date and time when the warehouse was last started or restarted. | [optional] [readonly] 
**updated_on** | **datetime** | Date and time when the warehouse was last updated, which includes changing any of the properties of the warehouse or changing the state (STARTED, SUSPENDED, RESIZING) of the warehouse. | [optional] [readonly] 
**owner** | **str** | Role that owns the warehouse. | [optional] [readonly] 
**kind** | **str** |  | [optional] [readonly] 
**tag** | **object** |  | [optional] 

## Example

```python
from snowflake.core.warehouse._generated.models.warehouse import Warehouse

# TODO update the JSON string below
json = "{}"
# create an instance of Warehouse from a JSON string
warehouse_instance = Warehouse.from_json(json)
# print the JSON string representation of the object
print Warehouse.to_json()

# convert the object into a dict
warehouse_dict = warehouse_instance.to_dict()
# create an instance of Warehouse from a dict
warehouse_form_dict = warehouse.from_dict(warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


