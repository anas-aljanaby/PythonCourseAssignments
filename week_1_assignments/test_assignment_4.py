import pytest
from io import StringIO
from contextlib import redirect_stdout
import assignment_4

def test_players_list():
    """Test that the players list is defined correctly with two players."""
    assert len(assignment_4.players) == 2, "There should be exactly two players in the list."
    for player in assignment_4.players:
        assert 'name' in player and 'numbers' in player, "Each player should have a 'name' and 'numbers'."
        assert isinstance(player['numbers'], set), "The 'numbers' for each player should be a set."

def test_print_results(capsys):
    """Test the output string for each player."""
    assignment_4.lottery_numbers = {13, 21, 22, 5, 8}
    assignment_4.players = [
        {'name': 'Alice', 'numbers': {13, 22, 7, 8, 10}},
        {'name': 'Bob', 'numbers': {13, 21, 5, 9, 11}},
    ]

    expected_outputs = [
        "Player Alice got 3 numbers right.",
        "Player Bob got 3 numbers right."
    ]

    for player in assignment_4.players:
        matched_numbers = player['numbers'].intersection(assignment_4.lottery_numbers)
        print(f"Player {player['name']} got {len(matched_numbers)} numbers right.")

    captured = capsys.readouterr()
    for expected in expected_outputs:
        assert expected in captured.out.strip(), f"Expected output '{expected}' not found in printed output."

