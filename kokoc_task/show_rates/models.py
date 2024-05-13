from django.db import models


class Currency(models.Model):
    """ Модель валюты """

    char_code = models.CharField(max_length=5, unique=True, verbose_name='Символьный знак')
    name = models.CharField(max_length=100, verbose_name='Наименование валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    """ Модель курса валюты """

    currency = models.ForeignKey(Currency, related_name='cur', on_delete=models.CASCADE, verbose_name='Валюта')
    date = models.DateField(verbose_name='Дата сбора данных')
    value = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Значение')

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        constraints = [
            models.UniqueConstraint(
                fields=['currency', 'date'],
                name='unique_currency_date'
            )
        ]

    def __str__(self):
        return f"{self.currency.name} - {self.date}: {self.value}"
