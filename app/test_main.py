import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "0  must be equal to [0, 0] human age",
        "14  must be equal to [0, 0] human age",
        "15  must be equal to [1, 1] human age",
        "23  must be equal to [1, 1] human age",
        "24  must be equal to [2, 2] human age",
        "27  must be equal to [2, 2] human age",
        "28  must be equal to [3, 2] human age",
        "100  must be equal to [21, 17] human age",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages
