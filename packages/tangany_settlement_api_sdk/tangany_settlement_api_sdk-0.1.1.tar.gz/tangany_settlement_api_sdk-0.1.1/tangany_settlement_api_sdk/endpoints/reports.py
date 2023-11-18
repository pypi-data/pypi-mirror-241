import json, requests

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class Reports:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/reports"

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
    
    def create(self, id: str, type: str, format: str, ledger_id: str, date: str,
               schedule_mode: str = None, schedule_hour: str = None, schedule_minute: str = None) -> str: 
        payload = {}
        payload['id'] = id
        payload['format'] = format
        payload['parameters'] = {
            "ledgerId": ledger_id,
            "date": date
        }
        payload['type'] = type
    
        if schedule_mode is not None:
            payload['schedule'] = {
                "mode": schedule_mode,
                "hour": schedule_hour,
                "minute": schedule_minute
            }
        
        response = requests.post(self._base_url, json=payload, headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    def delete(self, id: str) -> str:    
        url = f"{self._base_url }/{id}"
        response = requests.delete(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)