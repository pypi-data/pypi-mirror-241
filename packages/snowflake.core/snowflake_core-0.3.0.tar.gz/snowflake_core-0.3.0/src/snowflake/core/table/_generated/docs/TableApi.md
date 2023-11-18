# snowflake.core.table._generated.TableApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_search_optimization**](TableApi.md#add_search_optimization) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/search_optimization | Add search optimization.
[**create_or_update_table**](TableApi.md#create_or_update_table) | **PUT** /api/v2/databases/{database}/schemas/{schema}/tables/{name} | Create a (or alter an existing) table.
[**create_table**](TableApi.md#create_table) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables | Create a table
[**delete_row_access_policy**](TableApi.md#delete_row_access_policy) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/row_access_policy/{name} | Delete a row access policy.
[**delete_search_optimization**](TableApi.md#delete_search_optimization) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/search_optimization | Delete search optimization.
[**delete_table**](TableApi.md#delete_table) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/tables/{name} | Delete a table
[**fetch_effective_parameters**](TableApi.md#fetch_effective_parameters) | **GET** /api/v2/databases/{database}/schemas/{schema}/tables/{name}/parameters/effective | Fetch the effective parameters of a table.
[**fetch_table**](TableApi.md#fetch_table) | **GET** /api/v2/databases/{database}/schemas/{schema}/tables/{name} | Fetch a table.
[**list_tables**](TableApi.md#list_tables) | **GET** /api/v2/databases/{database}/schemas/{schema}/tables | List tables
[**rename_column**](TableApi.md#rename_column) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/columns/{name}:rename | Rename a column
[**rename_constraint**](TableApi.md#rename_constraint) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/constraints/{constraint_name}:rename | Rename a table constraint.
[**rename_table**](TableApi.md#rename_table) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{name}:rename | Rename a table
[**resume_recluster**](TableApi.md#resume_recluster) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{name}:resume_recluster | Resume recluster of a table
[**set_column_masking_policy**](TableApi.md#set_column_masking_policy) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{table}/columns/{column_name}/masking_policy | Set column masking policy.
[**set_row_access_policy**](TableApi.md#set_row_access_policy) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{table_name}/row_access_policy | Set row access policy.
[**suspend_recluster**](TableApi.md#suspend_recluster) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{name}:suspend_recluster | Suspend recluster of a table
[**swap_with**](TableApi.md#swap_with) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{name}:swapwith | Swap with another table
[**undelete_table**](TableApi.md#undelete_table) | **POST** /api/v2/databases/{database}/schemas/{schema}/tables/{name}:undelete | Undelete a deleted table.
[**unset_column_masking_policy**](TableApi.md#unset_column_masking_policy) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/tables/{table}/columns/{column_name}/masking_policy | Unset column masking policy.


# **add_search_optimization**
> SuccessResponse add_search_optimization(database, var_schema, name, targets)

Add search optimization.

Add search optimization.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    targets = ['targets_example'] # List[str] | 

    try:
        # Add search optimization.
        api_response = api_instance.add_search_optimization(database, var_schema, name, targets)
        print("The response of TableApi->add_search_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->add_search_optimization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **targets** | [**List[str]**](str.md)|  | 

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

# **create_or_update_table**
> SuccessResponse create_or_update_table(database, var_schema, name, table)

Create a (or alter an existing) table.

Create a (or alter an existing) table. Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    table = snowflake.core.table._generated.Table() # Table | 

    try:
        # Create a (or alter an existing) table.
        api_response = api_instance.create_or_update_table(database, var_schema, name, table)
        print("The response of TableApi->create_or_update_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->create_or_update_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **table** | [**Table**](Table.md)|  | 

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
**201** | Successful |  -  |
**400** | Bad Request. The request payload is invalid or malformed. This happens if the application didn&#39;t send the correct request payload. The response body may include the error code and message indicating the actual cause. The application must reconstruct the request body for retry. |  -  |
**401** | Unauthorized. The request is not authorized. This happens if the attached access token is invalid or missing. The response body may include the error code and message indicating the actual cause, e.g., expired, invalid token. The application must obtain a new access token for retry. |  -  |
**403** | Forbidden. The request is forbidden. This can also happen if the request is made even if the API is not enabled. |  -  |
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_table**
> SuccessResponse create_table(database, var_schema, table, create_mode=create_mode, as_select=as_select, template_query=template_query, like_table=like_table, clone_table=clone_table, copy_grants=copy_grants)

Create a table

Create a table.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    table = snowflake.core.table._generated.Table() # Table | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')
    as_select = 'as_select_example' # str |  (optional)
    template_query = 'template_query_example' # str |  (optional)
    like_table = 'like_table_example' # str |  (optional)
    clone_table = 'clone_table_example' # str |  (optional)
    copy_grants = True # bool |  (optional)

    try:
        # Create a table
        api_response = api_instance.create_table(database, var_schema, table, create_mode=create_mode, as_select=as_select, template_query=template_query, like_table=like_table, clone_table=clone_table, copy_grants=copy_grants)
        print("The response of TableApi->create_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->create_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **table** | [**Table**](Table.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]
 **as_select** | **str**|  | [optional] 
 **template_query** | **str**|  | [optional] 
 **like_table** | **str**|  | [optional] 
 **clone_table** | **str**|  | [optional] 
 **copy_grants** | **bool**|  | [optional] 

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
**201** | Successful |  -  |
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

# **delete_row_access_policy**
> SuccessResponse delete_row_access_policy(database, var_schema, name)

Delete a row access policy.

Delete a row access policy.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Delete a row access policy.
        api_response = api_instance.delete_row_access_policy(database, var_schema, name)
        print("The response of TableApi->delete_row_access_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->delete_row_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
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

# **delete_search_optimization**
> SuccessResponse delete_search_optimization(database, var_schema, name, targets=targets)

Delete search optimization.

Delete search optimization.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    targets = ['targets_example'] # List[str] |  (optional)

    try:
        # Delete search optimization.
        api_response = api_instance.delete_search_optimization(database, var_schema, name, targets=targets)
        print("The response of TableApi->delete_search_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->delete_search_optimization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **targets** | [**List[str]**](str.md)|  | [optional] 

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

# **delete_table**
> SuccessResponse delete_table(database, var_schema, name, if_exists=if_exists)

Delete a table

Delete a table with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the delete is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Delete a table
        api_response = api_instance.delete_table(database, var_schema, name, if_exists=if_exists)
        print("The response of TableApi->delete_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->delete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

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

# **fetch_effective_parameters**
> Dict[str, object] fetch_effective_parameters(database, var_schema, name)

Fetch the effective parameters of a table.

Fetch the effective parameters of a table.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Fetch the effective parameters of a table.
        api_response = api_instance.fetch_effective_parameters(database, var_schema, name)
        print("The response of TableApi->fetch_effective_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->fetch_effective_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **fetch_table**
> Table fetch_table(database, var_schema, name, deep=deep)

Fetch a table.

Fetch a Table using the SHOW command output.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    deep = True # bool |  (optional)

    try:
        # Fetch a table.
        api_response = api_instance.fetch_table(database, var_schema, name, deep=deep)
        print("The response of TableApi->fetch_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->fetch_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **deep** | **bool**|  | [optional] 

### Return type

[**Table**](Table.md)

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

# **list_tables**
> List[Table] list_tables(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history, deep=deep)

List tables

Lists the tables under the database and schema.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = 56 # int |  (optional)
    from_name = 'from_name_example' # str |  (optional)
    history = True # bool |  (optional)
    deep = True # bool |  (optional)

    try:
        # List tables
        api_response = api_instance.list_tables(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history, deep=deep)
        print("The response of TableApi->list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->list_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | **int**|  | [optional] 
 **from_name** | **str**|  | [optional] 
 **history** | **bool**|  | [optional] 
 **deep** | **bool**|  | [optional] 

### Return type

[**List[Table]**](Table.md)

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

# **rename_column**
> SuccessResponse rename_column(database, var_schema, name, new_name)

Rename a column

Rename a column

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    new_name = 'new_name_example' # str | 

    try:
        # Rename a column
        api_response = api_instance.rename_column(database, var_schema, name, new_name)
        print("The response of TableApi->rename_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->rename_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **new_name** | **str**|  | 

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

# **rename_constraint**
> SuccessResponse rename_constraint(database, var_schema, name, new_name)

Rename a table constraint.

Rename a table constraint

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    new_name = 'new_name_example' # str | 

    try:
        # Rename a table constraint.
        api_response = api_instance.rename_constraint(database, var_schema, name, new_name)
        print("The response of TableApi->rename_constraint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->rename_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **new_name** | **str**|  | 

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

# **rename_table**
> SuccessResponse rename_table(database, var_schema, name, new_name)

Rename a table

Rename a table

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    new_name = 'new_name_example' # str | 

    try:
        # Rename a table
        api_response = api_instance.rename_table(database, var_schema, name, new_name)
        print("The response of TableApi->rename_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->rename_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **new_name** | **str**|  | 

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

# **resume_recluster**
> SuccessResponse resume_recluster(database, var_schema, name)

Resume recluster of a table

Resume recluster of a table

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Resume recluster of a table
        api_response = api_instance.resume_recluster(database, var_schema, name)
        print("The response of TableApi->resume_recluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->resume_recluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
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

# **set_column_masking_policy**
> SuccessResponse set_column_masking_policy(database, var_schema, table, column_name, masking_policy_name, using=using, force=force)

Set column masking policy.

Set column masking policy.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    table = 'table_example' # str | 
    column_name = 'column_name_example' # str | 
    masking_policy_name = 'masking_policy_name_example' # str | 
    using = ['using_example'] # List[str] |  (optional)
    force = True # bool |  (optional)

    try:
        # Set column masking policy.
        api_response = api_instance.set_column_masking_policy(database, var_schema, table, column_name, masking_policy_name, using=using, force=force)
        print("The response of TableApi->set_column_masking_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->set_column_masking_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **table** | **str**|  | 
 **column_name** | **str**|  | 
 **masking_policy_name** | **str**|  | 
 **using** | [**List[str]**](str.md)|  | [optional] 
 **force** | **bool**|  | [optional] 

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

# **set_row_access_policy**
> SuccessResponse set_row_access_policy(database, var_schema, name, row_access_policy_name, columns)

Set row access policy.

Set row access policy.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    row_access_policy_name = 'row_access_policy_name_example' # str | 
    columns = ['columns_example'] # List[str] | 

    try:
        # Set row access policy.
        api_response = api_instance.set_row_access_policy(database, var_schema, name, row_access_policy_name, columns)
        print("The response of TableApi->set_row_access_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->set_row_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **row_access_policy_name** | **str**|  | 
 **columns** | [**List[str]**](str.md)|  | 

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

# **suspend_recluster**
> SuccessResponse suspend_recluster(database, var_schema, name)

Suspend recluster of a table

Suspend recluster of a table

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Suspend recluster of a table
        api_response = api_instance.suspend_recluster(database, var_schema, name)
        print("The response of TableApi->suspend_recluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->suspend_recluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
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

# **swap_with**
> SuccessResponse swap_with(database, var_schema, name, to_swap_table_name)

Swap with another table

Swap with another table

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    to_swap_table_name = 'to_swap_table_name_example' # str | 

    try:
        # Swap with another table
        api_response = api_instance.swap_with(database, var_schema, name, to_swap_table_name)
        print("The response of TableApi->swap_with:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->swap_with: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **to_swap_table_name** | **str**|  | 

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

# **undelete_table**
> SuccessResponse undelete_table(database, var_schema, name)

Undelete a deleted table.

Undelete a deleted table. This is equivalento UNDROP <table>.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Undelete a deleted table.
        api_response = api_instance.undelete_table(database, var_schema, name)
        print("The response of TableApi->undelete_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->undelete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_column_masking_policy**
> SuccessResponse unset_column_masking_policy(database, var_schema, name)

Unset column masking policy.

Unset column masking policy.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.table._generated
from snowflake.core.table._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.table._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.table._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.table._generated.TableApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Unset column masking policy.
        api_response = api_instance.unset_column_masking_policy(database, var_schema, name)
        print("The response of TableApi->unset_column_masking_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TableApi->unset_column_masking_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
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

