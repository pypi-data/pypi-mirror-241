# snowflake.core.image_repository._generated.ImageRepositoryApi

All URIs are relative to *https://org-account.snowflakecomputing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_repository**](ImageRepositoryApi.md#create_image_repository) | **POST** /api/v2/databases/{database}/schemas/{schema}/image-repositories | Create an image repository
[**create_or_alter_image_repository**](ImageRepositoryApi.md#create_or_alter_image_repository) | **PUT** /api/v2/databases/{database}/schemas/{schema}/image-repositories/{name} | Create a (or alter an existing) image repository.
[**delete_image_repository**](ImageRepositoryApi.md#delete_image_repository) | **DELETE** /api/v2/databases/{database}/schemas/{schema}/image-repositories/{name} | Delete an image repository
[**fetch_image_repository**](ImageRepositoryApi.md#fetch_image_repository) | **GET** /api/v2/databases/{database}/schemas/{schema}/image-repositories/{name} | Fetch an image repository.
[**list_image_repositories**](ImageRepositoryApi.md#list_image_repositories) | **GET** /api/v2/databases/{database}/schemas/{schema}/image-repositories | List image repositories


# **create_image_repository**
> CreateImageRepository200Response create_image_repository(database, var_schema, image_repository, create_mode=create_mode)

Create an image repository

Create an image repository, with standard create modifiers as query parameters. See the ImageRepository component definition for what is required to be provided in the request body.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.image_repository._generated
from snowflake.core.image_repository._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.image_repository._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.image_repository._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.image_repository._generated.ImageRepositoryApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    image_repository = snowflake.core.image_repository._generated.ImageRepository() # ImageRepository | 
    create_mode = 'errorIfExists' # str |  (optional) (default to 'errorIfExists')

    try:
        # Create an image repository
        api_response = api_instance.create_image_repository(database, var_schema, image_repository, create_mode=create_mode)
        print("The response of ImageRepositoryApi->create_image_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageRepositoryApi->create_image_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **image_repository** | [**ImageRepository**](ImageRepository.md)|  | 
 **create_mode** | **str**|  | [optional] [default to &#39;errorIfExists&#39;]

### Return type

[**CreateImageRepository200Response**](CreateImageRepository200Response.md)

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

# **create_or_alter_image_repository**
> CreateImageRepository200Response create_or_alter_image_repository(database, var_schema, name, image_repository)

Create a (or alter an existing) image repository.

Create a (or alter an existing) . Even if the operation is just an alter, the full property set must be provided.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.image_repository._generated
from snowflake.core.image_repository._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.image_repository._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.image_repository._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.image_repository._generated.ImageRepositoryApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    image_repository = snowflake.core.image_repository._generated.ImageRepository() # ImageRepository | 

    try:
        # Create a (or alter an existing) image repository.
        api_response = api_instance.create_or_alter_image_repository(database, var_schema, name, image_repository)
        print("The response of ImageRepositoryApi->create_or_alter_image_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageRepositoryApi->create_or_alter_image_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **image_repository** | [**ImageRepository**](ImageRepository.md)|  | 

### Return type

[**CreateImageRepository200Response**](CreateImageRepository200Response.md)

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

# **delete_image_repository**
> CreateImageRepository200Response delete_image_repository(database, var_schema, name, if_exists=if_exists)

Delete an image repository

Delete an image repository with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.image_repository._generated
from snowflake.core.image_repository._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.image_repository._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.image_repository._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.image_repository._generated.ImageRepositoryApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 
    if_exists = False # bool |  (optional) (default to False)

    try:
        # Delete an image repository
        api_response = api_instance.delete_image_repository(database, var_schema, name, if_exists=if_exists)
        print("The response of ImageRepositoryApi->delete_image_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageRepositoryApi->delete_image_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 
 **if_exists** | **bool**|  | [optional] [default to False]

### Return type

[**CreateImageRepository200Response**](CreateImageRepository200Response.md)

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

# **fetch_image_repository**
> ImageRepository fetch_image_repository(database, var_schema, name)

Fetch an image repository.

Fetch an image repository using the SHOW command output.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.image_repository._generated
from snowflake.core.image_repository._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.image_repository._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.image_repository._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.image_repository._generated.ImageRepositoryApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    name = 'name_example' # str | 

    try:
        # Fetch an image repository.
        api_response = api_instance.fetch_image_repository(database, var_schema, name)
        print("The response of ImageRepositoryApi->fetch_image_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageRepositoryApi->fetch_image_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**ImageRepository**](ImageRepository.md)

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

# **list_image_repositories**
> List[ImageRepository] list_image_repositories(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit)

List image repositories

Lists the image repositories under the database and schema.

### Example

```python
from __future__ import print_function
import time
import os
import snowflake.core.image_repository._generated
from snowflake.core.image_repository._generated.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://org-account.snowflakecomputing.com
# See configuration.py for a list of all supported configuration parameters.
configuration = snowflake.core.image_repository._generated.Configuration(
    host = "https://org-account.snowflakecomputing.com"
)


# Enter a context with an instance of the API client
with snowflake.core.image_repository._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = snowflake.core.image_repository._generated.ImageRepositoryApi(api_client)
    database = 'database_example' # str | 
    var_schema = 'var_schema_example' # str | 
    like = 'like_example' # str |  (optional)
    starts_with = 'starts_with_example' # str |  (optional)
    show_limit = {'key': snowflake.core.image_repository._generated.ListImageRepositoriesShowLimitParameter()} # ListImageRepositoriesShowLimitParameter |  (optional)

    try:
        # List image repositories
        api_response = api_instance.list_image_repositories(database, var_schema, like=like, starts_with=starts_with, show_limit=show_limit)
        print("The response of ImageRepositoryApi->list_image_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageRepositoryApi->list_image_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **str**|  | 
 **var_schema** | **str**|  | 
 **like** | **str**|  | [optional] 
 **starts_with** | **str**|  | [optional] 
 **show_limit** | [**ListImageRepositoriesShowLimitParameter**](.md)|  | [optional] 

### Return type

[**List[ImageRepository]**](ImageRepository.md)

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
**500** | Internal Server Error. The server hit an unrecoverable system error. The response body may include the error code and message for further guidance. The application owner may need to reach out the customer support. |  -  |
**503** | Service Unavailable. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |
**504** | Gateway Timeout. The request was not processed due to server side timeouts. The application may retry with backoff. The jittered backoff is recommended. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

