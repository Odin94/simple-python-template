import pytest

from project_root.src.main import is_testable


# Make sure test functions start with "test", make sure non-test functions don't!
def test_is_testable():
    expected = "abc_was_the_string"
    actual = is_testable("abc")

    assert expected == actual

