# pylint: disable=C0103
"""A simple and basic use of requests module with http://www.google.com"""

import requests

def main():
    """main method to try out http requests and see response obj"""

    ### This should work with status 200 OK
    print("\n===== CASE: status 200 OK =====")
    response = requests.get("http://www.google.com", timeout=10)
    print("status code:", response.status_code)
    print("content type:", response.headers['Content-Type'])

    # uncomment to see some more contents of the response object
    # print("headers:", response.headers)
    # print("content:", response.text)

    ### This should fail with status 404
    print("\n===== CASE: status 404 NOT FOUND =====")
    response = requests.get("http://www.google.com/somerandomurl", timeout=10)
    print("status code:", response.status_code)
    print("content type:", response.headers['Content-Type'])


if __name__ == "__main__":
    main()
