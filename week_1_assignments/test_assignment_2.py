import pytest
from unittest.mock import patch
import assignment_2

def test_greeting(capsys):
    """Test the greeting output."""
    with patch('builtins.input', return_value='Alice'):
        assignment_2.name = input("What is your name? ")
        print(f"Hello, {assignment_2.name}")
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello, Alice", "The greeting should be 'Hello, NAME'."

def test_age_in_months(capsys):
    """Test the age to months conversion and output."""
    with patch('builtins.input', side_effect=['25']):
        assignment_2.age = int(input("What is your age? "))
        assignment_2.months = assignment_2.age * 12
        print(f"{assignment_2.months} months")
        captured = capsys.readouterr()
        assert captured.out.strip() == "300 months", "The age in months should be correctly calculated and printed."


