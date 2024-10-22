from src.service.service import Service
from src.domain.codes import Colors, WinCodes


class Test:  # More like a demonstration class than a test class :P
    def __init__(self):
        self.service = Service(6, 7)

    def __player1_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.UNDERLINE}{Colors.BLUE}PLAYER 1 WINS!!!{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __player2_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.UNDERLINE}{Colors.BLUE}PLAYER 2 WINS!!!{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __draw_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.WARNING}DRAW :/{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __print_board(self):
        board = self.service.get_board()
        print(board)

    def test_function(self):
        # Player 1 Wins
        self.service.add_piece_player1(1)
        self.service.add_piece_player2(2)
        self.service.add_piece_player1(1)
        self.service.add_piece_player2(2)
        self.service.add_piece_player1(4)
        self.service.add_piece_player2(1)
        self.service.add_piece_player1(1)
        self.service.add_piece_player2(3)
        self.service.add_piece_player1(3)
        self.service.add_piece_player2(3)
        self.service.add_piece_player1(2)

        win_code = self.service.is_win()
        if win_code == WinCodes.player1_is_winner:
            self.__player1_wins()
            self.__print_board()
        elif win_code == WinCodes.player2_is_winner:
            self.__player2_wins()
            self.__print_board()
        elif win_code == WinCodes.draw:
            self.__draw_wins()
            self.__print_board()

        # Player 2 wins
        self.service = Service(6, 7)

        self.service.add_piece_player1(3)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(2)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(1)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(3)
        self.service.add_piece_player2(4)

        win_code = self.service.is_win()
        if win_code == WinCodes.player1_is_winner:
            self.__player1_wins()
            self.__print_board()
        elif win_code == WinCodes.player2_is_winner:
            self.__player2_wins()
            self.__print_board()
        elif win_code == WinCodes.draw:
            self.__draw_wins()
            self.__print_board()

        # Draw
        self.service = Service(4, 3)

        self.service.add_piece_player1(1)
        self.service.add_piece_player1(2)
        self.service.add_piece_player1(3)

        self.service.add_piece_player2(1)
        self.service.add_piece_player2(2)
        self.service.add_piece_player2(3)

        self.service.add_piece_player1(1)
        self.service.add_piece_player1(2)
        self.service.add_piece_player1(3)

        self.service.add_piece_player2(1)
        self.service.add_piece_player2(2)
        self.service.add_piece_player2(3)

        win_code = self.service.is_win()
        if win_code == WinCodes.player1_is_winner:
            self.__player1_wins()
            self.__print_board()
        elif win_code == WinCodes.player2_is_winner:
            self.__player2_wins()
            self.__print_board()
        elif win_code == WinCodes.draw:
            self.__draw_wins()
            self.__print_board()

        # Player 1 Wins
        self.service = Service(4, 5)

        self.service.add_piece_player1(1)
        self.service.add_piece_player2(2)
        self.service.add_piece_player1(2)
        self.service.add_piece_player2(3)
        self.service.add_piece_player1(4)
        self.service.add_piece_player2(3)
        self.service.add_piece_player1(3)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(5)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(4)

        win_code = self.service.is_win()
        if win_code == WinCodes.player1_is_winner:
            self.__player1_wins()
            self.__print_board()
        elif win_code == WinCodes.player2_is_winner:
            self.__player2_wins()
            self.__print_board()
        elif win_code == WinCodes.draw:
            self.__draw_wins()
            self.__print_board()

        # Error Messages
        self.service = Service(6, 7)

        self.service.add_piece_player1(2)
        self.service.add_piece_player2(3)
        self.service.add_piece_player1(3)
        self.service.add_piece_player2(3)
        print("\n")
        self.__print_board()
        try:
            self.service.add_piece_player1(10)
        except ValueError as ve:
            print(f"{Colors.WARNING}{ve}{Colors.ENDColor}")

        print(" >> Tried to add at column 10 << \n\n")

        self.service.add_piece_player1(3)
        self.service.add_piece_player2(2)
        self.service.add_piece_player1(4)
        self.service.add_piece_player2(4)
        self.service.add_piece_player1(3)
        self.service.add_piece_player2(3)

        try:
            self.service.add_piece_player1(3)
        except ValueError as ve:
            print(f"{Colors.WARNING}{ve}{Colors.ENDColor}")
        print(" >> Tried to add at column 3 << \n\n")
        self.__print_board()

        print(f"{Colors.HEADER}{Colors.BOLD}>>> Tests done! <<<\n"
              f">>> All functionalities are working flawlessly! <<<\n"
              f">>> Great success! <<<{Colors.ENDColor}\n\n")

        print(f"{Colors.GREEN}{Colors.UNDERLINE}{Colors.BOLD}Back to the game!!!{Colors.ENDColor}\n")