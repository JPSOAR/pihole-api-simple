import requests

class PiHole:
    def __init__(self, base_url, api_token=None):
        self.base_url = base_url
        self.api_token = api_token

    def _make_request(self, params=None):
        url = f"{self.base_url}/admin/api.php"
        if params is None:
            params = {}
        if self.api_token:
            params['auth'] = self.api_token
        response = requests.get(url, params=params)
        response.raise_for_status()
        json_response = response.json()
        if json_response == []:
            raise Exception("No data returned from Pi-hole. Ensure you provided a valid API token when created the PiHole object.")
        else:
            return response.json()

    def enable(self):
        return self._make_request({'enable': ''})

    def disable(self, duration=None):
        params = {'disable': duration} if duration else {'disable': ''}
        return self._make_request(params)

    def get_versions(self):
        return self._make_request({'versions': ''})

    def set_temp_unit(self, unit):
        if unit not in ['f', 'c', 'k']:
            raise ValueError("Temperature unit must be 'f' or 'c' or 'k'")
        return self._make_request({'setTempUnit': unit})
    
    def get_domain_list(self, list_type):
        if list_type not in ['white', 'black','regex_black','regex_white']:
            raise ValueError("List type must be 'white', 'black', 'regex_black' or 'regex_white'")
        return self._make_request({'list': list_type})

    def update_domain_list(self, list_type, action, domain):
        params = {}
        if list_type not in ['white', 'black','regex_black','regex_white']:
            raise ValueError("List type must be 'white', 'black', 'regex_black' or 'regex_white'")
        else:
            params['list'] = list_type
        if action == 'add':
            params['add'] = domain
        elif action == 'sub':
            params['sub'] = domain
        else:
            raise ValueError("Invalid action. Must be 'add' or 'sub'")
        return self._make_request(params)

    def get_custom_dns(self):
        params = {'customdns': '', 'action': 'get'}
        return self._make_request(params)

    def update_custom_dns(self, action, domain, ip):
        if action not in ['add', 'delete']:
            raise ValueError("Invalid action. Must be 'add' or 'delete'")
        params = {
            'customdns': '', 
            'action': action,
            'domain': domain,
            'ip': ip
        }
        return self._make_request(params)

    def get_custom_cname(self):
        params = {'customcname': '', 'action': 'get'}
        return self._make_request(params)

    def update_custom_cname(self, action, domain, target):
        if action not in ['add', 'delete']:
            raise ValueError("Invalid action. Must be 'add' or 'delete'")
        params = {
            'customcname': '', 
            'action': action,
            'domain': domain,
            'target': target
        }
        return self._make_request(params)
