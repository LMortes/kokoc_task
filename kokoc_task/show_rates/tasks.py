import requests
from datetime import date
from django.db import IntegrityError
from rest_framework import status
from .management.commands.get_data import REQUEST_URL
from .models import Currency, ExchangeRate
from .services import DatabaseService
from ..kokoc_task.celery import app


def fetch_data_celery(response):
    data = response.json()
    currencies = data['Valute']

    for currency_key, currency_data in currencies.items():
        currency_char_code = currency_data['CharCode']
        currency_name = currency_data['Name']
        currency_value = float(currency_data['Value'])

        exists_currency = DatabaseService.if_exists(
            model=Currency,
            char_code=currency_char_code
        )

        if not exists_currency:
            DatabaseService.create_object(
                model=Currency,
                char_code=currency_char_code,
                name=currency_name
            )

        try:
            currency = DatabaseService.get_object(
                model=Currency,
                char_code=currency_char_code
            )
            DatabaseService.create_object(
                model=ExchangeRate,
                currency=currency,
                date=date.today(),
                value=currency_value
            )
        except IntegrityError:
            ...


@app.task
def get_values():
    response = requests.get(REQUEST_URL)
    if response.status_code == status.HTTP_200_OK:
        fetch_data_celery(response)
        print(f'CELERY: Adding new records was successful')
    else:
        print(f'CELERY: Something went wrong :(')


