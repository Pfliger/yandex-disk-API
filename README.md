# Домашнее задание к лекции 9.«Работа с библиотекой requests, http-запросы»
## Задача №2
У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует [Полигон](https://yandex.ru/dev/disk/poligon/). Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.

Все ответы приходят в формате json;
Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
HOST: https://cloud-api.yandex.net:443

Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

Шаблон для программы
```
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')
```    
#Solution Made class, which can upload file to Yandex disk, and recursively get list of files on disk. This class also understand error codes and exceptions that can be raised during network connections and JSON parsing.
If you have no Yandex token pls get it on https://yandex.ru/dev/disk/poligon/