from http.client import responses
import requests

TOKEN = '' # Место для ввода Яндекс токена


class YaUploader:
    def __init__(self, token: str):
        self.TOKEN = {'Authorization': 'OAuth ' + token}
        self.HOST_API = 'https://cloud-api.yandex.net:443'
        self.UPLOAD_LINK = '/v1/disk/resources/upload'
        self.FILES_LIST = '/v1/disk/resources/files'

    def upload(self, file_path: str):
        upload_link = requests.get(self.HOST_API + self.UPLOAD_LINK, params={'path': file_path}, headers=self.TOKEN)
        if upload_link.status_code != requests.codes.ok:
            return f'\nОшибка при получении URL. Код: ' \
                   f'{upload_link.status_code} ({responses[upload_link.status_code]})'
        files = {'file': open(file_path, 'rb')}
        request = requests.put(upload_link.json()['href'], params={'path': file_path}, files=files)
        if not (200 <= request.status_code < 300):
            return f'\nОшибка при загрузке файла. Код: ' \
                   f'{request.status_code} ({responses[request.status_code]})'
        return f'\nФайл загружен. Код: {request.status_code} ({responses[request.status_code]})'

    def file_list (self):
        result = []
        request = requests.get(self.HOST_API + self.FILES_LIST, headers=self.TOKEN)
        if not (200 <= request.status_code < 300):
            return [f'\nОшибка при получении списка файлов. Код: '
                    f'{request.status_code} ({responses[request.status_code]})']
        result += [f'({x["name"]} ({str(int(x["size"] / 1024))} kB )' for x in request.json()['items']]
        return result


uploader = YaUploader(TOKEN)
print(uploader.upload('fox.gif'))
print('\nФайлы на Яндекс Диске:')
print(uploader.file_list())
