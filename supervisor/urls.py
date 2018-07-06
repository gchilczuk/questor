from django.urls import path

from supervisor.views import quest

urlpatterns = [
    path('quest/<uuid:id>', quest),
]
