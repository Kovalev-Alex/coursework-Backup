import requests


class YAAPIClient:
    """
    Access to YandexDisk
    """
    Base_url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token):
        self.token = token

    def get_common_params(self):
        return {
            'path': '/'
        }

    def get_common_headers(self):
        return {
            'Authorization': self.token
        }

    def get_info_disk(self):
        """
        Отображает использование диска
        :return:
        """
        response = requests.get(self.Base_url, headers=self.get_common_headers())
        total_space = response.json()['total_space']/1024/1024/1024
        used_space = response.json()['used_space']/1024/1024/1024
        return (
            '--------------Использование диска------------ \n'
            f'Всего места: {round(total_space, 2)} Gb \n'
            f'Занято: {round(used_space, 2)} Gb \n'
            f'Свободно: {round(total_space - used_space, 2)} GB')

    def list_dir(self, target):
        """
        Отображает содержимое каталога.

        :param target: 'Dir' Корневой каталог - '/'
        :return:

        """
        list_dirs = []
        params = self.get_common_params()
        params.update({'path': target})
        list_dir = requests.get(self.Base_url + 'resources', params=params,
                                headers=self.get_common_headers())
        for item in list_dir.json().get('_embedded', {}).get('items', {}):
            list_dirs.append(item.get('name'))
        return ', '.join(list_dirs)

    def create_dir(self, directory):
        params = self.get_common_params()
        params.update({'path': directory})
        requests.put(self.Base_url + 'resources', params=params, headers=self.get_common_headers())
        return f'Папка {directory} создана'

    def upload_file(self, directory, file):
        """
        Загрузка файла на Яндекс. Диск
        :param directory: Директория загрузки
        :param file: Имя файла
        :return:
        """
        self.create_dir(directory)
        params = self.get_common_params()
        params.update({'path': f'{directory}/{file}'})
        response = requests.get(self.Base_url + 'resources/upload', params=params, headers=self.get_common_headers())
        url_to_upload = response.json().get('href')
        with open(file, 'rb') as f:
            response = requests.put(url_to_upload, files={'file': f})
        return f'Файл успешно загружен' if response.status_code == 201 else "Что-то пошло не так!"
