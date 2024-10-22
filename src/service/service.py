from src.domain.domain import Board


class Service:
    def __init__(self, number_of_rows, number_of_columns):
        self.__board = Board(number_of_rows, number_of_columns)

    def add_piece_player1(self, column_number):
        try:
            self.__board.add_piece_player1(column_number)
        except ValueError as ve:
            raise ValueError(ve)

    def add_piece_player2(self, column_number):
        try:
            self.__board.add_piece_player2(column_number)
        except ValueError as ve:
            raise ValueError(ve)

    def is_win(self):
        return self.__board.is_win()

    def get_board(self):
        return self.__board

    def get_board_data(self):
        return self.__board.get_board_data()

    def get_symbol(self, line, column):
        return self.__board.get_symbol(line, column)

    def get_last_available_row_at_column(self, column):
        return self.__board.get_last_free_row_at_column_number(column)
