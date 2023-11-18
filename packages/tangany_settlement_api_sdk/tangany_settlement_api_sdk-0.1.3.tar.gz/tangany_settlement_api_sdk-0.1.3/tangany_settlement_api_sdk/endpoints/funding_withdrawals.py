import requests, json

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class FundingWithdrawals:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator  
        self._base_url = f"{authenticator.credentials.base_url}/ledgers"

    def list(self, ledger_id: str, next_page_token: str = None, limit: str = "100", status: str = None, reference: str = None,
             value_date_before: str = None, value_date_after: str = None, 
             booking_date_before: str = None, booking_date_after: str = None) -> str:
        url = f"{self._base_url}/{ledger_id}/funding/withdrawals"
        params = {}
        params['limit'] = limit

        if next_page_token is not None:
            params['pageToken'] = next_page_token

        if value_date_before is not None:
            params['valueDateBefore'] = value_date_before   

        if value_date_after is not None:
            params['valueDateAfter'] = value_date_after 

        if booking_date_before is not None:
            params['bookingDateBefore'] = booking_date_before 

        if booking_date_after is not None:
            params['bookingDateAfter'] = booking_date_after   

        if reference is not None:
            params['reference'] = reference  

        if status is not None:
            params['status'] = status              

        response = requests.get(url=url, headers=self._authenticator.get_base_header(), params=params)
        responseJson = return_or_raise(response)
        return responseJson     
    
    
    def create(self, ledger_id: str, transaction_id: str, from_account_id: str, value: str, asset_id: str, fiat_currency: str, fiat_value: str,  txHash: str,
               value_date: str = None, reference: str = None) -> str: 
        url = f"{self._base_url}/{ledger_id}/funding/withdrawals"
        payload = {}
        payload['id'] = transaction_id
        payload['fromAccountId'] = from_account_id
        payload['value'] = value
        payload['assetId'] = asset_id
        payload['fiatCurrency'] = fiat_currency
        payload['fiatValue'] = fiat_value
        payload['txHash'] = txHash   
        
        if value_date is not None:
            payload['valueDate'] = value_date

        if reference is not None:
            payload['reference'] = reference
        
        response = requests.post(url=url, json=[payload], headers=self._authenticator.get_base_header())
        return return_or_raise(response)