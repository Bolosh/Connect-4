

class InputOptions:
    help_word = "help"
    settings_word = "settings"
    test_word = "test"
    exit_words = "exit"
    yes_option = "y"
    no_option = "n"


class Codes:
    player_1 = 1
    player_2 = 2
    standard_number_of_rows = 6
    standard_number_of_columns = 7


class WinCodes:
    player1_is_winner = 1  # Player with 'X'
    player2_is_winner = 2  # Player with 'O'
    nothing_happened = -1  # Game not over yet
    draw = 0


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDColor = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
