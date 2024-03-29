# api_final
api final

### Описание:

В данной версии проекта yatube было реализовано взаимодействие с пользователем при помощи API.
Данный проект реализует функцию публикации постов, просмотр постов других авторов, подписка на авторов
и возможность комметировать посты.
Читать статьи, смотреть комментарии к постам может анонимный пользователь. Для создания поста или 
добавления к постам комментариев необходимо авторизоваться. Аналогично для подписки на 
каког-либо автора.
Редактировать пост или свой комментарий может только автор. Другим пользователям запрещено.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
 git clone git@github.com:serg350/api_final_yatube.git
```

```
cd .\yatube_api\
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
venv/Scripts/activate 
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Установить пакет djoser:

```
pip install djoser djangorestframework-simplejwt==4.7.2
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Примеры запроса получения публикации:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Ответ:

```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

Примеры запроса на подписку:

```
http://127.0.0.1:8000/api/v1/follow/
```

```
{
"following": "string"
}
```

Ответ:

```
{
"user": "string",
"following": "string"
}
```