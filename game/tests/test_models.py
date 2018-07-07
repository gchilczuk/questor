import pytest

from game.models import AnsResp


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
def test_answer_evalutaion(provided, expected, sample_answer):
    assert sample_answer.evaluate(provided) == expected
