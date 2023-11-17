def extract_conn_kwargs(params: set, target: dict) -> dict:
    """
    Description:
    Extracts the connection parameters from the given keywords argument 
    and returns a dictionary containing the connection parameters.

    Parameters:
    params (set): A set of connection parameters.
    target (dict): A dictionary containing the connection parameters.

    Returns:
    dict: A dictionary containing the connection parameters.

    Example: >>> extract_conn_kwargs({"url", "dialect", "username", "password", "host", "port", "database"},
    {"url": "https://www.google.com", "dialect": "postgresql", "username": "postgres", "password": "postgres",
    "host": "localhost", "port": "26257", "database": "postgres"}) {"url": "https://www.google.com", "dialect":
    "postgresql", "username": "postgres", "password": "postgres", "host": "localhost", "port": "26257", "database":
    "postgres"}
    """
    # return {key: target[key] for key in params if key in target}
    result = {}
    for p in params:
        if p in target:
            result[p] = target[p]
    return result
