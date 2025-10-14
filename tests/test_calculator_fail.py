"""
Initially failing test suite for calculator module
Students will need to fix the calculator to make these tests pass!
"""
import pytest
import sys
from pathlib import Path

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "app"))

from calculator import add, subtract, multiply, divide


class TestEdgeCases:
    """Test edge cases that will initially fail"""
    
    def test_add_floats(self):
        """Test addition with floating point numbers"""
        result = add(2.5, 3.7)
        assert abs(result - 6.2) < 0.0001  # Allow for floating point precision
        
    def test_subtract_floats(self):
        """Test subtraction with floating point numbers"""
        result = subtract(10.5, 3.2)
        assert abs(result - 7.3) < 0.0001
        
    def test_divide_floats(self):
        """Test division resulting in float"""
        result = divide(7, 2)
        assert result == 3.5
        
    def test_add_large_numbers(self):
        """Test addition with large numbers"""
        result = add(999999999, 1)
        assert result == 1000000000


# TODO: Uncomment these tests once you implement the missing functions!

# class TestMissingFunctions:
#     """Tests for functions that need to be implemented"""
#     
#     def test_square_root(self):
#         """Test square root function (need to implement!)"""
#         from calculator import square_root
#         assert square_root(16) == 4
#         assert square_root(25) == 5
#         
#     def test_absolute_value(self):
#         """Test absolute value function (need to implement!)"""
#         from calculator import absolute
#         assert absolute(-5) == 5
#         assert absolute(5) == 5

