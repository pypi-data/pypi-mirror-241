# snowflake.core.compute_pool._generated.ComputePoolApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compute_pool**](ComputePoolApi.md#create_compute_pool) | **POST** /api/v2/compute-pools | Create a compute pool
[**create_or_alter_compute_pool**](ComputePoolApi.md#create_or_alter_compute_pool) | **PUT** /api/v2/compute-pools/{name} | Create a (or alter an existing) compute pool.
[**delete_compute_pool**](ComputePoolApi.md#delete_compute_pool) | **DELETE** /api/v2/compute-pools/{name} | Delete a compute pool
[**fetch_compute_pool**](ComputePoolApi.md#fetch_compute_pool) | **GET** /api/v2/compute-pools/{name} | Fetch a compute pool.
[**fetch_compute_pools**](ComputePoolApi.md#fetch_compute_pools) | **GET** /api/v2/compute-pools | List compute pools
[**resume_compute_pool**](ComputePoolApi.md#resume_compute_pool) | **POST** /api/v2/compute-pools/{name}:resume | Resume a compute pool
[**stop_all_services_in_compute_pool**](ComputePoolApi.md#stop_all_services_in_compute_pool) | **POST** /api/v2/compute-pools/{name}:stopallservices | Stops all services on the compute pool.
[**suspend_compute_pool**](ComputePoolApi.md#suspend_compute_pool) | **POST** /api/v2/compute-pools/{name}:suspend | Perform an action on a compute pool


# **create_compute_pool**
> CreateComputePool200Response create_compute_pool(compute_pool, create_mode=create_mode)

Create a compute pool

Create a compute pool, with standard create modifiers as query parameters. See the Compute Pool component definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    compute_pool = snowflake.core.compute_pool._generated.ComputePool() # ComputePool | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')

    try:
        # Create a compute pool
        api_response = api_instance.create_compute_pool(compute_pool, create_mode=create_mode)
        print("The response of ComputePoolApi->create_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->create_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_pool** | [**ComputePool**](ComputePool.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

# **create_or_alter_compute_pool**
> CreateComputePool200Response create_or_alter_compute_pool(name, compute_pool)

Create a (or alter an existing) compute pool.

Create a (or alter an existing) . Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 
    compute_pool = snowflake.core.compute_pool._generated.ComputePool() # ComputePool | 

    try:
        # Create a (or alter an existing) compute pool.
        api_response = api_instance.create_or_alter_compute_pool(name, compute_pool)
        print("The response of ComputePoolApi->create_or_alter_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->create_or_alter_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **compute_pool** | [**ComputePool**](ComputePool.md)|  | 

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

# **delete_compute_pool**
> CreateComputePool200Response delete_compute_pool(name, if_exists=if_exists)

Delete a compute pool

Delete a compute pool with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a 404 failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Delete a compute pool
        api_response = api_instance.delete_compute_pool(name, if_exists=if_exists)
        print("The response of ComputePoolApi->delete_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->delete_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

# **fetch_compute_pool**
> ComputePool fetch_compute_pool(name)

Fetch a compute pool.

Fetch a compute pool using the SHOW command output.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 

    try:
        # Fetch a compute pool.
        api_response = api_instance.fetch_compute_pool(name)
        print("The response of ComputePoolApi->fetch_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->fetch_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ComputePool**](ComputePool.md)

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

# **fetch_compute_pools**
> List[ComputePool] fetch_compute_pools(like=like, starts_with=starts_with, show_limit=show_limit)

List compute pools

Lists the compute pools under the account.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = {'key': snowflake.core.compute_pool._generated.FetchComputePoolsShowLimitParameter()} # FetchComputePoolsShowLimitParameter |  (optional)

    try:
        # List compute pools
        api_response = api_instance.fetch_compute_pools(like=like, starts_with=starts_with, show_limit=show_limit)
        print("The response of ComputePoolApi->fetch_compute_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->fetch_compute_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | [**FetchComputePoolsShowLimitParameter**](.md)|  | [optional] 

### Return type

[**List[ComputePool]**](ComputePool.md)

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

# **resume_compute_pool**
> CreateComputePool200Response resume_compute_pool(name)

Resume a compute pool

Resume a compute pool, if suspended. This is a no-op if it is already running.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 

    try:
        # Resume a compute pool
        api_response = api_instance.resume_compute_pool(name)
        print("The response of ComputePoolApi->resume_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->resume_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

# **stop_all_services_in_compute_pool**
> CreateComputePool200Response stop_all_services_in_compute_pool(name)

Stops all services on the compute pool.

Stop all services in the compute pool.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 

    try:
        # Stops all services on the compute pool.
        api_response = api_instance.stop_all_services_in_compute_pool(name)
        print("The response of ComputePoolApi->stop_all_services_in_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->stop_all_services_in_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

# **suspend_compute_pool**
> CreateComputePool200Response suspend_compute_pool(name)

Perform an action on a compute pool

Suspend a compute pool.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.compute_pool._generated
from snowflake.core.compute_pool._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.compute_pool._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.compute_pool._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.compute_pool._generated.ComputePoolApi(api_client)
    name = 'name_example' # str | 

    try:
        # Perform an action on a compute pool
        api_response = api_instance.suspend_compute_pool(name)
        print("The response of ComputePoolApi->suspend_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolApi->suspend_compute_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**CreateComputePool200Response**](CreateComputePool200Response.md)

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

