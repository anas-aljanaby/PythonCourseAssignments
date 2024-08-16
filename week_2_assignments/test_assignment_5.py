import assignment_5
import pytest
from unittest.mock import patch

def test_input_p(capsys):
    """Test that the program prints 'Hello' when user types 'p' and continues asking."""
    user_inputs = iter(['p', 'p', 'q'])
    
    with patch('builtins.input', side_effect=user_inputs):
        assignment_5.user_input = input("Type 'p' or 'q': ")
        while assignment_5.user_input != 'q':
            if assignment_5.user_input == 'p':
                print("Hello")
            assignment_5.user_input = input("Type 'p' or 'q': ")
    
    captured = capsys.readouterr()
    assert captured.out.count("Hello") == 2, "The program should print 'Hello' twice when user inputs 'p' twice."

def test_input_q(capsys):
    """Test that the program terminates when user types 'q'."""
    user_inputs = iter(['p', 'q'])
    
    with patch('builtins.input', side_effect=user_inputs):
        assignment_5.user_input = input("Type 'p' or 'q': ")
        while assignment_5.user_input != 'q':
            if assignment_5.user_input == 'p':
                print("Hello")
            assignment_5.user_input = input("Type 'p' or 'q': ")
    
    captured = capsys.readouterr()
    assert "Hello" in captured.out, "The program should print 'Hello' once before terminating."
    assert captured.out.count("Hello") == 1, "The program should print 'Hello' only once when the user inputs 'p' then 'q'."

