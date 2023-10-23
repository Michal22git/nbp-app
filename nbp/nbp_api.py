import requests


class FetchAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def return_data(self, retries=0):
        if retries > 3:
            print(f"Max retries executed with failure")
            return None

        try:
            req = requests.get(
                self.endpoint,
                headers={
                    "Accept": "application/json"
                },
                timeout=10
            )

            return req.json()
        except requests.exceptions.Timeout:
            print(f"Timeout for {self.endpoint}. Retrying...")
            return self.return_data(retries + 1)
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return None
