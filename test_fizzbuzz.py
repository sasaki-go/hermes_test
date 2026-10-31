"""Tests for fizzbuzz.fizzbuzz."""

import pytest
from fizzbuzz import fizzbuzz


class TestFizzBuzzBasic:
    """Core behaviour: numbers, Fizz, Buzz, FizzBuzz."""

    def test_single(self):
        assert fizzbuzz(1) == ["1"]

    def test_fizz_at_3(self):
        assert fizzbuzz(3) == ["1", "2", "Fizz"]

    def test_buzz_at_5(self):
        assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_fizzbuzz_at_15(self):
        assert fizzbuzz(15) == [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ]

    def test_n_equals_15(self):
        """Full round of 15 numbers."""
        expected = [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ]
        assert fizzbuzz(15) == expected


class TestFizzBuzzEdge:
    """Boundary conditions."""

    def test_zero(self):
        assert fizzbuzz(0) == []

    def test_large(self):
        result = fizzbuzz(100)
        assert len(result) == 100
        assert result[-1] == "Buzz"  # 100 is multiple of 5

    def test_negative_raises(self):
        with pytest.raises(ValueError, match="non-negative"):
            fizzbuzz(-1)

    def test_negative_raises_message(self):
        with pytest.raises(ValueError, match="-5"):
            fizzbuzz(-5)
