"""
Built from https://fivetran.com/docs/rest-api/users
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
class Users:

    def __init__(self, auth: Auth = defaults['auth'], roles: list = defaults['roles']):
        self.req = auth
        self.roles = roles
        self.keys = [ "given_name", "family_name", "role", "phone", "picture" ]

    def list(self):
        return self.req.get('users')

    def invite(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.keys}
        return self.req.post('users', data=data)
    
    def modify(self, user_id: str, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.keys}
        return self.req.patch(f'users/{user_id}', data=data)
    
    def delete(self, user_id: str):
        return self.req.delete(f'users/{user_id}')
    
    '''
    Below are the beta and private preview endpoints.
    '''

    def list_roles(self, user_id: str):
        return self.req.get(f'users/{user_id}/connectors')
    
    def add_to_connector(self, user_id: str, connector_id: str):
        return self.req.post(f'users/{user_id}/connectors/{connector_id}')

    def assign_role(self, user_id: str, connector_id: str, role: str):
        if role not in self.roles: 
            raise ValueError(f'Invalid role: {role}')
        data = {'id': connector_id, 'role': role}
        return self.req.post(f'users/{user_id}/connectors', data=data)
    
    def update_role(self, user_id: str, connector_id: str, role: str):
        if role not in self.roles: 
            raise ValueError(f'Invalid role: {role}')
        data = {'role': role}
        url = f'users/{user_id}/connectors/{connector_id}'
        return self.req.patch(url, data=data)

    def delete_role(self, user_id: str, connector_id: str):
        url = f'users/{user_id}/connectors/{connector_id}'
        return self.req.delete(url)
   
    def delete_roles(self, user_id: str):
        return self.req.delete(f'users/{user_id}/role')

    def list_groups(self, user_id: str):
        return self.req.get(f'users/{user_id}/groups')
    
    def group(self, user_id: str, group_id: str):
        return self.req.get(f'users/{user_id}/groups/{group_id}')

    def add_to_group(self, user_id: str, group_id: str, role: str):
        data = {'id': group_id, 'role': role}
        return self.req.post(f'users/{user_id}/groups', data=data)
    
    def update_group_role(self, user_id: str, group_id: str, role: str):
        data = {'role': role}
        url = f'users/{user_id}/groups/{group_id}'
        return self.req.patch(url, data=data)
    
    def remove_group(self, user_id: str, group_id: str):
        return self.req.delete(f'users/{user_id}/groups/{group_id}')