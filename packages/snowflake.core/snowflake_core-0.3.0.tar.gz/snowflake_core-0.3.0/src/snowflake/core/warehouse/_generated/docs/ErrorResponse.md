# ErrorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message returned by server | [optional] 
**error_code** | **str** | Error code | [optional] 
**request_id** | **str** | Unique request id | [optional] 

## Example

```python
from snowflake.core.warehouse._generated.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print ErrorResponse.to_json()

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_form_dict = error_response.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


