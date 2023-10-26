from time import sleep
from urllib.parse import urlencode
import requests
from vk_api import VKAPIClient
from yandex_api import (YAAPIClient)
import time

user_id = ''
token_vk = ''

def get_token():
    url = 'https://oauth.vk.com/authorize'
    params = {
        'client_id': '51775885',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'response_type': 'token',
        'scope': 'photos, status'
    }
    response = f'{url}?{urlencode(params)}'
    return response


def autorize_ya():
    print("Нужно авторизоваться в Яндекс")
    token_ya = input("Введите токен: ")
    client_ya = YAAPIClient(token_ya)
    return client_ya


def main():
    print('Добро пожаловать в программу.')
    print("----------------------------")
    # Для отладки все токены и id жестко прописываются.
    # user = int(input('Введите use_id: '))

    print(f'Подключаемся к аккаунту {user_id}')
    vk_client = VKAPIClient(token_vk, user_id)
    client = autorize_ya()
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
                      '0 - Выход в главное меню'
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
            while True:
                print('\n'
                      '1 - Посмотреть инфо \n'
                      '2 - Сохранить на Яндекс.Диск \n'
                      '0 - Выход в главное меню'
                      '\n')
                photo = int(input('Ваш выбор: '))
                if photo == 1:
                    for item in list_photo:
                        name_file = item.get('name')
                        date_file = item.get('date')
                        time_str = time.localtime(date_file)
                        time_string = time.strftime("%m-%d-%Y", time_str)
                        print(f'Имя файла: {name_file}',
                              f'Дата создания: {time_string}')
                elif photo == 2:
                    name_dir = input('Введите имя папки для сохранения: \n'
                                     'или "info" для просмотра содержимого диска \n'
                                     '0 - для выхода в подменю')
                    if name_dir == 'info':
                        client.get_info_disk()
                    elif name_dir == 0:
                        break
                    else:
                        client.create_dir(name_dir)
                        # client.upload_file()
                elif photo == 0:
                    break

        elif action == 4:
            while True:
                print('Что будем делать? \n'
                      '1 - Инфо диска \n'
                      '2 - Просмотр содержимого диска \n'
                      '3 - Новая папка \n'
                      '4 - Сохранение фотографий на Диск \n'
                      '0 - Выход в главное меню')
                look_disk = int(input('Ваш выбор: '))
                if look_disk == 1:
                    inform = client.get_info_disk()
                    print(inform)
                    input('Нажмите Enter для продолжения')
                elif look_disk == 2:
                    print('Корневой каталог "/" \n'
                          'С него принято начинать просмотр.')
                    direct_name = input('Введите имя каталога ')
                    print(client.list_dir(direct_name))
                    input('Нажмите Enter для продолжения')
                elif look_disk == 3:
                    new_dir = input('Введите имя папки: ')
                    print(client.create_dir(new_dir))
                    input('Нажмите Enter для продолжения ')
                elif look_disk == 0:
                    break

        elif action == 0:
            print('Завершение работы')
            sleep(1.5)
            break


if __name__ == '__main__':

    main()


    #print(list_photo)
    # client = autorize_ya()
    # print(client.get_info_disk())
    # print(client.list_dir('/'))
    # print(client.upload_file('Разное', 'README.md'))

    # for nums, item in enumerate(list_photo):
    #     response = requests.get(item)
    #     if response.status_code == 200:
    #         with open('sample', 'wb') as f:
    #             f.write(response.content)
    #     with open('sample.jpg', 'rb') as file:
    #         client.upload_file('Image', file)


    # get_token()
