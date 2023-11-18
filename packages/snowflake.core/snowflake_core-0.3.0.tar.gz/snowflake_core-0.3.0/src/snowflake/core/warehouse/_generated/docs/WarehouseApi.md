# snowflake.core.warehouse._generated.WarehouseApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_all_queries_on_warehouse**](WarehouseApi.md#abort_all_queries_on_warehouse) | **POST** /api/v2/warehouses/{name}:abort | abort all queries
[**create_warehouses**](WarehouseApi.md#create_warehouses) | **POST** /api/v2/warehouses | Create or replace warehouse
[**describe_warehouse**](WarehouseApi.md#describe_warehouse) | **GET** /api/v2/warehouses/{name} | Describe warehouse
[**drop_warehouse**](WarehouseApi.md#drop_warehouse) | **DELETE** /api/v2/warehouses/{name} | Drop warehouse
[**list_warehouses**](WarehouseApi.md#list_warehouses) | **GET** /api/v2/warehouses | List warehouse
[**rename_warehouse**](WarehouseApi.md#rename_warehouse) | **POST** /api/v2/warehouses/{name}:rename | update and rename warehouse
[**resume_warehouse**](WarehouseApi.md#resume_warehouse) | **POST** /api/v2/warehouses/{name}:resume | resume warehouse
[**set_warehouse**](WarehouseApi.md#set_warehouse) | **PUT** /api/v2/warehouses/{name} | update parameters of the warehouse
[**suspend_warehouse**](WarehouseApi.md#suspend_warehouse) | **POST** /api/v2/warehouses/{name}:suspend | suspend warehouse
[**tag_warehouse**](WarehouseApi.md#tag_warehouse) | **POST** /api/v2/warehouses/{name}:tag | Set tags for warehouse
[**use_warehouse**](WarehouseApi.md#use_warehouse) | **POST** /api/v2/warehouses/{name}:use | use current warehouse for session


# **abort_all_queries_on_warehouse**
> SuccessResponse abort_all_queries_on_warehouse(name, if_exists=if_exists)

abort all queries

Aborts all the queries currently running or queued on the warehouse.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # abort all queries
        api_response = api_instance.abort_all_queries_on_warehouse(name, if_exists=if_exists)
        print("The response of WarehouseApi->abort_all_queries_on_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->abort_all_queries_on_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_warehouses**
> SuccessResponse create_warehouses(warehouse, create_mode=create_mode)

Create or replace warehouse

Create a virtual warehouse. Equivalent to CREATE WAREHOUSE in SQL.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    warehouse = snowflake.core.warehouse._generated.Warehouse() # Warehouse | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')

    try:
        # Create or replace warehouse
        api_response = api_instance.create_warehouses(warehouse, create_mode=create_mode)
        print("The response of WarehouseApi->create_warehouses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->create_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse** | [**Warehouse**](Warehouse.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]

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
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_warehouse**
> Warehouse describe_warehouse(name)

Describe warehouse

Describes the warehouse, show infomation of the choosen warehouse. Equivalent to DESCRIBE WAREHOUSE in SQL.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 

    try:
        # Describe warehouse
        api_response = api_instance.describe_warehouse(name)
        print("The response of WarehouseApi->describe_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->describe_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Warehouse**](Warehouse.md)

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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_warehouse**
> SuccessResponse drop_warehouse(name, if_exists=if_exists)

Drop warehouse

Removes the specified virtual warehouse from the system. Equivalent to DROP WAREHOUSE in SQL.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Drop warehouse
        api_response = api_instance.drop_warehouse(name, if_exists=if_exists)
        print("The response of WarehouseApi->drop_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->drop_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_warehouses**
> List[Warehouse] list_warehouses(like=like)

List warehouse

Show a list of warehouse filted by pattern. Equivalent to SHOW WAREHOUSE in SQL.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    like = 'like_example' # str |  (optional)

    try:
        # List warehouse
        api_response = api_instance.list_warehouses(like=like)
        print("The response of WarehouseApi->list_warehouses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->list_warehouses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **like** | **str**|  | [optional] 

### Return type

[**List[Warehouse]**](Warehouse.md)

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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_warehouse**
> SuccessResponse rename_warehouse(name, warehouse, if_exists=if_exists)

update and rename warehouse

Specifies a new identifier for the warehouse; must be unique for current account.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    warehouse = snowflake.core.warehouse._generated.Warehouse() # Warehouse | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # update and rename warehouse
        api_response = api_instance.rename_warehouse(name, warehouse, if_exists=if_exists)
        print("The response of WarehouseApi->rename_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->rename_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **warehouse** | [**Warehouse**](Warehouse.md)|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

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
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_warehouse**
> SuccessResponse resume_warehouse(name, if_exists=if_exists)

resume warehouse

Bring current warehouse to a usable ‘Running’ state by provisioning compute resources if current warehouse is suspended.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # resume warehouse
        api_response = api_instance.resume_warehouse(name, if_exists=if_exists)
        print("The response of WarehouseApi->resume_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->resume_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_warehouse**
> SuccessResponse set_warehouse(name, warehouse, if_exists=if_exists)

update parameters of the warehouse

Specifies one or more properties/parameters to set for the warehouse. If one parameter is not specified, it will be unset, which means it will be reset to default.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    warehouse = snowflake.core.warehouse._generated.Warehouse() # Warehouse | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # update parameters of the warehouse
        api_response = api_instance.set_warehouse(name, warehouse, if_exists=if_exists)
        print("The response of WarehouseApi->set_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->set_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **warehouse** | [**Warehouse**](Warehouse.md)|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

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
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_warehouse**
> SuccessResponse suspend_warehouse(name, if_exists=if_exists)

suspend warehouse

Remove all compute nodes from a warehouse and put the warehouse into a ‘Suspended’ state if current warehouse is not suspended.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # suspend warehouse
        api_response = api_instance.suspend_warehouse(name, if_exists=if_exists)
        print("The response of WarehouseApi->suspend_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->suspend_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_warehouse**
> SuccessResponse tag_warehouse(name, body, if_exists=if_exists)

Set tags for warehouse

Specifies one or more tags to set for the warehouse.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 
    body = None # object | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Set tags for warehouse
        api_response = api_instance.tag_warehouse(name, body, if_exists=if_exists)
        print("The response of WarehouseApi->tag_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->tag_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | **object**|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

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
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_warehouse**
> SuccessResponse use_warehouse(name)

use current warehouse for session

Specifies the active/current warehouse for the session.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.warehouse._generated
from snowflake.core.warehouse._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.warehouse._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.warehouse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.warehouse._generated.WarehouseApi(api_client)
    name = 'name_example' # str | 

    try:
        # use current warehouse for session
        api_response = api_instance.use_warehouse(name)
        print("The response of WarehouseApi->use_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseApi->use_warehouse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**410** | Gone. This error is primarily intended to assist the task of web maintenance by notifying the recipient that the resource is intentionally unavailable. |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

