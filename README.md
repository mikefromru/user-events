# События
## _Добро пожаловать!_

Приложение для создания событий. Каждый зарегистрированный пользователь может создать событие, удалить своё событие, присоединится к событию которое было созданно другими пользователями.
Приложения написанно с использованием Django(DRF) в качестве бекэнда. Также используется интерфейс написан на Vue.js который и используется в Django шаблонах.

## Технологии

Приложение События использует ряд технологий:

- Django - бесплатный и свободный фреймворк для веб-приложений!
- Django Restframework - API фреймворк для Django 
- Vue.js - прогрессивный фреймворк для создания пользовательских интерфейсов
- Docker - программная платформа для быстрой разработки, тестирования и развертывания приложений
- Docker-compouse - средство для определения и запуска приложений Docker с несколькими контейнерами
- Bootstrap - CSS-фреймворк

## Установка

```sh
cd user-events
cp project/settings/example.env project/settings/.env
```

Установите переменные окружения в `.env` файле (Обязательные переменные приведены ниже для development)
```
SECRET_KEY=your-secret-key
```

Установка зависимостей, выполнение миграций
```
pip install -r requirements.txt
python manage.py migrate
```

Запуск с настройками development
```
python manage.py runserver --settings=project.settings.development
```

Запуска с настройками production на локальной машине.
Добавьте переменные окружения в `.env` файле для БД и использования с Docker в prodaction
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432
```

```
python manage.py runserver --settings=project.settings.production --insecure
```

## Docker

```
docker compose up --build
```


## Использование
- Зарегистрироваться POST `/accounts/register/`
- Войти в систему POST `/accounts/login/`
- Создать событие POST `/app/`
- Получить все события GET `/events/`
- Получить только свои события GET `/app/`
- Получить событи GET `/event/id_event/`
- Удалить событие DELETE `/event/id_event/`
- Принять участие или отменить участие в событие PATCH `/event/id_event/`