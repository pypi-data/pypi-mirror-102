
from restconf_sdk.restconf_requests import make_request


class IOSXEDevice:
    def __init__(self, hostname, username, password, port=None, https=True):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

        if https:
            self.https = "https"
        else:
            self.https = "http"

        if port:
            self.path = f"{self.https}://{self.hostname}:{self.port}"
        else:
            self.path = f"{self.https}://{self.hostname}"

    def get_version(self):
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/version"
        response = make_request(self, url)
        json_response = response.json()
        return json_response

    def get_configs(self):
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native"
        response = make_request(self, url)
        json_response = response.json()
        return json_response

    def get_hostname(self):
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/hostname"
        response = make_request(self, url)
        json_response = response.json()
        return json_response["Cisco-IOS-XE-native:hostname"]

    def get_all_interfaces(self):
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/interface"
        response = make_request(self, url)
        json_response = response.json()
        return json_response["Cisco-IOS-XE-native:interface"]

    def get_single_interface(self, interface_type, interface_name):
        # If the interface you are trying to get is GigabitEthernet1,
        # then the interface_type will be "GigabitEthernet" and interface_name will be "1"
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}={interface_name}"
        response = make_request(self, url)
        json_response = response.json()
        return json_response

    def bring_interface_up(self, interface_type, interface_name):
        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}"
        body = {f"Cisco-IOS-XE-native:{interface_type}": {'name': interface_name, 'shutdown': [None]}}
        response = make_request(self, url, body=body, method="PATCH")
        return response

    def edit_interface_details(self, interface_type: str, interface_name: str, **interface_details):
        """
        This is used when we want to edit a specific interface. For example, if we want to edit the interface
        GigabitEthernet1:

        edit_interface_details(
            device, "GigabitEthernet", "1",
            description='this rocks', primary_ip_address={'ip': '10.10.40.10', 'mask': '255.255.255.0'}
        )
        """
        new_interface_details = {'name': interface_name}

        if 'description' in interface_details:
            new_interface_details['description'] = interface_details['description']

        if 'primary_ip_address' in interface_details:
            address = interface_details['primary_ip_address']['ip']
            mask = interface_details['primary_ip_address']['mask']
            address = {
                "address": {"primary": {
                    "address": address,
                    "mask": mask
                }}}
            new_interface_details["ip"] = address

        body = {f"Cisco-IOS-XE-native:{interface_type}": new_interface_details}

        url = f"{self.path}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}"
        response = make_request(self, url, body=body, method="PATCH")

        if response.status_code == 204:
            return True
        elif response.status_code == 500:
            return response.json()
