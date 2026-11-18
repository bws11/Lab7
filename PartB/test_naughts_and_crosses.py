import pytest
from naughts_and_crosses import *

def test_game():
    # Test is valid move
    assert is_valid_move(create_board(), 2, 2) == True
    assert is_valid_move(create_board(), 1, 1) == True
    assert is_valid_move(create_board(), 0, 0) == True
    assert is_valid_move(create_board(), 2, 3) == False
    assert is_valid_move(create_board(), 3, 2) == False
    assert is_valid_move(create_board(), -2, 2) == False
    assert is_valid_move(create_board(), 2, -2) == False


pytest.main()