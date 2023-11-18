import requests, json

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class Ledgers:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/ledgers"    
    
    def list(self, next_page_token: str = None, limit: str = "100") -> str:
        params = {}
        params['limit'] = limit

        if next_page_token is not None:
            params['pageToken'] = next_page_token
        
        response = requests.get(url=self._base_url, headers=self._authenticator.get_base_header(), params=params)
        return return_or_raise(response)
    
    def get(self, id: str) -> str: 
        url = f"{self._base_url }/{id}"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)    
    
    def create(self, id: str, label: str) -> str: 
        payload = {}
        payload['id'] = id
        payload['label'] = label        
        response = requests.post(self._base_url, json=payload, headers=self._authenticator.get_base_header())
        return return_or_raise(response)