from django import forms


class QuestForm(forms.Form):
    user_answer = forms.CharField(max_length=24)
