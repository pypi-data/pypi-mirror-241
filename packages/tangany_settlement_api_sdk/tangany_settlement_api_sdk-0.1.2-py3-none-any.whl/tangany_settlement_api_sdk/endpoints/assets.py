import requests

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class Assets:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/assets"
    
    def list(self) -> str:
        response = requests.get(url=self._base_url, headers=self._authenticator.get_base_header())
        responseJson = return_or_raise(response)
        return responseJson
    
    def get(self, id: str) -> str: 
        url = f"{self._base_url }/{id}"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)