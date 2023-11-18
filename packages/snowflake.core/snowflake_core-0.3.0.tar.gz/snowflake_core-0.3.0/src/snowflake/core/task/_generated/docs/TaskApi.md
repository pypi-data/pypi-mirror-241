# snowflake.core.task._generated.TaskApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_alter_task**](TaskApi.md#create_or_alter_task) | **PUT** /api/v2/databases/{database}/schemas/{schema}/tasks/{name} | Create a (or alter an existing) task
[**create_task**](TaskApi.md#create_task) | **POST** /api/v2/databases/{database}/schemas/{schema}/tasks | Create a task
[**delete_task**](TaskApi.md#delete_task) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/tasks/{name} | Delete a task
[**execute_task**](TaskApi.md#execute_task) | **POST** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}:execute | Execute a task object.
[**fetch_task**](TaskApi.md#fetch_task) | **GET** /api/v2/databases/{database}/schemas/{schema}/tasks/{name} | Fetch a task
[**fetch_task_dependents**](TaskApi.md#fetch_task_dependents) | **GET** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}/dependents | Fetch the dependent tasks of a task
[**get_complete_graphs**](TaskApi.md#get_complete_graphs) | **GET** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}/complete_graphs | Get the graph runs that are completed for the task.
[**get_current_graphs**](TaskApi.md#get_current_graphs) | **GET** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}/current_graphs | Get the graph runs that are executing or scheduled for the task for the next 8 days.
[**list_tasks**](TaskApi.md#list_tasks) | **GET** /api/v2/databases/{database}/schemas/{schema}/tasks | List tasks
[**resume_task**](TaskApi.md#resume_task) | **POST** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}:resume | Resume a suspended task.
[**suspend_task**](TaskApi.md#suspend_task) | **POST** /api/v2/databases/{database}/schemas/{schema}/tasks/{name}:suspend | Suspends a running task.


# **create_or_alter_task**
> SuccessResponse create_or_alter_task(database, var_schema, name, task)

Create a (or alter an existing) task

Create a (or alter an existing) task. Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    task = snowflake.core.task._generated.Task() # Task | 

    try:
        # Create a (or alter an existing) task
        api_response = api_instance.create_or_alter_task(database, var_schema, name, task)
        print("The response of TaskApi->create_or_alter_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->create_or_alter_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **task** | [**Task**](Task.md)|  | 

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> SuccessResponse create_task(database, var_schema, task, create_mode=create_mode)

Create a task

Create a task, with standard create modifiers as query parameters. See the Task component definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    task = snowflake.core.task._generated.Task() # Task | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')

    try:
        # Create a task
        api_response = api_instance.create_task(database, var_schema, task, create_mode=create_mode)
        print("The response of TaskApi->create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **task** | [**Task**](Task.md)|  | 
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
**404** | Not Found. The request endpoint is not valid. This happens if the API endpoint does not exist, or if the API is not enabled. |  -  |
**405** | Method Not Allowed. The request method doesn&#39;t match the supported API. This happens, for example, if the application calls the API with GET method but the endpoint accepts only POST. |  -  |
**409** | Conflict. The requested operation could not be performed due to a conflicting state that could not be resolved. This usually happens when a CREATE request was performed when there is a pre-existing resource with the same name, and also without one of the options orReplace/ifNotExists.  |  -  |
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> SuccessResponse delete_task(database, var_schema, name, if_exists=if_exists)

Delete a task

Delete a task with the task name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Delete a task
        api_response = api_instance.delete_task(database, var_schema, name, if_exists=if_exists)
        print("The response of TaskApi->delete_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->delete_task: %s\n" % e)
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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_task**
> SuccessResponse execute_task(database, var_schema, name, retry_last=retry_last)

Execute a task object.

Execute a task -- this is equivalent to EXECUTE IMMEDIATE.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    retry_last = False # bool | Retry the last failed run of the DAG. (optional) (default to False)

    try:
        # Execute a task object.
        api_response = api_instance.execute_task(database, var_schema, name, retry_last=retry_last)
        print("The response of TaskApi->execute_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->execute_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **retry_last** | **bool**| Retry the last failed run of the DAG. | [optional] [default to False]

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

# **fetch_task**
> Task fetch_task(database, var_schema, name)

Fetch a task

Fetch a task using the describe command output.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Fetch a task
        api_response = api_instance.fetch_task(database, var_schema, name)
        print("The response of TaskApi->fetch_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->fetch_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Task**](Task.md)

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_task_dependents**
> List[Task] fetch_task_dependents(database, var_schema, name)

Fetch the dependent tasks of a task

This operation returns a list of the dependent tasks of the task with identifier {name}.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Fetch the dependent tasks of a task
        api_response = api_instance.fetch_task_dependents(database, var_schema, name)
        print("The response of TaskApi->fetch_task_dependents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->fetch_task_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**List[Task]**](Task.md)

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complete_graphs**
> List[TaskRun] get_complete_graphs(database, var_schema, name, result_limit=result_limit, error_only=error_only)

Get the graph runs that are completed for the task.

This function returns details for graph runs that are completed.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    result_limit = 56 # int | Number of results to return, at most. Default is 1000, valid range is 1 to 10000. (optional)
    error_only = True # bool | Whether to only return results for tasks runs that have failed. Default is false. (optional)

    try:
        # Get the graph runs that are completed for the task.
        api_response = api_instance.get_complete_graphs(database, var_schema, name, result_limit=result_limit, error_only=error_only)
        print("The response of TaskApi->get_complete_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_complete_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **result_limit** | **int**| Number of results to return, at most. Default is 1000, valid range is 1 to 10000. | [optional] 
 **error_only** | **bool**| Whether to only return results for tasks runs that have failed. Default is false. | [optional] 

### Return type

[**List[TaskRun]**](TaskRun.md)

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_graphs**
> List[TaskRun] get_current_graphs(database, var_schema, name, result_limit=result_limit)

Get the graph runs that are executing or scheduled for the task for the next 8 days.

This function returns details for graph runs that are currently executing or are next scheduled to run within the next 8 days.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    result_limit = 56 # int |  (optional)

    try:
        # Get the graph runs that are executing or scheduled for the task for the next 8 days.
        api_response = api_instance.get_current_graphs(database, var_schema, name, result_limit=result_limit)
        print("The response of TaskApi->get_current_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_current_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **result_limit** | **int**|  | [optional] 

### Return type

[**List[TaskRun]**](TaskRun.md)

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> List[Task] list_tasks(database, var_schema, root_only=root_only, like=like, starts_with=starts_with, show_limit=show_limit)

List tasks

Lists tasks under the database and schema, with show options as query parameters.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    root_only = False # bool |  (optional) (default to False)
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = 56 # int |  (optional)

    try:
        # List tasks
        api_response = api_instance.list_tasks(database, var_schema, root_only=root_only, like=like, starts_with=starts_with, show_limit=show_limit)
        print("The response of TaskApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **root_only** | **bool**|  | [optional] [default to False]
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | **int**|  | [optional] 

### Return type

[**List[Task]**](Task.md)

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
**429** | Limit Exceeded. The number of requests hit the rate limit. The application must slow down the frequency of hitting the API endpoints. |  -  |
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_task**
> SuccessResponse resume_task(database, var_schema, name)

Resume a suspended task.

Resumes a suspended task object. This is equivalento an ALTER TASK ... RESUME.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Resume a suspended task.
        api_response = api_instance.resume_task(database, var_schema, name)
        print("The response of TaskApi->resume_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->resume_task: %s\n" % e)
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

# **suspend_task**
> SuccessResponse suspend_task(database, var_schema, name)

Suspends a running task.

Suspends a running task. This is equivalent to an ALTER TASK ... SUSPEND.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.task._generated
from snowflake.core.task._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.task._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.task._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.task._generated.TaskApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Suspends a running task.
        api_response = api_instance.suspend_task(database, var_schema, name)
        print("The response of TaskApi->suspend_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->suspend_task: %s\n" % e)
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

