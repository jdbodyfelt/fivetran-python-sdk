"""
Built from https://fivetran.com/docs/rest-api/groups
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

class Groups:

    def __init__(self, auth: Auth = defaults['auth'], roles: list = defaults['roles']):
        self.req = auth
        self.roles = roles

    def create(self, name: str):
        return self.req.post('groups', data={'name': name})

    def list(self):
        return self.req.get('groups')

    def about(self, group_id: str):
        return self.req.get(f'groups/{group_id}')

    def modify(self, group_id: str, name: str):
        return self.req.patch(f'groups/{group_id}', data={'name': name})

    def list_connectors(self, group_id: str):
        return self.req.get(f'groups/{group_id}/connectors')

    def list_users(self, group_id: str):
        return self.req.get(f'groups/{group_id}/users')

    def add_user(self, group_id: str, email: str, role: str):
        if role not in self.roles:
            raise ValueError(f'Invalid role: {role}')
        data = {'email': email, 'role': role}
        return self.req.post(f'groups/{group_id}/users')

    def remove_user(self, group_id: str, user_id: str):
        return self.req.delete(f'groups/{group_id}/users/{user_id}')

    def delete(self, group_id: str):
        return self.req.delete(f'groups/{group_id}')