from datetime import date
import requests
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from rest_framework import status
from show_rates.models import Currency, ExchangeRate
from show_rates.services import DatabaseService

REQUEST_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


class Command(BaseCommand):
    """ Кастомная команда для парсинга данных о валюте. """

    help = f'Get and save currency and exchange rate from {REQUEST_URL}'

    def handle(self, *args, **options):
        self.response = requests.get(REQUEST_URL)
        if self.response.status_code == status.HTTP_200_OK:
            self.fetch_data()
            self.stdout.write(self.style.SUCCESS('Currency and exchange rate successfully fetch :)'))
        else:
            self.stdout.write(self.style.ERROR('Something went wrong :('))

    def fetch_data(self):
        data = self.response.json()
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
