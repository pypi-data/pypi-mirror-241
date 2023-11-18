import requests

from attr import define
from ..auth import Authenticator
from .response_handler import return_or_raise

@define
class ReportResults:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/reports/"

    def list(self, report_id: str) -> str:        
        url = f"{self._base_url}/{report_id}/results"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    def get(self, report_id: str, result_id: str) -> str: 
        url = f"{self._base_url}/{report_id}/results/{result_id}"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())

        if response.headers["content-type"] == 'text/csv':                
            decoded_response = response.content.decode('utf-8')
            return decoded_response
        else:
            return return_or_raise(response)