from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ExchangeRate
from datetime import datetime
from .services import DatabaseService


class ShowExchangeRatesView(APIView):
    """ Вьюха для получения курсов валют за указанную дату. """

    def get(self, request, *args, **kwargs):
        date_str = request.query_params.get('date', None)
        if date_str is not None:
            try:
                exchange_rates = DatabaseService.get_object_by_attr(
                    model=ExchangeRate,
                    date=datetime.strptime(date_str, '%Y-%m-%d')
                )
                rates_data = [
                    {"currency": rate.currency.char_code, "value": rate.value} for rate in exchange_rates
                ]
                return Response(rates_data)
            except ValueError:
                return Response(
                    {
                        "error": True,
                        "error_description": "Incorrect date format"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    "error": True,
                    "error_description": "Date parameter is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
