# snowflake.core.service._generated.ServiceApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServiceApi.md#create_service) | **POST** /api/v2/databases/{database}/schemas/{schema}/services | Create a service
[**delete_service**](ServiceApi.md#delete_service) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/services/{name} | Delete a service
[**fetch_service**](ServiceApi.md#fetch_service) | **GET** /api/v2/databases/{database}/schemas/{schema}/services/{name} | Fetch a service.
[**fetch_service_logs**](ServiceApi.md#fetch_service_logs) | **GET** /api/v2/databases/{database}/schemas/{schema}/services/{name}/logs | Fetch the logs for a given service.
[**fetch_service_status**](ServiceApi.md#fetch_service_status) | **GET** /api/v2/databases/{database}/schemas/{schema}/services/{name}/status | Fetch the status for a given service.
[**list_services**](ServiceApi.md#list_services) | **GET** /api/v2/databases/{database}/schemas/{schema}/services | List services
[**resume_service**](ServiceApi.md#resume_service) | **POST** /api/v2/databases/{database}/schemas/{schema}/services/{name}:resume | Resume a service
[**suspend_service**](ServiceApi.md#suspend_service) | **POST** /api/v2/databases/{database}/schemas/{schema}/services/{name}:suspend | Suspend a service


# **create_service**
> SuccessResponse create_service(database, var_schema, service, create_mode=create_mode)

Create a service

Create a service, with standard create modifiers as query parameters. See the Service component definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    service = snowflake.core.service._generated.Service() # Service | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')

    try:
        # Create a service
        api_response = api_instance.create_service(database, var_schema, service, create_mode=create_mode)
        print("The response of ServiceApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->create_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **service** | [**Service**](Service.md)|  | 
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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> SuccessResponse delete_service(database, var_schema, name, if_exists=if_exists)

Delete a service

Delete a service with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Delete a service
        api_response = api_instance.delete_service(database, var_schema, name, if_exists=if_exists)
        print("The response of ServiceApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
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

# **fetch_service**
> Service fetch_service(database, var_schema, name)

Fetch a service.

Fetch a Service using the SHOW command output.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Fetch a service.
        api_response = api_instance.fetch_service(database, var_schema, name)
        print("The response of ServiceApi->fetch_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->fetch_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Service**](Service.md)

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

# **fetch_service_logs**
> str fetch_service_logs(database, var_schema, name, instance_id=instance_id, container_name=container_name)

Fetch the logs for a given service.

Fetch the logs for a service.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    instance_id = 56 # int |  (optional)
    container_name = 'container_name_example' # str |  (optional)

    try:
        # Fetch the logs for a given service.
        api_response = api_instance.fetch_service_logs(database, var_schema, name, instance_id=instance_id, container_name=container_name)
        print("The response of ServiceApi->fetch_service_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->fetch_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **instance_id** | **int**|  | [optional] 
 **container_name** | **str**|  | [optional] 

### Return type

**str**

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

# **fetch_service_status**
> str fetch_service_status(database, var_schema, name, timeout=timeout)

Fetch the status for a given service.

Fetch the status for a service.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    timeout = 56 # int |  (optional)

    try:
        # Fetch the status for a given service.
        api_response = api_instance.fetch_service_status(database, var_schema, name, timeout=timeout)
        print("The response of ServiceApi->fetch_service_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->fetch_service_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **timeout** | **int**|  | [optional] 

### Return type

**str**

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

# **list_services**
> List[Service] list_services(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit)

List services

Lists the services under the database and schema.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = 56 # int |  (optional)

    try:
        # List services
        api_response = api_instance.list_services(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit)
        print("The response of ServiceApi->list_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | **int**|  | [optional] 

### Return type

[**List[Service]**](Service.md)

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

# **resume_service**
> SuccessResponse resume_service(database, var_schema, name)

Resume a service

Resume a service.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Resume a service
        api_response = api_instance.resume_service(database, var_schema, name)
        print("The response of ServiceApi->resume_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->resume_service: %s\n" % e)
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

# **suspend_service**
> SuccessResponse suspend_service(database, var_schema, name)

Suspend a service

Suspend a service.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.service._generated
from snowflake.core.service._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.service._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.service._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.service._generated.ServiceApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Suspend a service
        api_response = api_instance.suspend_service(database, var_schema, name)
        print("The response of ServiceApi->suspend_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->suspend_service: %s\n" % e)
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

