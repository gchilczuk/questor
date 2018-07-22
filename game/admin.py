from django.contrib import admin
from game.models import Reward, Edition, Quest, Answer


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    pass


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
