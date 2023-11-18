# snowflake.core.database._generated.DatabaseApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabaseApi.md#create_database) | **POST** /api/v2/databases | Create a database
[**create_database_from_share**](DatabaseApi.md#create_database_from_share) | **POST** /api/v2/databases/from_share | Create a database from a share.
[**create_or_update_database**](DatabaseApi.md#create_or_update_database) | **PUT** /api/v2/databases/{name} | Create a (or alter an existing) database.
[**delete_database**](DatabaseApi.md#delete_database) | **DELETE** /api/v2/databases/{name} | Delete a database.
[**disable_database_failover**](DatabaseApi.md#disable_database_failover) | **POST** /api/v2/databases/{name}/failover:disable | Disable database failover.
[**disable_database_replication**](DatabaseApi.md#disable_database_replication) | **POST** /api/v2/databases/{name}/replication:disable | Disable database replication.
[**enable_database_failover**](DatabaseApi.md#enable_database_failover) | **POST** /api/v2/databases/{name}/failover:enable | Enable database failover.
[**enable_database_replication**](DatabaseApi.md#enable_database_replication) | **POST** /api/v2/databases/{name}/replication:enable | Enable database replication.
[**fetch_database**](DatabaseApi.md#fetch_database) | **GET** /api/v2/databases/{name} | 
[**list_databases**](DatabaseApi.md#list_databases) | **GET** /api/v2/databases | List databases
[**primary_database_failover**](DatabaseApi.md#primary_database_failover) | **POST** /api/v2/databases/{name}/failover:primary | Set database as primary.
[**refresh_database_replication**](DatabaseApi.md#refresh_database_replication) | **POST** /api/v2/databases/{name}/replication:refresh | Refresh database replications.


# **create_database**
> SuccessResponse create_database(database, create_mode=create_mode, kind=kind, clone=clone)

Create a database

Create a database, with modifiers as query parameters. See the database definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    database = snowflake.core.database._generated.Database() # Database | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')
    kind = 'kind_example' # str | Type of database. At the time of writing this transient and permanent (represented by the empty string) are supported. (optional)
    clone = snowflake.core.database._generated.Clone() # Clone |  (optional)

    try:
        # Create a database
        api_response = api_instance.create_database(database, create_mode=create_mode, kind=kind, clone=clone)
        print("The response of DatabaseApi->create_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | [**Database**](Database.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]
 **kind** | **str**| Type of database. At the time of writing this transient and permanent (represented by the empty string) are supported. | [optional] 
 **clone** | [**Clone**](.md)|  | [optional] 

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

# **create_database_from_share**
> SuccessResponse create_database_from_share(create_mode=create_mode, kind=kind, name=name, share=share)

Create a database from a share.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')
    kind = 'kind_example' # str | Type of database. At the time of writing this transient and permanent (represented by the empty string) are supported. (optional)
    name = 'name_example' # str |  (optional)
    share = 'share_example' # str | The share the database should be createdfrom. Should be of the form \"<provider_account>.<share_name>\". (optional)

    try:
        # Create a database from a share.
        api_response = api_instance.create_database_from_share(create_mode=create_mode, kind=kind, name=name, share=share)
        print("The response of DatabaseApi->create_database_from_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create_database_from_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]
 **kind** | **str**| Type of database. At the time of writing this transient and permanent (represented by the empty string) are supported. | [optional] 
 **name** | **str**|  | [optional] 
 **share** | **str**| The share the database should be createdfrom. Should be of the form \&quot;&lt;provider_account&gt;.&lt;share_name&gt;\&quot;. | [optional] 

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_database**
> SuccessResponse create_or_update_database(name, database)

Create a (or alter an existing) database.

Create a (or alter an existing) database. Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 
    database = snowflake.core.database._generated.Database() # Database | 

    try:
        # Create a (or alter an existing) database.
        api_response = api_instance.create_or_update_database(name, database)
        print("The response of DatabaseApi->create_or_update_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create_or_update_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **database** | [**Database**](Database.md)|  | 

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

# **delete_database**
> SuccessResponse delete_database(name)

Delete a database.

Delete a database with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete a database.
        api_response = api_instance.delete_database(name)
        print("The response of DatabaseApi->delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->delete_database: %s\n" % e)
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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_database_failover**
> SuccessResponse disable_database_failover(name, account_identifiers=account_identifiers)

Disable database failover.

Disables failover for this primary database, meaning no replica of this database (i.e. secondary database) can be promoted to serve as the primary database.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 
    account_identifiers = ['account_identifiers_example'] # List[str] | Unique identifier of the accounts. (optional)

    try:
        # Disable database failover.
        api_response = api_instance.disable_database_failover(name, account_identifiers=account_identifiers)
        print("The response of DatabaseApi->disable_database_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->disable_database_failover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **account_identifiers** | [**List[str]**](str.md)| Unique identifier of the accounts. | [optional] 

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_database_replication**
> SuccessResponse disable_database_replication(name, account_identifiers=account_identifiers)

Disable database replication.

Disables replication for this primary database, meaning no replica of this database (i.e. secondary database) in another account can be refreshed. Any secondary databases remain linked to the primary database, but requests to refresh a secondary database are denied.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 
    account_identifiers = ['account_identifiers_example'] # List[str] | Unique identifier of the accounts. (optional)

    try:
        # Disable database replication.
        api_response = api_instance.disable_database_replication(name, account_identifiers=account_identifiers)
        print("The response of DatabaseApi->disable_database_replication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->disable_database_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **account_identifiers** | [**List[str]**](str.md)| Unique identifier of the accounts. | [optional] 

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_database_failover**
> SuccessResponse enable_database_failover(name, account_identifiers)

Enable database failover.

Specifies a comma-separated list of accounts in your organization where a replica of this primary database can be promoted to serve as the primary database.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 
    account_identifiers = ['account_identifiers_example'] # List[str] | Unique identifier of the accounts.

    try:
        # Enable database failover.
        api_response = api_instance.enable_database_failover(name, account_identifiers)
        print("The response of DatabaseApi->enable_database_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->enable_database_failover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **account_identifiers** | [**List[str]**](str.md)| Unique identifier of the accounts. | 

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_database_replication**
> SuccessResponse enable_database_replication(name, account_identifiers, ignore_edition_check=ignore_edition_check)

Enable database replication.

Promotes a local database to serve as a primary database for replication. A primary database can be replicated in one or more accounts, allowing users in those accounts to query objects in each secondary (i.e. replica) database.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 
    account_identifiers = ['account_identifiers_example'] # List[str] | Unique identifier of the accounts.
    ignore_edition_check = True # bool | Allows replicating data to accounts on lower editions. Please see https://docs.snowflake.com/en/sql-reference/sql/alter-database for full description. (optional)

    try:
        # Enable database replication.
        api_response = api_instance.enable_database_replication(name, account_identifiers, ignore_edition_check=ignore_edition_check)
        print("The response of DatabaseApi->enable_database_replication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->enable_database_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **account_identifiers** | [**List[str]**](str.md)| Unique identifier of the accounts. | 
 **ignore_edition_check** | **bool**| Allows replicating data to accounts on lower editions. Please see https://docs.snowflake.com/en/sql-reference/sql/alter-database for full description. | [optional] 

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_database**
> Database fetch_database(name)



Fetch a database.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.fetch_database(name)
        print("The response of DatabaseApi->fetch_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->fetch_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Database**](Database.md)

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

# **list_databases**
> List[Database] list_databases(like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history)

List databases

Lists the accessible databases.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = 56 # int |  (optional)
    from_name = 'from_name_example' # str |  (optional)
    history = True # bool |  (optional)

    try:
        # List databases
        api_response = api_instance.list_databases(like=like, starts_with=starts_with, show_limit=show_limit, from_name=from_name, history=history)
        print("The response of DatabaseApi->list_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->list_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | **int**|  | [optional] 
 **from_name** | **str**|  | [optional] 
 **history** | **bool**|  | [optional] 

### Return type

[**List[Database]**](Database.md)

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

# **primary_database_failover**
> SuccessResponse primary_database_failover(name)

Set database as primary.

Promotes the specified secondary (replica) database to serve as the primary database.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 

    try:
        # Set database as primary.
        api_response = api_instance.primary_database_failover(name)
        print("The response of DatabaseApi->primary_database_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->primary_database_failover: %s\n" % e)
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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_database_replication**
> SuccessResponse refresh_database_replication(name)

Refresh database replications.

Refreshes a secondary database from a snapshot of its primary database. A snapshot includes changes to the objects and data.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.database._generated
from snowflake.core.database._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.database._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.database._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.database._generated.DatabaseApi(api_client)
    name = 'name_example' # str | 

    try:
        # Refresh database replications.
        api_response = api_instance.refresh_database_replication(name)
        print("The response of DatabaseApi->refresh_database_replication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->refresh_database_replication: %s\n" % e)
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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

