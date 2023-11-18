# PointOfTimeStatement

A point of time that is identified by when a statement was executed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from snowflake.core.schema._generated.models.point_of_time_statement import PointOfTimeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfTimeStatement from a JSON string
point_of_time_statement_instance = PointOfTimeStatement.from_json(json)
# print the JSON string representation of the object
print PointOfTimeStatement.to_json()

# convert the object into a dict
point_of_time_statement_dict = point_of_time_statement_instance.to_dict()
# create an instance of PointOfTimeStatement from a dict
point_of_time_statement_form_dict = point_of_time_statement.from_dict(point_of_time_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


