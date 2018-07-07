from django.urls import path

from game.views import quest

urlpatterns = [
    path('quest/<uuid:id>', quest),
]
