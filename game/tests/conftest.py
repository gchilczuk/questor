import pytest

from game.models import Answer, Reward, Edition


@pytest.fixture
def sample_reward(db):
    return Reward.objects.get_or_create(description='The cake is a lie.')[0]


@pytest.fixture
def sample_edition(sample_reward, db):
    return Edition.objects.get_or_create(name='Sample Edition', reward=sample_reward)[0]


@pytest.fixture
def sample_answers(db):
    return [Answer.objects.create(content='a',
                                  confirmation='Congratulations! Your answer is correct!',
                                  default="Sorry, it's not correct",
                                  rejections={'aa': 'Overcomplicated',
                                              'z': 'Nope.'})
            for _ in range(2)]
