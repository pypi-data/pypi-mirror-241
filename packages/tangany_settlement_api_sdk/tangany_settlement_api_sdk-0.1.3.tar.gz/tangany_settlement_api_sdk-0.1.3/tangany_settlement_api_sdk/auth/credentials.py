class Credentials:
    client_id: str
    client_secret: str
    base_url: str
    scope: str
    auth_server_url: str

    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://api.tangany.com/settlement", auth_server_url: str =  "https://auth.tangany.com/2.0", scope: str = "https://auth.tangany.com/settlement/.default"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self. auth_server_url = auth_server_url
        self.scope = scope