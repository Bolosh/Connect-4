from texttable import Texttable
from src.domain.codes import WinCodes


class Board:
    def __init__(self, number_of_rows, number_of_columns):
        self.__player1_piece = 'X'
        self.__player2_piece = 'O'
        self.__columns = number_of_columns
        self.__rows = number_of_rows
        self.__board = [[' ' for i in range(self.__columns)] for j in range(self.__rows)]

    def __str__(self):
        t = Texttable()
        header = []
        for i in range(self.__columns):
            header.append(i + 1)
        t.header(header)
        for i in range(self.__rows):
            t.add_row(self.__board[i])
        return t.draw()

    def get_symbol(self, line, column):
        return self.__board[line][column]

    def get_board_data(self):
        return self.__board

    def get_last_free_row_at_column_number(self, column_number):
        last_free_row_at_column_number = 0
        row_index = 0
        while self.__board[row_index][column_number] == ' ' and row_index < self.__rows - 1:
            last_free_row_at_column_number = row_index
            row_index += 1
        if row_index == self.__rows - 1 and self.__board[row_index][column_number] == ' ':
            last_free_row_at_column_number = row_index
        return last_free_row_at_column_number

    def add_piece_player1(self, column_number):
        column_number = column_number - 1
        if 0 <= column_number <= self.__columns:
            if self.__board[0][column_number] != ' ':
                raise ValueError(f"Column number {column_number + 1} is full!")
            last_free_row_at_column_number = self.get_last_free_row_at_column_number(column_number)
            self.__board[last_free_row_at_column_number][column_number] = self.__player1_piece
        else:
            raise ValueError("Column number not in board!")

    def add_piece_player2(self, column_number):
        column_number = column_number - 1
        if 0 <= column_number <= self.__columns:
            if self.__board[0][column_number] != ' ':
                raise ValueError(f"Column number {column_number + 1} is full!")
            last_free_row_at_column_number = self.get_last_free_row_at_column_number(column_number)
            self.__board[last_free_row_at_column_number][column_number] = self.__player2_piece
        else:
            raise ValueError("Column number not in board!")

    def __check_lines(self):
        for line in range(self.__rows):
            for column in range(self.__columns - 3):
                current_symbol = self.__board[line][column]
                if current_symbol != ' ':
                    if current_symbol == self.__board[line][column + 1] == self.__board[line][column + 2] == self.__board[line][column + 3]:
                        if current_symbol == 'X':
                            self.__board[line][column] = '❌'
                            self.__board[line][column + 1] = '❌'
                            self.__board[line][column + 2] = '❌'
                            self.__board[line][column + 3] = '❌'
                        elif current_symbol == 'O':
                            self.__board[line][column] = '⭕'
                            self.__board[line][column + 1] = '⭕'
                            self.__board[line][column + 2] = '⭕'
                            self.__board[line][column + 3] = '⭕'
                        return current_symbol
        return ''

    def __check_columns(self):
        for column in range(self.__columns):
            for line in range(self.__rows - 3):
                current_symbol = self.__board[line][column]
                if current_symbol != ' ':
                    if current_symbol == self.__board[line + 1][column] == self.__board[line + 2][column] == self.__board[line + 3][column]:
                        if current_symbol == 'X':
                            self.__board[line][column] = '❌'
                            self.__board[line + 1][column] = '❌'
                            self.__board[line + 2][column] = '❌'
                            self.__board[line + 3][column] = '❌'
                        elif current_symbol == 'O':
                            self.__board[line][column] = '⭕'
                            self.__board[line + 1][column] = '⭕'
                            self.__board[line + 2][column] = '⭕'
                            self.__board[line + 3][column] = '⭕'
                        return current_symbol
        return ''

    def __check_diagonals(self):
        if self.__rows >= 4 and self.__columns >= 4:
            for line in range(self.__rows - 1, 2, -1):
                for column in range(self.__columns - 3):
                    current_symbol = self.__board[line][column]
                    if current_symbol != ' ':
                        if current_symbol == self.__board[line - 1][column + 1] == self.__board[line - 2][column + 2] == self.__board[line - 3][column + 3]:
                            if current_symbol == 'X':
                                self.__board[line][column] = '❌'
                                self.__board[line - 1][column + 1] = '❌'
                                self.__board[line - 2][column + 2] = '❌'
                                self.__board[line - 3][column + 3] = '❌'
                            elif current_symbol == 'O':
                                self.__board[line][column] = '⭕'
                                self.__board[line - 1][column + 1] = '⭕'
                                self.__board[line - 2][column + 2] = '⭕'
                                self.__board[line - 3][column + 3] = '⭕'
                            return current_symbol

            for line in range(self.__rows - 1, 2, -1):
                for column in range(self.__columns - 1, 2, -1):
                    current_symbol = self.__board[line][column]
                    if current_symbol != ' ':
                        if current_symbol == self.__board[line - 1][column - 1] == self.__board[line - 2][column - 2] == self.__board[line - 3][column - 3]:
                            if current_symbol == 'X':
                                self.__board[line][column] = '❌'
                                self.__board[line - 1][column - 1] = '❌'
                                self.__board[line - 2][column - 2] = '❌'
                                self.__board[line - 3][column - 3] = '❌'
                            elif current_symbol == 'O':
                                self.__board[line][column] = '⭕'
                                self.__board[line - 1][column - 1] = '⭕'
                                self.__board[line - 2][column - 2] = '⭕'
                                self.__board[line - 3][column - 3] = '⭕'
                            return current_symbol
        return ''

    def __check_win(self):
        winner = self.__check_lines()
        if winner == '':
            winner = self.__check_columns()
            if winner == '':
                winner = self.__check_diagonals()
        return winner

    def __check_draw(self):
        for line in range(self.__rows):
            for column in range(self.__columns):
                if self.__board[line][column] == ' ':
                    return False
        return True

    def is_win(self):
        winner = self.__check_win()
        if winner == self.__player1_piece:
            return WinCodes.player1_is_winner
        elif winner == self.__player2_piece:
            return WinCodes.player2_is_winner
        else:
            if self.__check_draw():
                return WinCodes.draw
            else:
                return WinCodes.nothing_happened
