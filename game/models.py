import uuid
from collections import namedtuple

from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.utils.timezone import now


class Edition(models.Model):
    """
    Represents single game edition in the service. Edition can have multiple Quests

    :name: name of the game edition
    :start: date when game edition start, if not provided edition will start instantly
        quests are not available for players before start date
    :finish: date when game edition ends, if not provided edition will last forever
        quests are not available for players after finish date
    """

    name = models.CharField(max_length=16, blank=False)
    start = models.DateTimeField(default=now)
    finish = models.DateTimeField(null=True)


class Quest(models.Model):
    """
    Represents basic quest entity.
    Player must complete the task to get the next one.
    To confirm that quest is solved player have to
    correctly answer the final question of the question.

    :id: uuid, primary key; universally unique identifier makes quests ordered non-sequentialy
    :title: the title of the quest
    :description: detailed description of quest
    :question: final question of the quest
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    question = models.CharField(max_length=100)
    answer = models.OneToOneField('Answer', models.SET_NULL)
    edition = models.ForeignKey(Edition, models.CASCADE, related_name='quests', related_query_name='quest')


AnsResp = namedtuple('AnsResp', ['correct', 'feedback'])


class Answer(models.Model):
    """
    Representation of correct answer of Quest.

    :answer: correct answer of final question of the Quest
    :confirmation: feedback provided when user provide correct answer
    :default: default rejection response
    :rejections: dictionary of special-case responses to wrong answers.
        It may be useful for example when is very probable that user will misspell answer,
        or when answer is close enough to provide additional informations.
    """

    content = models.CharField(max_length=24)
    confirmation = models.TextField()
    default = models.TextField()
    rejections = HStoreField()

    def evaluate(self, answer):
        """
        Evaluate if answer provided by user is correct and return appropriate answer

        :param answer: answer provided by user
        :return: True if users' answer is correct, False otherwise
        """
        correct = answer == self.content

        return AnsResp(
            correct,
            self.confirmation if correct else self.rejections.get(answer, self.default))
