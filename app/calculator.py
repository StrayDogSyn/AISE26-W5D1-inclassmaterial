"""
Simple Calculator Module
A basic calculator for demonstrating CI/CD concepts
"""


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent


def modulo(a, b):
    """Return the remainder of a divided by b"""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def main():
    """Demo the calculator functions"""
    print("Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"5 % 2 = {modulo(5, 2)}")


if __name__ == "__main__":
    main()
