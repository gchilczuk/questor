from django.urls import path

from game.views import QuestView, hello

urlpatterns = [
    path('quest/<uuid:id>', QuestView.as_view(), name='quest'),
    path('a', hello, name='hello'),
]
