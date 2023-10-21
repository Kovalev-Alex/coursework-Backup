import requests

class VKAPIClient:
    """
    The class provides access to the VK api through standard VK requests.
    Features:
    Getting user status.
    Getting user information.
    getting profile photos.
    setting the user status.
    """
    Base_url = 'https://api.vk.com/method'

    def __init__(self, token, user_ids):
        self.token = token
        self.user_id = user_ids

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.154'}

    def _build_url(self, api_method):
        return f'{self.Base_url}/{api_method}'

    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(
            self._build_url('status.get'), params=params)
        return response.json().get('response', {}).get('text')

    def set_status(self, new_status):
        params = self.get_common_params()
        params.update({'user_id': self.user_id, 'text': new_status})
        response = requests.get(
            self._build_url('status.set'), params=params)
        response.raise_for_status()

    def replace_status(self, target, replace_string):
        status = self.get_status()
        new_status = status.replace(target, replace_string)
        self.set_status(new_status)

    def users_info(self):
        params = self.get_common_params()
        response = requests.get(
            self._build_url('users.get'), params=params)
        return response.json()

    def get_photos(self):
        params = self.get_common_params()
        params.update({'owner_id': self.user_id,
                       'album_id': 'profile'})
        response = requests.get(
            self._build_url('photos.get'), params=params)
        return response.json()
