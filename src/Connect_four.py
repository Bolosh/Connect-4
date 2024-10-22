from src.ui.ui import UserInterface
from src.domain.codes import Codes


if __name__ == "__main__":
    user_interface = UserInterface(Codes.standard_number_of_rows, Codes.standard_number_of_columns)
    user_interface.start_program()
