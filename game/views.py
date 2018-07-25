from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.http import require_GET

from game.forms import QuestForm
from game.models import Quest


class QuestView(View):
    http_method_names = ['get', 'post']

    def get(self, request, id):
        quest = get_object_or_404(Quest, id=id)
        return render(request, 'question.html', {'quest': quest})

    def post(self, request, id):
        quest = get_object_or_404(Quest, id=id)
        qf = QuestForm(request.POST)

        if qf.is_valid():
            user_answer = qf.cleaned_data['user_answer']
            result = quest.answer.evaluate(user_answer)
            return render(request, 'answer.html', {'quest': quest, 'result': result})

        else:
            return HttpResponseBadRequest('You broke it - you won it!')


@require_GET
def reward(request, id):
    quest = get_object_or_404(Quest, id=id)
    edition = quest.edition
    return render(request, 'reward.html', {'name': edition.name, 'reward': edition.reward})
