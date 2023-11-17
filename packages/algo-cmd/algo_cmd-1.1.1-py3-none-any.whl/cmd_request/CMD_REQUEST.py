import requests
from requests.adapters import HTTPAdapter, Retry


class REQUEST:
    def __init__(self):
        self.http_strategy = Retry(total=5, backoff_factor=1,
                                   status_forcelist=[500, 502, 503, 504])
        self.http_adapter = HTTPAdapter(max_retries=self.http_strategy)

    def gen_client(self):
        with requests.Session() as an_session:
            an_session.mount("http://", self.http_adapter)
            an_session.mount("https://", self.http_adapter)
            return an_session
