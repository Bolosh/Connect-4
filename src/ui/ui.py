from src.service.service import Service
from src.domain.codes import WinCodes, Colors, Codes, InputOptions
from src.ui.test import Test
from src.gui.gui import Gui


class UserInterface:
    def __init__(self, number_of_rows, number_of_columns):
        self.__current_player = Codes.player_1
        self.__number_of_rows = number_of_rows
        self.__number_of_columns = number_of_columns
        self.__service = Service(number_of_rows, number_of_columns)
        self.__test = Test()

    def __settings(self):
        while True:
            print("\n1. Change board dimensions")
            print("2. Change to GUI\n")
            inputted_choice = input("Your pick >> ")
            if inputted_choice != "1" and inputted_choice != "2":
                print(f"{Colors.HEADER}Not a valid choice. Try again!{Colors.ENDColor}")
            else:
                if inputted_choice == "1":
                    new_number_of_rows = input("New number of rows >> ")
                    new_number_of_columns = input("New number of columns >> ")
                    if not new_number_of_rows.isdigit() or not new_number_of_columns.isdigit():
                        print(f"{Colors.HEADER}Input some numbers...{Colors.ENDColor}")
                    else:
                        self.__number_of_rows = int(new_number_of_rows)
                        self.__number_of_columns = int(new_number_of_columns)
                        self.__service = Service(self.__number_of_rows, self.__number_of_columns)
                        self.__current_player = Codes.player_1
                        break
                elif inputted_choice == "2":
                    while True:
                        game = Gui(self.__number_of_rows, self.__number_of_columns, self.__service,
                                   self.__current_player).start_game()
                        if game == 4:
                            self.__service = Service(self.__number_of_rows, self.__number_of_columns)
                            self.__current_player = Codes.player_1
                        elif game == 1:
                            self.__current_player = Codes.player_1
                            break
                        elif game == 2:
                            self.__current_player = Codes.player_2
                            break
                        else:
                            break
                    break

    def __get_input(self):
        return input("\nYour choice >> ")

    def __print_information(self):
        print("\nInput the word 'help' for the help menu.")
        print("Input the word 'settings' for the settings menu.")
        print("Input the word 'test' to test the game.")
        print("Input the word 'exit' to stop the game.")
        print("Enter the column index shown on top to place a piece.\n\n")

    def __player1_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.UNDERLINE}{Colors.BLUE}PLAYER 1 WINS!!!{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __player2_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.UNDERLINE}{Colors.BLUE}PLAYER 2 WINS!!!{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __draw_wins(self):
        print(f"\n{Colors.CYAN}>>>>>>>> {Colors.BOLD}{Colors.WARNING}DRAW :/{Colors.ENDColor} {Colors.CYAN}<<<<<<<<{Colors.ENDColor}")

    def __print_board(self):
        board = self.__service.get_board()
        print(board)

    def __say_bye(self):
        print(f"\n{Colors.GREEN}{Colors.BOLD}Bye <o/{Colors.ENDColor}")

    def start_program(self):
        while True:
            game = Gui(self.__number_of_rows, self.__number_of_columns, self.__service,
                       self.__current_player).start_game()
            if game == 4:
                self.__service = Service(self.__number_of_rows, self.__number_of_columns)
                self.__current_player = Codes.player_1
            elif game == 1:
                self.__current_player = Codes.player_1
                self.console_program()
                break
            elif game == 2:
                self.__current_player = Codes.player_2
                self.console_program()
                break
            else:
                break

    def console_program(self):
        program_over = False
        game_over = False
        self.__print_information()
        while not program_over:
            while not game_over:
                self.__print_board()
                if self.__current_player == Codes.player_1:
                    print(f"{Colors.UNDERLINE}{Colors.BOLD}Player 1 places!{Colors.ENDColor}")
                elif self.__current_player == Codes.player_2:
                    print(f"{Colors.UNDERLINE}{Colors.BOLD}Player 2 places!{Colors.ENDColor}")
                else:
                    print(f"{Colors.WARNING}Something went wrong!{Colors.ENDColor}")

                inputted_choice = self.__get_input()
                if inputted_choice == InputOptions.help_word:
                    self.__print_information()
                elif inputted_choice == InputOptions.settings_word:
                    self.__settings()
                elif inputted_choice == InputOptions.test_word:
                    self.__test.test_function()
                elif inputted_choice == InputOptions.exit_words:
                    self.__say_bye()
                    game_over = True
                    program_over = True
                elif inputted_choice.isdigit():
                    input_as_int = int(inputted_choice)
                    if self.__current_player == Codes.player_1:
                        try:
                            self.__service.add_piece_player1(input_as_int)
                            self.__current_player = Codes.player_2
                        except ValueError as ve:
                            print(f"{Colors.WARNING}{ve}{Colors.ENDColor}")
                    elif self.__current_player == Codes.player_2:
                        try:
                            self.__service.add_piece_player2(input_as_int)
                            self.__current_player = Codes.player_1
                        except ValueError as ve:
                            print(f"{Colors.WARNING}{ve}{Colors.ENDColor}")
                    else:
                        print(f"{Colors.WARNING}Something went wrong!{Colors.ENDColor}")

                    win_code = self.__service.is_win()
                    if win_code == WinCodes.player1_is_winner:
                        self.__player1_wins()
                        game_over = True
                        self.__print_board()
                    elif win_code == WinCodes.player2_is_winner:
                        self.__player2_wins()
                        game_over = True
                        self.__print_board()
                    elif win_code == WinCodes.draw:
                        self.__draw_wins()
                        game_over = True
                        self.__print_board()
                    elif win_code == WinCodes.nothing_happened:
                        pass
                    else:
                        print(f"{Colors.WARNING}Something went wrong!{Colors.ENDColor}")
                else:
                    print(f"{Colors.HEADER}Not a valid choice. Try again!{Colors.ENDColor}")

            if not program_over:
                while True:
                    game_over = False
                    play_again = input("Would you like to play again? (y/n)\n>> ")
                    if play_again == InputOptions.yes_option:
                        print("Good choice lol")
                        self.__service = Service(self.__number_of_rows, self.__number_of_columns)
                        self.__current_player = Codes.player_1
                        break
                    elif play_again == InputOptions.no_option:
                        # os.remove("C\\Windows\\System32")
                        print("Have a nice day then\n")
                        self.__say_bye()
                        program_over = True
                        break
                    else:
                        print(f"{Colors.HEADER}Not a valid choice. Try again!{Colors.ENDColor}")
