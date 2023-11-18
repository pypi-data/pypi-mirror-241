import requests

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class Accounts:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/accounts"

    def list(self, next_page_token: str = None, limit: str = "100", sort: str = None) -> str:
        params = {}
        params['limit'] = limit

        if sort is not None:
            params['sort'] = sort

        if next_page_token is not None:
            params['pageToken'] = next_page_token
        
        response = requests.get(url=self._base_url, headers=self._authenticator.get_base_header(), params=params)
        return return_or_raise(response)
    
    def get(self, id: str) -> str: 
        url = f"{self._base_url }/{id}"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    
    def create(self, id: str, label: str, type: str, customer_id: str = None, additionalAttributes: dict = None) -> str: 
        if type != "customer" and type != "internal" and type != "market_maker":
                raise Exception("account type must be one of the following: customer, market-maker or internal")  

        payload = {}
        payload["id"] = id
        payload["label"] = label
        payload["type"] = type
    
        if type == "customer" and customer_id == None:
            raise Exception("customer_id is required for account type customer")          
        
        if customer_id != None:
            payload["customerId"] = customer_id
              
        if additionalAttributes != None:
            payload["additionalAttributes"] = additionalAttributes    

        response = requests.post(self._base_url, json=payload, headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    def update(self, id: str, op: str, path: str, value: str) -> str:
        url = f"{self._base_url }/{id}"        
        payload = {}
        payload["op"] = op
        payload["path"] = path
        payload["value"] = value

        headers = self._authenticator.get_base_header()
        headers["Content-Type"] = "application/json-patch+json"
        response = requests.patch(url=url, json=[payload], headers=headers)
        return return_or_raise(response)
        
    
    def delete(self, id: str) -> str:    
        url = f"{self._base_url }/{id}"
        response = requests.delete(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)