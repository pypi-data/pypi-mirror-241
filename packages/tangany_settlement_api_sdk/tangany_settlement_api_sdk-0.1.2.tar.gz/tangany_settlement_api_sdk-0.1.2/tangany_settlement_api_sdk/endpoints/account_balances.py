import json, requests

from attr import define

from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class AccountBalances:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator  
        self._base_url = f"{authenticator.credentials.base_url}/ledgers"
    
    def list(self, ledger_id: str, valuta_date: str = None, next_page_token: str = None, limit: str = "100") -> str:
        url = f"{self._base_url}/{ledger_id}/balances/accounts"
        params = {}
        params['limit'] = limit

        if valuta_date is not None:
            params['date'] = valuta_date

        if next_page_token is not None:
            params['pageToken'] = next_page_token
        
        response = requests.get(url=url, headers=self._authenticator.get_base_header(), params=params)
        responseJson = return_or_raise(response)
        return responseJson   

    def get(self, ledger_id: str, account_id: str, valuta_date: str = None) -> str:
        url = f"{self._base_url}/{ledger_id}/balances/accounts/{account_id}"

        if valuta_date is not None:
            url = f"{url}?date={valuta_date}"

        response = requests.get(url=url, headers=self._authenticator.get_base_header())        

        responseJson = return_or_raise(response)
        return responseJson    