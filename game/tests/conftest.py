import pytest

from game.models import Answer


@pytest.fixture
def sample_answer():
    return Answer(content='a',
                  confirmation='Congratulations! Your answer is correct!',
                  default="Sorry, it's not correct",
                  rejections={'aa': 'Overcomplicated',
                              'z': 'Nope.'})
