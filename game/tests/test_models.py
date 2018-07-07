import pytest

from game.models import AnsResp, Quest


@pytest.mark.parametrize('provided,expected', [
    # correct answer
    ('a', AnsResp(True, 'Congratulations! Your answer is correct!')),

    # not correct
    ('b', AnsResp(False, "Sorry, it's not correct")),
    ('ə', AnsResp(False, "Sorry, it's not correct")),
    ('#! •daada\n a ', AnsResp(False, "Sorry, it's not correct")),

    # not correct - special case
    ('z', AnsResp(False, 'Nope.')),

    # blank answer
    ('', AnsResp(False, "Sorry, it's not correct")),
])
def test_answer_evalutaion(provided, expected, sample_answers):
    """Test if answer from user is evaluated correctly"""
    assert sample_answers[0].evaluate(provided) == expected


@pytest.mark.django_db
def test_quests_chaining(sample_edition, sample_answers):
    """Test if next / previous quests are returned correctly"""
    next_quest = Quest.objects.create(title='quest 2',
                                      description='really simple quest',
                                      question='2+3=?',
                                      answer=sample_answers[0],
                                      edition=sample_edition)

    current_quest = Quest.objects.create(title='quest 1',
                                         description='really simple quest',
                                         question='2+2=?',
                                         answer=sample_answers[1],
                                         edition=sample_edition,
                                         succeeding=next_quest)

    assert current_quest.succeeding == next_quest
    assert next_quest.preceding == current_quest
