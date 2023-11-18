import requests

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class AssetBalances:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator  
        self._base_url = f"{authenticator.credentials.base_url}/ledgers"

    def get(self, ledger_id: str, valuta_date: str = None) -> str:
        url = f"{self._base_url}/{ledger_id}/balances/assets"

        if valuta_date is not None:
            url = f"{url}?date={valuta_date}"
            
        response = requests.get(url=url, headers=self._authenticator.get_base_header())        

        responseJson = return_or_raise(response)
        return responseJson    