import pytest
from unittest.mock import patch

def test_winning_player(capsys):
    """Test to ensure the correct player and winnings are determined."""
    lottery_numbers = {13, 21, 22, 5, 8, 3}

    with patch('assignment_7.lottery_numbers', lottery_numbers):
        with patch('assignment_7.players', [
            {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},  # 3 matches
            {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},  # 2 matches
            {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},  # 1 match
            {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},  # 3 matches
        ]):
            from assignment_7 import max_matched, winner
            max_matched = 0
            winner = ""
            for player in assignment_7.players:
                matched_numbers = player["numbers"].intersection(lottery_numbers)
                if len(matched_numbers) > max_matched:
                    max_matched = len(matched_numbers)
                    winner = player["name"]

            if winner:
                winnings = 100 ** max_matched
                print(f"{winner} won {winnings}.")
            else:
                print("No winner.")

            captured = capsys.readouterr()
            assert "Rolf won 1000000." in captured.out or "Jen won 1000000." in captured.out

def test_no_winner(capsys):
    """Test to ensure correct behavior when there is no winner."""
    lottery_numbers = {30, 31, 32, 33, 34, 35}

    with patch('assignment_7.lottery_numbers', lottery_numbers):
        with patch('assignment_7.players', [
            {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},  # 0 matches
            {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},  # 0 matches
            {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},  # 0 matches
            {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},  # 0 matches
        ]):
            from assignment_7 import max_matched, winner
            max_matched = 0
            winner = ""
            for player in assignment_7.players:
                matched_numbers = player["numbers"].intersection(lottery_numbers)
                if len(matched_numbers) > max_matched:
                    max_matched = len(matched_numbers)
                    winner = player["name"]

            if winner:
                winnings = 100 ** max_matched
                print(f"{winner} won {winnings}.")
            else:
                print("No winner.")

            captured = capsys.readouterr()
            assert "No winner." in captured.out

