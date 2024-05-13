from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('show_rates.urls')),
]

admin.site.site_header = 'Курсы валют'
admin.site.index_title = 'Курсы валют'
