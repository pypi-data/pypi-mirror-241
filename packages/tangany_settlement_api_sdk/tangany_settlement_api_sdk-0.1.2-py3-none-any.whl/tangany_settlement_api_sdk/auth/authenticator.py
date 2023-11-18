import json, requests, urllib3, time, logging
from datetime import datetime
from .credentials import Credentials

urllib3.disable_warnings()

class Authenticator:    
    credentials: Credentials
    valid_until: int
    token: str

    def __init__(self, credentials: Credentials):
        self.credentials = credentials         
        self.valid_until = 0
        self.token = ""

    def get_token(self) -> str:
        if not self.is_valid():
            self._refresh_token()

        return self.token 
    
    def is_valid(self) -> bool:
        now_unix = self._to_unix(datetime.now())
        tolerance = 60

        return self.valid_until > now_unix + tolerance

    def get_base_header(self) -> dict[str, str]:
        return {
            "tangany-version": "2",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "bearer " + self.get_token()
        }   
    
    def _refresh_token(self):
        logging.info("Refreshing token")    
    
        token_req_payload = {
            'grant_type': 'client_credentials',
            'client_id': self.credentials.client_id,
            'client_secret': self.credentials.client_secret,
            'scope': self.credentials.scope
        }

        token_response = requests.post(self.credentials.auth_server_url, 
                                       data=token_req_payload, 
                                       verify=False, 
                                       allow_redirects=False, 
                                       auth=(self.credentials.client_id, self.credentials.client_secret))
                    
        if token_response.status_code !=200:
            raise ConnectionRefusedError("Authentication failed: " + str(json.loads(token_response.text)))

        token_response_json = json.loads(token_response.text)
        self._set_valid_until_from_response(token_response_json)
        self.token = token_response_json['access_token']
    
    def _set_valid_until_from_response(self, token_response_json: str):
        now_unix = self._to_unix(datetime.now())
        expires_in = int(token_response_json['expires_in'])
        self.valid_until = now_unix + expires_in

    def _to_unix(self, datetime: datetime) -> int:
        return int(time.mktime(datetime.timetuple()))
