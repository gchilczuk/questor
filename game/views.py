from django.shortcuts import get_object_or_404, render
from django.views import View

from game.models import Quest


class QuestView(View):
    http_method_names = ['get', 'post']

    def get(self, request, id, *args, **kwargs):
        quest = get_object_or_404(Quest, id=id)
        return render(request, 'question.html', {'quest': quest})

    def post(self, request, id, *args, **kwargs):
        quest = get_object_or_404(Quest, id=id)

        return render(request, 'answer.html', {})



def hello(request):
    return render(request, 'question.html', {})
