from time import sleep
import requests
from tqdm import tqdm
from vk_api import VKAPIClient
from yandex_api import (YAAPIClient)
import time


user_id = ''
token_vk = ''
token_ya = ''


def main():
    print('Добро пожаловать в программу.')
    print("----------------------------")
    print(f'Подключаемся к аккаунту {user_id}')
    vk_client = VKAPIClient(token_vk, user_id)
    client = YAAPIClient(token_ya)
    info = vk_client.users_info()
    name = info.get('name')
    last_name = info.get('last_name')
    ids = info.get('ID')
    sleep(1)
    while True:
        print('----------------------')
        print('Что интересует?')
        print('1 - Информация ВК \n'
              '2 - Статус ВК \n'
              '3 - Информация о фотографиях ВК \n'
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
            list_photo = vk_client.get_photos_list()
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
                                     '0 - для выхода в подменю \n')
                    if name_dir == 'info':
                        print(client.list_dir('/'))
                    elif name_dir == 0:
                        break
                    else:
                        client.create_dir(name_dir)
                        for file in tqdm(list_photo):
                            get_content = requests.get(file.get('url')).content
                            with open(file.get('name'), 'wb') as f:
                                f.write(get_content)
                                client.upload_file(name_dir, file.get('name'))
                elif photo == 0:
                    break
        elif action == 4:
            while True:
                print('Что будем делать? \n'
                      '1 - Инфо диска \n'
                      '2 - Просмотр содержимого диска \n'
                      '3 - Новая папка \n'
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
