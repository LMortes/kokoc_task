# Kokos Test Task

Тестовое задание Kokoc Group.

## Clone repo

Склонировать репозиторий.

```bash
git clone https://github.com/LMortes/kokoc_task.git
```

## Виртуальное окружение и зависимости
### Создание виртуального окружения
```bash
python -m venv venv
```
### Активация venv
Windows:
```bash
source venv/Scripts/activate
```

MacOS/Linux:
```bash
source venv/bin/activate
```
### Установка зависимостей
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
## Запуск проекта.
Прогоним миграции
```bash
cd kokos_task/
python manage.py makemigrations
python manage.py migrate
```
Спарсим данные о курсе валют со страницы
```bash
python manage.py get_data
```
Запустим сервер
```bash
python manage.py runserver
```

## Пример работы API
```bash
GET /show_rates?date=yyyy-mm-dd - получить список курсов валют за конкретную дату.
```
Тело ответа:
```json
[ 
    {
        "currency": "AUD",
        "value": 60.4411
    },
    {
        "currency": "AZN",
        "value": 53.9018
    },
    {
        "currency": "GBP",
        "value": 114.6146
    },
    ...
]
```
### Возможные ошибки:
Некорректная дата в параметрах запроса
```json
{
    "error": True,
    "error_description": "Incorrect date format"
}
```

Не передан обязательный параметр date в запросе
```json
{
    "error": True,
    "error_description": "Date parameter is required"
}
```

# Отложенная задача
## Запуск Celery задачи
Запуск celery задачи, которая в 7:00 каждый день парсит данные сервиса ЦБ

1. Запуск Redis (Docker)
```bash
docker run -d -p 6379:6379 redis
```

2. Запуск Worker`а celery
```bash
celery -A kokoc_task worker -l info
```

3. Запуск задачи celery.
```bash
celery -A kokoc_task beat -l info
```