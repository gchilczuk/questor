import pytest

from game.forms import QuestForm


@pytest.mark.parametrize('input,expected', [
    # valid input
    ({'user_answer': 'a'}, True),
    ({'user_answer': '•’ąśðądazażółćgęśląjaźń'}, True),
    ({'user_answer': '_'}, True),

    # invalid input
    ({'user_answer': ''}, False),
])
def test_questform_valid(input, expected):
    assert QuestForm(input).is_valid() == expected
