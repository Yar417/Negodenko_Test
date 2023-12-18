Сборка и запуск контейнеров

    Установите Docker и Docker Compose на вашем компьютере.
    Клонируйте репозиторий с Django-приложением на ваш компьютер.
    Откройте терминал и перейдите в директорию проекта.
    Переименуйте secret_example.py в secret.py и проведите его настройки (поля уже подготовлены)
    Другие сервисы SMTP:
    https://dev-ed.ru/blog/django-email-gmail-mailru-yandex/
    
    Запустите следующую команду для сборки и запуска контейнеров:
    
          docker-compose up --build

После выполнения этих шагов ваше Django-приложение будет запущено в контейнере Docker и будет доступно по адресу:

    http://127.0.0.1:8000

Вы можете взаимодействовать с Django-приложением, используя следующие API-эндпоинты:

    GET /api/items/: Получить список всех книг.
    GET /api/items/<id>/: Получить информацию о конкретной книге.
    POST /api/items/: Создать новую книгу.
    PUT /api/items/<id>/: Обновить информацию о книге.
    DELETE /api/items/<id>/: Удалить книгу.

    POST api/users/: Создать нового пользователя
    
Особенности приложения

Django и Django REST Framework для создания веб-приложения и API.
Celery для асинхронных задач, таких как отправка электронных писем.
Docker для создания изолированной среды для запуска приложения и его зависимостей.