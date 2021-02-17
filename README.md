### *Поиск IT вакансий*

___

###### **Описание программы**

Скрипт собирает информацию с сайтов [https://hh.ru](https://hh.ru) и [https://www.superjob.ru](https://www.superjob.ru), получает список вакансий и выводит в консоль сравнительную таблицу с количеством вакансий по Москве за 30 дней и средней з/п.

___________________________
###### **Инструкция**
1. Установить python с оффициального сайта [https://www.python.org](https://www.python.org).
2. Поставить IDE для работы. Можно использовать стандартный интерпретатор, а можно скачать продвинутый [_PyCharm_](https://www.jetbrains.com/pycharm/).
3. Создать __виртуальное окружение__. Для его создания лучше всего подходит _Python Virtual Environments_. Прочитать о нем можно на [_официальной странице_](https://www.python.org/dev/peps/pep-0405/).
4. Скачать `все файлы из репозитория` в отдельную папку.
5. Зарегистрировать свое приложение на сайте [https://api.superjob.ru/info/](https://api.superjob.ru) для получения секретного ключа.
6. Создать проект в [_PyCharm_](https://www.jetbrains.com/pycharm/) или в ином интерпретаторе и создать файл `.env`. Внести в этот файл:
    ```
    TOKEN_SUPERJOB=Ваш секретный ключ.
   ``` 
7. Установить необходимые модули с помощью консольной команды:
```
pip install -r requirements.txt.
``` 
8. С помощью интерпритатора запустить файл `manage.py`.

___________________________
###### **Примечание**
1. _Количество поисковых запросов на [https://hh.ru](https://hh.ru) имеет ограничение в 2000, поэтому скрипт анализирует только первые 20 страниц_.