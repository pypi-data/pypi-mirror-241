from ..core.requests import request_endpoint

async def chat(**kwargs):
    result = await request_endpoint("chat", **kwargs)
    return result

async def models_get(**kwargs):
    result = await request_endpoint("models_get", **kwargs)
    return result

async def model_delete(**kwargs):
    result = await request_endpoint("model_delete", **kwargs)
    return result

async def model_patch(**kwargs):
    result = await request_endpoint("model_patch", **kwargs)
    return result

async def model_post(**kwargs):
    """
    Creates a new model in the FalconAI service.

    Args:
        model_name (str): Name of the model.
        model_type (str): Type of the model, could be 'base'.
        version (str): Version of the model.
        year (int): Year of the model release.
        dataset_size (str): Size of the dataset used.
        provider (str): Provider of the model.
        modality (str): Modality of the model.
        max_tokens (str): Maximum tokens that the model can handle.
        description (str): Description of the model.
        model_attributes (str): Attributes of the model.

    Returns:
        The response from the FalconAI service.
    """
    
    result = await request_endpoint("model_post", **kwargs)
    return result