# Бэкэнд-сервер для интернет-магазина.
В этом бэкэнд-сервере присутствуют эндпонты __/categories__, __/subcategories__ и __/products__, с помощью которых  можно добавлять, редактировать, удалять и отображать категории, подкатегории и товары с возможностью пагинации.
### Инструкция по запуску бэкенд-сервера:
  1.Клонируем репозиторий с сайта GitHub и заходим в директорию с проектом:
  ```
  git clone git@github.com:NoRIS95/Task2_for_Saraphan.git
  cd Task2_for_Saraphan

  ```
  2.Создаём виртуальное окружение (в нашем случае оно будет называться env) и активируем его:
  ```
  python3 -m venv env
  source ./env/bin/activate
  ```
  3. Устанавливаем зависимости из текстового файла requirements.txt
  ```
  pip install -r requirements.txt
  ```
  4.Создаём репозиторий миграции:
  ```
  flask db init
  ```
  5. Создадим сценарий миграции:
  ```
  flask db migrate
  ```
  6. Применяем изменения в базе данных:
  ```
  flask db upgrade
  ```
  7. Заходим в директорию app и создаем папку static:
  ```
  cd app
  mkdir static
  ```
  8. Заходим в папку static, создаём там директории category_photo, subcategory_photo и product_photo и возвращаемся обратно на 2 директории вверх:
  ```
  cd static
  mkdir category_photo
  mkdir subcategory_photo
  mkdir product_photo
  cd ../../
  ```
  9. Задаём путь основного приложения Flask:
  ```
  export FLASK_APP=main.py
  export ADMIN_TOKEN=<....>
  ```
  10. Запускаем наш сервер:
  ```
  flask run
  ```
## REST API
  Примеры запросов для проверки работы манипуляций с категориями, подкатегориями и продуктами лежат в директории [tests/](tests/).
### Headers
{"Admin_token": <ADMIN_TOKEN>}
### Categories API
#### Отображение категорий
```GET /categories```
Параметры:
* page - параметр пагинации
* per_page - параметр пагинации

#### Добавление категорий
``` POST /categories```
Параметры:
* name - название категории
* slug_name - slug-имя категории
  + files

#### Редактирование категорий
``` PUT /categories```
Параметры:
* id - id категории
* name - новое название категории
* slug_name - новое slug-имя категории
  + files

#### Удаление категорий
``` DELETE /categories```
Параметры:
* category_id - id категории

### Subcategories API
#### Отображение подкатегорий
```GET /subcategories```
Параметры:
* page - параметр пагинации
* per_page - параметр пагинации

#### Добавление подкатегории
``` POST /subcategories```
Параметры:
* category_id - id категории
* name - название подкатег  ории
* slug_name - slug-имя подкатегории
  + files

#### Редактирование подкатегорий
``` PUT /subcategories```
Параметры:
* category_id - id категории
* id - id подкатегории
* name - новое название подкатегории
* slug_name - новое slug-имя подкатегории
  + files

#### Удаление подкатегорий
``` DELETE /subcategories```
Параметры:
* id - id подкатегории

### Products API
#### Отображение товаров
```GET /products```
Параметры:
* page - параметр пагинации
* per_page - параметр пагинации

#### Добавление товара
``` POST /products```
Параметры:
* subcategory_id - id подкатегории
* name - название товара
* slug_name - slug-имя товара
  + files

#### Редактирование товара
``` PUT /products```
Параметры:
* subcategory_id - id подкатегории
* id - id товара
* name - новое название товара
* slug_name - новое slug-имя товара
  + files

#### Удаление товара
``` DELETE /subcategories```
Параметры:
* id - id товара

