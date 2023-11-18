
from typing import Any
import requests

def return_or_raise(response: requests.Response) -> Any:        
    responseJson = response.json()
    if response.status_code == 200:
        return responseJson
    else:
        raise Exception(str(responseJson))