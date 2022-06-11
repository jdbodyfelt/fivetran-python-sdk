"""
Built from https://fivetran.com/docs/rest-api/connectors
"""
#/**********************************************/
from auth import Auth

defaults = {
    'auth': Auth(), 
    'roles': [
        'Account Administrator', 
        'Account Billing', 
        'Account Analyst', 
        'Account Reviewer', 
        'Destination Creator'
    ]
}

#/**********************************************/

class Connectors:

    def __init__(self, auth: Auth = defaults['auth'], roles: list = defaults['roles']):
        self.req = auth
        self.roles = roles

    def types(self):
        cursor = "START"
        url = 'metadata/connectors-types'
        result = []
        while cursor: 
            cursor = None
            response = self.req.get(url, params={'cursor': cursor})
            if response['Code'] == 'Success':
                result.append(response['data']['items'])
                cursor = response['next_cursor']
        return result

    