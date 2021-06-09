# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

import requests


def create_folder_yadisc():
    token = ''
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    folder_name = 'New_photos'
    params = {'path': folder_name, 'overwrite': 'true'}
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }
    response = requests.put(upload_url, headers=headers, params=params)
    if response.status_code == 201:
        print(f'Папка "{folder_name}" создана в Вашем Яндекс.Диске.\n')
    else:
        print('response not 201')
    return response.status_code


def check_folders_list_yadisc():
    token = ''
    check_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=New_photos'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.get(check_url, headers=headers)
    if response.status_code == 200:
        print('response 200 ok')
    else:
        print('response not 200')
    return response.status_code


class TestYandexDiscApiPytest:

    def setup(self):
        print("method setup")

    def test_create_folder_yadisc_api_true(self):
        assert create_folder_yadisc() == 201

    def test_create_folder_yadisc_api_false(self):
        assert create_folder_yadisc() != 201

    def test_check_folders_list_yadisc_api_true(self):
        assert check_folders_list_yadisc() == 200

    def test_check_folders_list_yadisc_api_false(self):
        assert check_folders_list_yadisc() >= 200

    def teardown(self):
        print("method teardown")
