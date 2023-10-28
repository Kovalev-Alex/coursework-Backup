from tqdm import tqdm
import requests
from time import sleep


class VKAPIClient:
    """
    Класс предоставляет доступ к VK api через стандартные запросы VK.
    Возможности:
    Получение статуса пользователя.
    Изменение статуса пользователя.
    Получение информации о пользователе.
    Получение фотографий профиля.
    Установка нового статуса пользователя.
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
        """
        Возвращает Статус пользователя ВК

        :return:
        """
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(
            self._build_url('status.get'), params=params)
        return response.json().get('response', {}).get('text')

    def set_status(self, new_status):
        """
        Устанавливает новый статус пользователя ВК

        :param new_status:
        :return:
        """
        params = self.get_common_params()
        params.update({'user_id': self.user_id, 'text': new_status})
        response = requests.get(
            self._build_url('status.set'), params=params)
        response.raise_for_status()

    def replace_status(self, target, replace_string):
        """
        Позволяет заменить слово в статусе ВК.

        :param target:
        :param replace_string:
        :return:
        """
        status = self.get_status()
        new_status = status.replace(target, replace_string)
        self.set_status(new_status)

    def users_info(self):
        """
        Возвращает информацию о пользователе.
        :return:
        Имя:\n
        Фамилия:\n
        ID:
        """
        params = self.get_common_params()
        response = requests.get(
            self._build_url('users.get'), params=params)
        name = response.json().get('response', {})[0].get('first_name')
        last_name = response.json().get('response', {})[0].get('last_name')
        ids = response.json().get('response', {})[0].get('id')
        return {'name': name, 'last_name': last_name, 'ID': ids}

    def get_photos_list(self):
        """
        Запрос фотографий профиля.
        Возвращает список фотографий размера 'w'
        :return:
        """
        photos = []
        params = self.get_common_params()
        params.update({'owner_id': self.user_id,
                       'album_id': 'profile',
                       'extended': 1})
        response = requests.get(
            self._build_url('photos.get'), params=params)
        list_photos = response.json().get('response', {}).get('items')
        print(f'В данное время у Вас {len(list_photos)} фотографий.')
        while True:
            count = int(input('Сколько фотографий будем сохранять?: '))
            if count > len(list_photos):
                print('У Вас нет столько фотографий. Будьте скромнее. :)')
                continue
            else:
                for item in tqdm(list_photos[:count]):
                    sleep(0.1)
                    likes = item.get('likes').get('count')
                    data = item.get('date')
                    for size in item.get('sizes', {}):
                        if size['type'] == 'w':
                            photos.append({'name': str(likes) + '.jpeg',
                                           'likes': likes,
                                           'date': data,
                                           'url': size.get('url')})

            return photos

    def get_content(self, url):
        params = self.get_common_params()
        response = requests.get(url, params=params)
        with open('file.jpeg', 'wb') as f:
            f.write(response.content)
        return f
