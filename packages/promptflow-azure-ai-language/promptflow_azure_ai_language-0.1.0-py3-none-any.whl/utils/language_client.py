import requests 
import os 
import time 
from utils.mode import Mode

DEFAULT_TIMEOUT = int(os.environ.get("DEFAULT_TEST_TIMEOUT", "60"))

# Client class to connect to and call Azure AI Language APIs:
class LanguageClient():

    # Initializes client: must pass in API key, endpoint, and inter-path:
    def __init__(self, endpoint, api_key, inter_path, region=None, cert=None, session:requests.Session=None):
        self.endpoint = endpoint
        self.region = region
        self.inter_path = inter_path  
        self.cert = cert              
        self.api_key = api_key        
        self.session = session 

    # Obtains headers for API request:
    def get_headers(self):
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/json"
        }
        if self.region:
            headers["Ocp-Apim-Subscription-Region"] = self.region
        return headers

    # Synchronous API request:
    def run_sync_endpoint(self, json_obj, request_path, method="post"):
        url = self.endpoint + self.inter_path + request_path 
        headers = self.get_headers()

        session = requests.Session() if self.session is None else self.session 
        response = session.request(method=method, url=url, headers=headers, json=json_obj, cert=self.cert)

        return response
    
    # Asyncrhonous API request:
    def run_async_endpoint(self, json_obj, request_path, method="post", timeout=DEFAULT_TIMEOUT, sleep_time=5):
        url = self.endpoint + self.inter_path + request_path 
        headers = self.get_headers()
        session = requests.Session() if self.session is None else self.session 
        response = session.request(method=method, url=url, headers=headers, json=json_obj, cert=self.cert)

        try:
            response.raise_for_status()
        except requests.HTTPError:
            return response

        # Poll until completion of job:
        status_url = response.headers["Operation-Location"]
        start = time.time()
        while(True):
            if time.time() - start > timeout:
                print(response)
                print(response.content.decode(response.encoding or "utf-8"))
                print(response.headers)
                raise TimeoutError("Operation timed out")

            response = session.get(url=status_url, headers=headers, cert=self.cert)
            try:
                response.raise_for_status()
                json_res = response.json()
                status = json_res["status"]
                if status == "succeeded" or status == "failed":
                    break
            except requests.HTTPError:
                pass

            time.sleep(sleep_time)

        return response
    
    # Run either sync or async endpoint.
    def run_endpoint(self, json_obj, request_path, mode:Mode):
        if mode == Mode.SYNC:
            return self.run_sync_endpoint(json_obj=json_obj, request_path=request_path)
        else: 
            return self.run_async_endpoint(json_obj=json_obj, request_path=request_path)
        