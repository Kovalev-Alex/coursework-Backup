from time import sleep
from urllib.parse import urlencode
import os
import requests
from vk_api import VKAPIClient
from yandex_api import (YAAPIClient)


# user_id =


if __name__ == '__main__':
    print('Добро пожаловать в программу.')
    print("----------------------------")
    user = int(input('Введите use_id: '))
    TOKEN_VK = os.environ['APIVK']
    print(f'Подключаемся к аккаунту {user}')
    vk_client = VKAPIClient(TOKEN_VK, user)

    info = vk_client.users_info()
    name = info.get('name')
    last_name = info.get('last_name')
    ids = info.get('ID')
    print(f'Приветствую, {name} {last_name}')
    sleep(1)
    while True:
        print('----------------------')
        print('Что интересует?')
        print('1 - Информация ВК \n'
              '2 - Статус ВК \n'
              '3 - Фотографии ВК \n'
              '4 - Яндекс.Диск \n'
              '0 - Выход из программы.')
        action = int(input('Ваш выбор: '))
        if action == 1:
            print('\n'
                  f'Имя: {name} \n'
                  f'Фамилия: {last_name} \n'
                  f'ID Профиля: {ids} \n'
                  f'Для продолжения нажмите Enter...'
                  '\n')
            input()
        elif action == 2:
            while True:
                print('\n'
                      '1 - Посмотреть статус \n'
                      '2 - Изменить статус \n'
                      '3 - Установить новый статус \n'
                      '0 - Выход из подменю'
                      '\n')
                status = int(input('Ваш выбор: '))
                if status == 1:
                    print('В данный момент Ваш статус: ')
                    print(vk_client.get_status())
                    input('Для продолжения нажмите Enter...')
                elif status == 2:
                    word = input('Какое слово в статусе меняем: ')
                    new_word = input('На что меняем: ')
                    vk_client.replace_status(word, new_word)
                elif status == 3:
                    new_status = input('Введите новый статус: ')
                    vk_client.set_status(new_status)
                    print("Новый статус установлен!")
                elif status == 0:
                    break
        elif action == 3:
            list_photo = vk_client.get_photos()
            print(list_photo)
            while True:
                print('\n'
                      '1 - Посмотреть инфо \n'
                      '2 - Сохранить на Яндекс.Диск \n'
                      '0 - Выход из подменю'
                      '\n')
                photo = int(input('Ваш выбор: '))
                if photo == 1:
                    for item in list_photo:
                        name_file = item.get('name')
                        date_file = item.get('date')
                        print(f'Имя файла: {name_file}'
                              f'Время создания: {date_file}')
                elif photo == 2:
                    print("Сначала нужно авторизоваться!")
                    TOKEN_YA = input("Введите токен: ")
                    client = YAAPIClient(TOKEN_YA)

            print(list_photo)





    # print(client.list_dir('/'))
    # print(client.upload_file('Image', 'VK_API.py'))
    # for nums, item in enumerate(list_photo):68
    #     response = requests.get(item)
    #     if response.status_code == 200:
    #         with open('sample', 'wb') as f:
    #             f.write(response.content)
    #     with open('sample.jpg', 'rb') as file:
    #         client.upload_file('Image', file)


    # def get_token():
    #     url = 'https://oauth.vk.com/authorize'
    #     params = {
    #         'client_id': '51775885',
    #         'redirect_uri': 'https://oauth.vk.com/blank.html',
    #         'response_type': 'token',
    #         'scope': 'photos, status'
    #     }
    #     response = f'{url}?{urlencode(params)}'
    #     print(response)


    # get_token()
