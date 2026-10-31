"""FizzBuzz — FizzBuzz implementation."""


def fizzbuzz(n: int) -> list[str]:
    """Return a FizzBuzz list from 1 to n inclusive.

    Rules
    -----
    * Multiples of 3  → "Fizz"
    * Multiples of 5  → "Buzz"
    * Multiples of 15 → "FizzBuzz"
    * Otherwise       → the decimal representation of the number

    Parameters
    ----------
    n : int
        Upper bound (1-based). Must be >= 1.

    Raises
    ------
    ValueError
        If *n* is negative.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    result: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
