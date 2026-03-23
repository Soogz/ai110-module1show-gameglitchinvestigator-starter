from logic_utils import check_guess, reset_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests for the numeric-vs-string comparison bug fix.
# The old code passed a string secret on even attempts, causing lexicographic
# comparison where e.g. "9" > "10" (wrong). These cases verify numeric ordering.

def test_hint_correct_when_single_digit_guess_below_two_digit_secret():
    # 9 < 10 numerically, but "9" > "10" lexicographically.
    # Should always be "Too Low".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

def test_hint_correct_when_guess_starts_with_larger_digit_than_secret():
    # 21 < 30 numerically, but "21" > "19" etc. – broader numeric case.
    outcome, _ = check_guess(21, 30)
    assert outcome == "Too Low"

def test_hint_correct_numeric_too_high():
    # 15 > 9 numerically; make sure "Too High" is returned, not confused by string order.
    outcome, _ = check_guess(15, 9)
    assert outcome == "Too High"


# Tests for the new game reset fix.
# Before the fix, clicking "New Game" after a game ended did not reset status
# to "playing", so st.stop() would fire immediately and block all input.

def test_reset_game_state_after_win():
    state = {"attempts": 5, "secret": 42, "status": "won", "history": [10, 20, 42]}
    reset_game_state(state, 77)
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["attempts"] == 0
    assert state["secret"] == 77

def test_reset_game_state_after_loss():
    state = {"attempts": 8, "secret": 99, "status": "lost", "history": [1, 2, 3]}
    reset_game_state(state, 55)
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["attempts"] == 0
    assert state["secret"] == 55

def test_reset_game_state_sets_new_secret():
    state = {"attempts": 3, "secret": 10, "status": "won", "history": [10]}
    reset_game_state(state, 42)
    assert state["secret"] == 42
