from django.urls import path

from supervisor.views import quest, mirror

urlpatterns = [
    path('', mirror),
    path('quest/<uuid:id>', quest),
]
