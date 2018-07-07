import pytest

from game.models import Answer, Reward, Edition


@pytest.fixture
def sample_reward(db):
    return Reward.objects.create(description='The cake is a lie.')


@pytest.fixture
def sample_edition(sample_reward, db):
    return Edition.objects.create(name='Sample Edition', reward=sample_reward)


@pytest.fixture
def sample_answers(db):
    return [Answer.objects.create(content='a',
                                  confirmation='Congratulations! Your answer is correct!',
                                  default="Sorry, it's not correct",
                                  rejections={'aa': 'Overcomplicated',
                                              'z': 'Nope.'})
            for _ in range(2)]
