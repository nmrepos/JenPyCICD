import pytest
import calc

class TestCalc:

    def test_add2_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        assert result == 3

    def test_add2_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2(10.5, 2.0)
        assert result == 12.5

    def test_add2_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('hello', 'world')
        assert result == 'helloworld'

    def test_add2_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string
        """
        result = calc.add2('hello', 3)
        assert result == 'hello3'

    def test_add2_integer_and_string(self):
        """
        Test the addition of an integer and a string returns them as one
        concatenated string
        """
        result = calc.add2(3, 'hello')
        assert result == '3hello'

    def test_subtract2_integers(self):
        """
        Test that the subtraction of two integers returns the correct result
        """
        result = calc.subtract2(10, 3)
        assert result == 7
