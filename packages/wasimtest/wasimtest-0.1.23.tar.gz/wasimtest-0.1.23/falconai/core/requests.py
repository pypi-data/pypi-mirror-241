import httpx
from ..config import config

async def request_endpoint(endpoint_name, **kwargs):
    endpoint = config.get_endpoint_data(endpoint_name)
    if not endpoint:
        raise ValueError(f"No configuration found for endpoint: {endpoint_name}")

    method = endpoint['method']
    url = endpoint['url']
    headers = endpoint['headers']
    param_definitions = endpoint['params']
    data = extract_fields(endpoint["body"], **kwargs)
    
    
     # Build params based on what's actually passed in kwargs
    params = {param: kwargs[param] for param in param_definitions if param in kwargs}

    
    # if params:
    #     query_string = '&'.join([f"{key}={kwargs.get(key, '')}" for key in params])
    #     url = f"{url}?{query_string}"
        
    response = await make_request(method, url, headers, data, params)
    return response.json()

async def make_request(method, url, headers=None, data=None, params=None):
    # Using a try-except block to handle exceptions
    try:
        async with httpx.AsyncClient() as client:
            if method == 'POST':
                response = await client.post(url, headers=headers, params=params, json=data)
            elif method == 'GET':
                # Including params for GET request
                response = await client.get(url, headers=headers, params=params)
            elif method == 'PUT':
                # Including json data for PUT request
                response = await client.put(url, headers=headers, params=params, json=data)
            elif method == 'DELETE':
                # DELETE requests might not need a body, but including for completeness
                response = await client.delete(url, headers=headers, json=data, params=params)
            elif method == 'PATCH':
                # Including json data for PATCH request
                response = await client.patch(url, headers=headers, json=data, params=params)
            else:
                raise ValueError("Invalid HTTP method provided.")

            # Handling the response
            response.raise_for_status()  # Will raise an exception for 4XX/5XX status codes
            return response.json()

    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        # Depending on the use case, you might want to re-raise the exception
        # or handle it differently, e.g., return an error message or None.
        return None

    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
        # Similar to above, the exception can be re-raised or handled as needed.
        return None

def extract_fields(fields, **kwargs):
    data = {}
    for field, value in fields.items():
        if isinstance(value, dict):
            data[field] = extract_fields(value, **kwargs)
        else:
            data[field] = kwargs.get(field, None)
    return data

