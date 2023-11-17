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

    if response.get("error"):
        # Handle error
        print(f"Error: {response['error']}")
    else:
        # Process successful response
        data = response.get("data")
        
    return response

async def make_request(method, url, headers=None, data=None, params=None):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, headers=headers, json=data, params=params)

            # Check if the response is successful
            if response.status_code >= 400:
                # Return error information as a dictionary
                return {
                    "status_code": response.status_code,
                    "error": response.json() if response.content else response.text
                }

            # Return successful response
            return {"status_code": response.status_code, "data": response.json()}

    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        return {"status_code": 0, "error": str(e)}

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"status_code": 0, "error": str(e)}

def extract_fields(fields, **kwargs):
    data = {}
    for field, value in fields.items():
        if isinstance(value, dict):
            data[field] = extract_fields(value, **kwargs)
        else:
            data[field] = kwargs.get(field, None)
    return data

