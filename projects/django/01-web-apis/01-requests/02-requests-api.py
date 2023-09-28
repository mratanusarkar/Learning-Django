# pylint: disable=C0103
"""Explore the use of REST API HTTP Requests with https://exchangeratesapi.io/"""

import requests

def main():
    """main method to try out exchange-rates-api endpoints"""

    BASE_URL = "https://api.exchangeratesapi.io/latest"
    body = {
        "base": "USD",
        "symbols": "GBP"
    }

    # requests methods can be: GET, POST, PUT, DELETE, etc...
    res = requests.get(BASE_URL, params=body, timeout=10)
    print("status code:", res.status_code)
    print("content type:", res.headers['Content-Type'])

    if res.status_code == 200:
        data = res.json()
        print("res json data:", data)
    else:
        print("error! no data")
        raise Exception("There was an error!")  # pylint: disable=W0719


if __name__ == "__main__":
    main()
