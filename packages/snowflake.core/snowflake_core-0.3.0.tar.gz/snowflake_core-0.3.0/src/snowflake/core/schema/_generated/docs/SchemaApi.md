# snowflake.core.schema._generated.SchemaApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_schema**](SchemaApi.md#create_or_update_schema) | **PUT** /api/v2/databases/{database}/schemas/{name} | Create a (or alter an existing) schema.
[**create_schema**](SchemaApi.md#create_schema) | **POST** /api/v2/databases/{database}/schemas | Create a schema
[**delete_schema**](SchemaApi.md#delete_schema) | **DELETE** /api/v2/databases/{database}/schemas/{name} | Delete a schema.
[**fetch_schema**](SchemaApi.md#fetch_schema) | **GET** /api/v2/databases/{database}/schemas/{name} | 
[**list_schemas**](SchemaApi.md#list_schemas) | **GET** /api/v2/databases/{database}/schemas | List schemas


# **create_or_update_schema**
> SuccessResponse create_or_update_schema(database, name, model_schema)

Create a (or alter an existing) schema.

Create a (or alter an existing) schema. Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.schema._generated
from snowflake.core.schema._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.schema._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.schema._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.schema._generated.SchemaApi(api_client)
    database = 'database_example' # str | 
    name = 'name_example' # str | 
    model_schema = snowflake.core.schema._generated.ModelSchema() # ModelSchema | 

    try:
        # Create a (or alter an existing) schema.
        api_response = api_instance.create_or_update_schema(database, name, model_schema)
        print("The response of SchemaApi->create_or_update_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->create_or_update_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **name** | **str**|  | 
 **model_schema** | [**ModelSchema**](ModelSchema.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_schema**
> SuccessResponse create_schema(database, model_schema, create_mode=create_mode, kind=kind, clone=clone, with_managed_access=with_managed_access)

Create a schema

Create a schema, with modifiers as query parameters. See the schema definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.schema._generated
from snowflake.core.schema._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.schema._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.schema._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.schema._generated.SchemaApi(api_client)
    database = 'database_example' # str | 
    model_schema = snowflake.core.schema._generated.ModelSchema() # ModelSchema | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')
    kind = '' # str | Type of schema. At the time of writing this transient and permanent (represented by the empty string) are supported. (optional) (default to '')
    clone = snowflake.core.schema._generated.Clone() # Clone |  (optional)
    with_managed_access = False # bool | Specifies a managed schema. Managed access schemas centralize privilege management with the schema owner. (optional) (default to False)

    try:
        # Create a schema
        api_response = api_instance.create_schema(database, model_schema, create_mode=create_mode, kind=kind, clone=clone, with_managed_access=with_managed_access)
        print("The response of SchemaApi->create_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->create_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **model_schema** | [**ModelSchema**](ModelSchema.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]
 **kind** | **str**| Type of schema. At the time of writing this transient and permanent (represented by the empty string) are supported. | [optional] [default to &#39;&#39;]
 **clone** | [**Clone**](.md)|  | [optional] 
 **with_managed_access** | **bool**| Specifies a managed schema. Managed access schemas centralize privilege management with the schema owner. | [optional] [default to False]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schema**
> SuccessResponse delete_schema(database, name)

Delete a schema.

Delete a schema with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.schema._generated
from snowflake.core.schema._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.schema._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.schema._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.schema._generated.SchemaApi(api_client)
    database = 'database_example' # str | 
    name = 'name_example' # str | 

    try:
        # Delete a schema.
        api_response = api_instance.delete_schema(database, name)
        print("The response of SchemaApi->delete_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->delete_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_schema**
> ModelSchema fetch_schema(database, name)



Fetch a schema.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.schema._generated
from snowflake.core.schema._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.schema._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.schema._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.schema._generated.SchemaApi(api_client)
    database = 'database_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = api_instance.fetch_schema(database, name)
        print("The response of SchemaApi->fetch_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->fetch_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schemas**
> List[ModelSchema] list_schemas(database, like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history)

List schemas

Lists the accessible schemas.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.schema._generated
from snowflake.core.schema._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.schema._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.schema._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.schema._generated.SchemaApi(api_client)
    database = 'database_example' # str | 
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = 56 # int |  (optional)
    from_name = 'from_name_example' # str |  (optional)
    history = False # bool |  (optional) (default to False)

    try:
        # List schemas
        api_response = api_instance.list_schemas(database, like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history)
        print("The response of SchemaApi->list_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->list_schemas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | **int**|  | [optional] 
 **from_name** | **str**|  | [optional] 
 **history** | **bool**|  | [optional] [default to False]

### Return type

[**List[ModelSchema]**](ModelSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

