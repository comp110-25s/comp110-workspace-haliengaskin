"""This is the test file for my dictionary."""

__author__: str = "730730083"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_one():
    """Regular degular use case of invert."""
    ice_cream = {
        "chocolate": "twelve",
        "vanilla": "eight",
        "strawberry": "five",
    }
    expected = {
        "twelve": "chocolate",
        "eight": "vanilla",
        "five": "strawberry",
    }
    assert invert(ice_cream) == expected


def test_invert_two():
    """Another regular degular use case of invert."""
    cowo = {
        "lion": "fish",
        "jelly": "bean",
        "cat": "nap",
        "blue": "bird",
    }
    expected = {
        "fish": "lion",
        "bean": "jelly",
        "nap": "cat",
        "bird": "blue",
    }
    assert invert(cowo) == expected


def test_invert_doubles():
    """Duplicate test case for invert."""
    not_even_andre = {"amadou": "onana", "andre": "onana"}
    with pytest.raises(KeyError):
        invert(not_even_andre)


def test_count_one():
    """Test case for count."""
    psv_ars: list[str] = [
        "timber",
        "nwaneri",
        "merino",
        "odegaard",
        "trossard",
        "odegaard",
        "calafiori",
    ]
    expected = {
        "timber": 1,
        "nwaneri": 1,
        "merino": 1,
        "odegaard": 2,
        "trossard": 1,
        "calafiori": 1,
    }
    assert count(psv_ars) == expected


def test_count_two():
    """Test case for count."""
    nonsense: list[str] = [
        "I",
        "dont",
        "even",
        "know",
        "Im",
        "talkin",
        "nonsense",
        "Im",
        "talkin",
        "Im",
        "talkin",
    ]
    expected = {
        "I": 1,
        "dont": 1,
        "even": 1,
        "know": 1,
        "Im": 3,
        "talkin": 3,
        "nonsense": 1,
    }
    assert count(nonsense) == expected


def test_count_nodoubles():
    """Test case for when there are no repeated words."""
    noreps: list[str] = [
        "nike",
        "adidas",
        "newbalance",
    ]
    expected = {
        "nike": 1,
        "adidas": 1,
        "newbalance": 1,
    }
    assert count(noreps) == expected


def test_favorite_color_one():
    mane: dict[str, str] = {
        "aj": "orange",
        "rainbow": "blue",
        "rari": "purple",
        "twi": "purple",
        "flutter": "yellow",
        "pinkie": "pink",
    }
    expected = "purple"
    assert favorite_color(mane) == expected


def test_favorite_color_two():
    mane: dict[str, str] = {
        "aj": "orange",
        "rainbow": "blue",
        "shining": "blue",
        "rari": "purple",
        "twi": "purple",
        "flutter": "yellow",
        "pinkie": "pink",
    }
    expected = "blue"
    assert favorite_color(mane) == expected


def test_favorite_color_none():
    mane: dict[str, str] = {
        "aj": "orange",
        "rainbow": "blue",
        "rari": "white",
        "twi": "purple",
        "flutter": "yellow",
        "pinkie": "pink",
    }
    expected = "no repeats"
    assert favorite_color(mane) == expected


def test_bin_len_one():
    ok: list[str] = ["the", "quick", "fox"]
    expected = {3: {"fox", "the"}, 5: {"quick"}}
    assert bin_len(ok) == expected


def test_bin_len_two():
    sent: list[str] = ["i", "am", "the", "best", "coder"]
    expected = {1: {"i"}, 2: {"am"}, 3: {"the"}, 4: {"best"}, 5: {"coder"}}
    assert bin_len(sent) == expected


def test_bin_len_empty():
    empty: list[str] = []
    expected: dict[int, set[str]] = {}
    assert bin_len(empty) == expected
