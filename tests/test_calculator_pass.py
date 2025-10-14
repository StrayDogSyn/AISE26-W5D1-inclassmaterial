"""
Passing test suite for calculator module
These tests should all pass initially
"""
import pytest
import sys
from pathlib import Path

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "app"))

from calculator import add, subtract, multiply, divide, power, modulo


class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        
    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
        
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5
        
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers"""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
        
    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0


class TestDivision:
    """Test division operations"""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers"""
        assert divide(6, 3) == 2
        assert divide(10, 2) == 5
        
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestAdvancedOperations:
    """Test advanced operations"""
    
    def test_power(self):
        """Test power operation"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1
        
    def test_modulo(self):
        """Test modulo operation"""
        assert modulo(5, 2) == 1
        assert modulo(10, 3) == 1
        assert modulo(7, 7) == 0
        
    def test_modulo_by_zero_raises_error(self):
        """Test that modulo by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            modulo(5, 0)

