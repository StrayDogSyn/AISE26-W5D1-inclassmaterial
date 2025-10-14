"""
Example test file for live coding demonstration
Shows how to write tests that will run in CI pipeline
"""
import pytest


# Example 1: Simple assertion test
def test_simple_assertion():
    """A basic test with a simple assertion"""
    result = 2 + 2
    assert result == 4


# Example 2: Testing with multiple assertions
def test_string_operations():
    """Test string operations"""
    text = "Hello, CI/CD"
    assert "CI" in text
    assert text.startswith("Hello")
    assert len(text) == 12


# Example 3: Testing exceptions
def test_exception_handling():
    """Test that exceptions are raised correctly"""
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0


# Example 4: Parametrized tests (more efficient!)
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (10, 20),
])
def test_double_number(input, expected):
    """Test doubling numbers with parametrize"""
    assert input * 2 == expected


# Example 5: Test that will intentionally fail (for demonstration)
@pytest.mark.skip(reason="This test is intentionally skipped for demo")
def test_intentional_failure():
    """This test would fail if not skipped"""
    assert 1 == 2  # This is false!


# Example 6: Test fixtures
@pytest.fixture
def sample_list():
    """Fixture that provides a sample list"""
    return [1, 2, 3, 4, 5]


def test_with_fixture(sample_list):
    """Test using a fixture"""
    assert len(sample_list) == 5
    assert sum(sample_list) == 15

