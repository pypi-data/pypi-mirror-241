from typingchecker import check_types
from typing import Union
import pytest


class needed_class:
    def __init__(self, var) -> None:
        self.var = var


class checked_class:
    @check_types()
    def __init__(
        self,
        a: int,
        b: list[list[int]],
        c: Union[needed_class, list[needed_class]],
        d: float | list[float],
        e: dict[str, int],
    ):
        pass


needed_obj = needed_class(3)


def test_check_types_decorator():
    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1]],
        needed_obj,
        1.0,
        {"a": 1},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[1], [2]],
        [needed_obj, needed_obj],
        [1.0, 2.0],
        {"a": 1, "b": 2},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [],
        needed_obj,
        1.0,
        {},
    )

    ### if check_types works, this should not raise an error
    checked_class(
        1,
        [[]],
        [needed_obj],
        [1.0],
        {"a": 1},
    )

    ### if check_types works, this should raise an TypeError because a is not an int
    with pytest.raises(TypeError):
        checked_class(
            "1",
            [[1]],
            needed_obj,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because b is not a list of lists of ints
    with pytest.raises(TypeError):
        checked_class(
            1,
            [1],
            needed_obj,
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because c is not a needed_class or a list of needed_class
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            "needed_obj",
            1.0,
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because d is not a float or a list of floats
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            "1.0",
            {"a": 1},
        )

    ### if check_types works, this should raise an TypeError because e is not a dict of str to int
    with pytest.raises(TypeError):
        checked_class(
            1,
            [[1]],
            needed_obj,
            1.0,
            {"a": "1"},
        )
