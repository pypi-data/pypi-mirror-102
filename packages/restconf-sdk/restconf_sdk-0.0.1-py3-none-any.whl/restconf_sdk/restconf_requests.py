import requests
from requests.auth import HTTPBasicAuth

HEADERS = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}


def make_request(device, url: str, body=None, method: str = 'GET'):
    """
    device -> IOSXEDevice
    body -> a dictionary or a list
    method -> str
    """
    method = method.strip().upper()
    auth = HTTPBasicAuth(device.username, device.password)

    if method not in ['GET', 'POST', 'PUT', 'PATCH']:
        raise Exception("method must be part of: GET, POST, PUT or PATCH")

    requests.packages.urllib3.disable_warnings()
    if method == 'GET':
        return requests.get(url, auth=auth, headers=HEADERS, verify=False)

    elif method == 'POST':
        return requests.post(url, auth=auth, headers=HEADERS, json=body, verify=False)

    elif method == 'PATCH':
        return requests.patch(url, auth=auth, headers=HEADERS, json=body, verify=False)

    elif method == 'PUT':
        return requests.put(url, auth=auth, headers=HEADERS, json=body, verify=False)
