import random
import string
import uuid

import pytest

from ..utils import is_valid_uuid, toss

fake_uuid = ["".join([random.choice(string.ascii_letters) for _ in range(random.randint(16, 31))]) for _ in range(10)]

tosses_list = [[1, 2], [1], [1, 2, 3]]
excepted_result = [{1: 2, 2: 1}, {}, {1: 2, 2: 3, 3: 1}]


@pytest.mark.parametrize("uuid_", (uuid.uuid4().hex for _ in range(10)))
def test_is_valid_uuid__valid_uuid(uuid_):
    assert is_valid_uuid(uuid_)


@pytest.mark.parametrize("uuid_", fake_uuid)
def test_is_valid_uuid__invalid_uuid(uuid_):
    assert not is_valid_uuid(uuid_)


@pytest.mark.xfail
@pytest.mark.parametrize(("init_list", "toss_result"), list(zip(tosses_list, excepted_result)))
def test_toss_result(init_list, toss_result):

    assert toss(init_list) == toss_result
