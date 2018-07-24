from django.urls import path

from game.views import QuestView, reward

urlpatterns = [
    path('quest/<uuid:id>', QuestView.as_view(), name='quest'),
    path('reward/<uuid:id>', reward, name='reward'),
]
