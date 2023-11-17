# http request http://localhost:1428/your_endpoint

import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:1428/your_endpoint'
    params = {'arg1': 'hello', 'arg2': 'world'}
    response = requests.get(url, params)
    print(response.text)