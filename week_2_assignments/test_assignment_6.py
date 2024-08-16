import pytest
from io import StringIO
from contextlib import redirect_stdout
import assignment_6

def test_fizzbuzz(capsys):
    """Test that the FizzBuzz implementation is correct for numbers 1 to 100."""
    expected_output = []
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            expected_output.append("FizzBuzz")
        elif i % 3 == 0:
            expected_output.append("Fizz")
        elif i % 5 == 0:
            expected_output.append("Buzz")
        else:
            expected_output.append(str(i))
    
    with redirect_stdout(StringIO()) as f:
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

    captured = f.getvalue().strip().split('\n')
    assert captured == expected_output, "The output does not match the expected FizzBuzz sequence."


