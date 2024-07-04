import pytest
from penalty import penalty

def test_cow_penalty_points():
assert penalty.cow_penalty_points(55) == 7
assert penalty.cow_penalty_points(33) == 5
assert penalty.cow_penalty_points(70) == 3
assert penalty.cow_penalty_points(25) == 2
assert penalty.cow_penalty_points(99) == 1

pytest.main()





