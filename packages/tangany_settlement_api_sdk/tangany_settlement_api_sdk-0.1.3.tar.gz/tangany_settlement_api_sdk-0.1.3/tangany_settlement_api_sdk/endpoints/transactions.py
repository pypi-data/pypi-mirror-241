import json, requests

from attr import define
from .response_handler import return_or_raise
from ..auth import Authenticator

@define
class Transactions:
    _authenticator: Authenticator
    _base_url: str

    def __init__(self, authenticator: Authenticator):
        self._authenticator = authenticator
        self._base_url = f"{authenticator.credentials.base_url}/ledgers"

    def list(self, ledger_id: str, next_page_token: str = None, limit: str = "100", status: str = None, reference: str = None,  involving_account_id: str = None,
             value_date_before: str = None, value_date_after: str = None, 
             booking_date_before: str = None, booking_date_after: str = None) -> str:
        url = f"{self._base_url}/{ledger_id}/transactions"
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

        if involving_account_id is not None:
            params['involvingAccountId'] = involving_account_id  

        if reference is not None:
            params['reference'] = reference  

        if status is not None:
            params['status'] = status  

        response = requests.get(url=url, headers=self._authenticator.get_base_header(), params=params)
        responseJson = return_or_raise(response)
        return responseJson        

    def get(self, ledger_id: str, transaction_id: str) -> str: 
        url = f"{self._base_url}/{ledger_id}/transactions/{transaction_id}"
        response = requests.get(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    
    def create(self, ledger_id: str, transaction_id: str, from_account_id: str, to_account_id: str, value: str, value_date: str, asset_id: str, fiat_currency: str, fiat_value: str, 
               reference: str = None, trade_info_fill_date: str = None, trade_info_market_maker_tx_id: str = None) -> str: 
        url = f"{self._base_url}/{ledger_id}/transactions"
        payload = {}
        payload['id'] = transaction_id
        payload['fromAccountId'] = from_account_id
        payload['toAccountId'] = to_account_id
        payload['value'] = value
        payload['valueDate'] = value_date
        payload['assetId'] = asset_id
        payload['fiatCurrency'] = fiat_currency
        payload['fiatValue'] = fiat_value
        payload['reference'] = reference

        if trade_info_fill_date is not None or trade_info_market_maker_tx_id is not None:
            payload['tradeInfo'] = {
                "fillDate": trade_info_fill_date,
                "marketMakerTxId": trade_info_market_maker_tx_id
            }           
        
        response = requests.post(url=url, json=[payload], headers=self._authenticator.get_base_header())
        return return_or_raise(response)
    
    def delete(self, ledger_id: str, transaction_id: str) -> str: 
        url = f"{self._base_url}/{ledger_id}/transactions/{transaction_id}"
        response = requests.delete(url=url, headers=self._authenticator.get_base_header())
        return return_or_raise(response)