import pytest
from unittest.mock import patch
import assignment_3

def test_add_friend():
    """Test if the friend's name is correctly added to the user_friends set."""
    assignment_3.user_friends = set()
    with patch('builtins.input', return_value='Jen'):
        friend_name = input("Name a friend: ")
        assignment_3.user_friends.add(friend_name)
    assert friend_name in assignment_3.user_friends, "The friend's name should be added to the user_friends set."

def test_intersection(capsys):
    """Test if the intersection between nearby_people and user_friends is correct."""
    assignment_3.user_friends = {'Jen'}
    assignment_3.nearby_people = {'Rolf', 'Jen', 'Anna'}
    intersection = assignment_3.user_friends.intersection(assignment_3.nearby_people)
    
    print(intersection)
    captured = capsys.readouterr()
    assert captured.out.strip() == "{'Jen'}", "The intersection should correctly show the nearby friends."


