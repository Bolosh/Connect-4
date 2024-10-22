import sys
import pygame
from pygame.locals import *
from src.domain.codes import Codes, WinCodes


class Colors:
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 234, 0)
    BLACK = (0, 0, 0)
    COOL_BLUE = (146, 244, 255)
    BROWN = (99, 77.5, 36.5)
    ORANGE = (255, 165, 0)
    VIOLET = (207, 159, 255)


class Gui:
    def add_piece(self, column):
        column -= 1
        row_index = self.service.get_last_available_row_at_column(column)
        board = self.service.get_board_data()
        if board[0][column] != ' ':
            self.rect_list.append(pygame.Rect(column * self.piece_size + 20 + 15, self.window_size[1] - self.rows * self.piece_size, 45, 5))
        else:
            self.rect_list.append(pygame.Rect(column * self.piece_size + 20 + 15, self.window_size[1] - (self.rows - row_index - 1) * self.piece_size - 5, 45, 5))

    def __init__(self, number_of_rows, number_of_columns, service, current_player):
        self.service = service
        self.__current_player = current_player
        self.rows = number_of_rows
        self.columns = number_of_columns
        self.game_over = -1
        self.program_over = False

        self.window_size = [1000, 800]
        self.piece_size = 80
        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption("Connect Four")
        self.screen = pygame.display.set_mode(self.window_size, 0, 32)

        self.piece_image = pygame.image.load('../assets/piece_red.png').convert_alpha()
        self.piece_mask = pygame.mask.from_surface(self.piece_image)
        self.piece_rect = self.piece_image.get_rect(center=(35, 35))

        self.player1_piece_image = pygame.image.load('../assets/piece_red.png').convert_alpha()
        self.player1_piece_mask = pygame.mask.from_surface(self.player1_piece_image)
        self.player1_piece_rect = self.player1_piece_image.get_rect(center=(35, 35))

        self.player2_piece_image = pygame.image.load('../assets/piece_yellow.png').convert_alpha()
        self.player2_piece_mask = pygame.mask.from_surface(self.player2_piece_image)
        self.player2_piece_rect = self.player2_piece_image.get_rect(center=(35, 35))

        self.background = pygame.image.load('../assets/background.png').convert_alpha()
        self.podium = pygame.image.load('../assets/podium.png').convert_alpha()
        self.table = pygame.image.load('../assets/table.png').convert_alpha()

        self.rect_list = []
        self.checker_rect = []

        self.offset = [0, 0]
        self.left_click = False

        self.vertical_momentum = 0.2
        self.horizontal_momentum = 0
        self.piece_velocity = 0

        self.help_menu_text = ["-> Clik and drag to aim and", "release to shoot.",
                               "-> Right click to reset piece position.",
                               "-> 'R' key to restart the game.",
                               "-> 'Esc' key to exit the game.",
                               "-> 'C' to play the game in console."]

        board_data = service.get_board_data()
        for line in range(self.rows - 1, -1, -1):
            for column in range(self.columns):
                if board_data[line][column] != ' ':
                    self.add_piece(column)

    def add_text(self, text, text_color, font_name, size, pos_x, pos_y):
        font = pygame.font.SysFont(font_name, size)
        text_image = font.render(text, True, text_color)
        self.screen.blit(text_image, (pos_x, pos_y))

    def add_rectangles_to_list(self):
        self.rect_list.append(pygame.Rect(20, self.window_size[1] - self.piece_size * self.rows, 1, self.piece_size * self.rows))
        for column in range(1, self.columns):
            self.rect_list.append(pygame.Rect(column * 80 + 19, self.window_size[1] - self.piece_size * self.rows, 2, self.piece_size * self.rows))
        self.rect_list.append(pygame.Rect(self.columns * 80 + 19, self.window_size[1] - self.piece_size * self.rows, 1, self.piece_size * self.rows))

        self.rect_list.append(pygame.Rect(self.window_size[0] - 400, self.window_size[1] - 330, 400, 330))
        self.rect_list.append(pygame.Rect(20, self.window_size[1] - 5, self.piece_size * self.columns, 5))

        self.rect_list.append(pygame.Rect(0, -1, self.window_size[0], 1))
        self.rect_list.append(pygame.Rect(0, self.window_size[1] + 1, self.window_size[0], 1))
        self.rect_list.append(pygame.Rect(-1, 0, 1, self.window_size[0]))
        self.rect_list.append(pygame.Rect(self.window_size[0] + 1, 0, 1, self.window_size[1]))

    def draw_board(self):
        pygame.draw.rect(self.screen, Colors.BLUE, pygame.Rect(20, self.window_size[1] - self.piece_size * self.rows, self.piece_size * self.columns, self.piece_size * self.rows))
        for line in range(self.rows):
            for column in range(self.columns):
                symbol = self.service.get_symbol(line, column)
                if symbol == 'X' or symbol == '❌':
                    self.screen.blit(self.player1_piece_image, ((column + 1) * self.piece_size + 20 - self.piece_size / 2 - 35, (line + 1) * self.piece_size + self.window_size[1] - self.piece_size * self.rows - self.piece_size / 2 - 35))
                elif symbol == 'O' or symbol == '⭕':
                    self.screen.blit(self.player2_piece_image, ((column + 1) * self.piece_size + 20 - self.piece_size / 2 - 35, (line + 1) * self.piece_size + self.window_size[1] - self.piece_size * self.rows - self.piece_size / 2 - 35))
                else:
                    if self.columns >= 7:
                        if line == column == 0:
                            pygame.draw.circle(self.screen, Colors.BROWN, ((column + 1) * self.piece_size + 20 - self.piece_size / 2, (line + 1) * self.piece_size + self.window_size[1] - self.piece_size * self.rows - self.piece_size / 2), self.piece_size / 2 - 5)
                        else:
                            pygame.draw.circle(self.screen, Colors.COOL_BLUE, ((column + 1) * self.piece_size + 20 - self.piece_size / 2, (line + 1) * self.piece_size + self.window_size[1] - self.piece_size * self.rows - self.piece_size / 2), self.piece_size / 2 - 5)
                    else:
                        pygame.draw.circle(self.screen, Colors.COOL_BLUE, ((column + 1) * self.piece_size + 20 - self.piece_size / 2, (line + 1) * self.piece_size + self.window_size[1] - self.piece_size * self.rows - self.piece_size / 2), self.piece_size / 2 - 5)

    def checker_rectangles(self):
        for column in range(self.columns):
            self.checker_rect.append(pygame.Rect(column * self.piece_size + 20 + 15, self.window_size[1] - self.rows * self.piece_size + 40, 45, 5))

    def check_column_with_checker_rectangles(self):
        index = 1
        for column_rect in self.checker_rect:
            if self.piece_rect.colliderect(column_rect):
                self.checker_rect = []
                return index
            index += 1
        return -1

    def check_collision(self):
        # Check collisions as rectangles
        hit_list = []
        for rectangle in self.rect_list:
            if rectangle.colliderect(self.piece_rect):
                hit_list.append(rectangle)
        return hit_list

        # Check collisions as circles
        # hit_list = []
        # for rectangle in self.rect_list:
        #     rect_mask = pygame.mask.from_surface(pygame.Surface((rectangle.width, rectangle.height)))
        #     if self.piece_mask.overlap(rect_mask, (rectangle.x - self.piece_rect.x, rectangle.y - self.piece_rect.y)):
        #         hit_list.append(rectangle)
        # return hit_list

    def move_check(self, movement):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.piece_rect.x += movement[0]
        hit_list = self.check_collision()
        for rectangle in hit_list:
            if movement[0] > 0:
                self.piece_rect.right = rectangle.left
                collision_types['right'] = True
            if movement[0] < 0:
                self.piece_rect.left = rectangle.right
                collision_types['left'] = True
        self.piece_rect.y += movement[1]
        hit_list = self.check_collision()
        for rectangle in hit_list:
            if movement[1] > 0:
                self.piece_rect.bottom = rectangle.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                self.piece_rect.top = rectangle.bottom
                collision_types['top'] = True
        return collision_types

    def set_momentum(self, mouse_now, mouse_initial):
        cx = mouse_now[0]  # Current x
        cy = mouse_now[1]  # Current y
        ix = mouse_initial[0]  # Initial x
        iy = mouse_initial[1]  # Initial y
        self.vertical_momentum += (iy - cy) / 10
        self.horizontal_momentum += (ix - cx) / 10

    def start_game(self):
        self.piece_rect.x, self.piece_rect.y = [700, 200]
        self.add_rectangles_to_list()
        self.checker_rectangles()
        first_scripted_bounce_vertical = False
        second_scripted_bounce_vertical = False
        help_menu_active = False
        in_column = False
        mouse_initial = []
        bounces_in_column = 0
        current_column = -1
        end_game = False
        while True:  # Game Loop ----------------------
            # Background
            self.screen.blit(self.background, (0, 0))
            self.draw_board()

            if end_game:
                self.screen.blit(self.podium, (self.window_size[0] - 400, self.window_size[1] - 330))

            else:
                self.screen.blit(self.table, (self.window_size[0] - 400, self.window_size[1] - 330))

            if help_menu_active:
                self.screen.blit(self.table, (self.window_size[0] - 400, self.window_size[1] - 330))
                self.add_text(self.help_menu_text[0], Colors.VIOLET, "Nirmala UI", 20, 630, 485)
                self.add_text(self.help_menu_text[1], Colors.VIOLET, "Nirmala UI", 20, 630, 510)
                self.add_text(self.help_menu_text[2], Colors.VIOLET, "Nirmala UI", 20, 630, 550)
                self.add_text(self.help_menu_text[3], Colors.VIOLET, "Nirmala UI", 20, 630, 600)
                self.add_text(self.help_menu_text[4], Colors.VIOLET, "Nirmala UI", 20, 630, 650)
                self.add_text(self.help_menu_text[5], Colors.VIOLET, "Nirmala UI", 20, 630, 700)
                self.add_text("* 'Esc' or 'H' to exit this menu.", Colors.ORANGE, "Nirmala UI", 20, 630, 750)
            else:
                self.add_text("'H' for help", Colors.VIOLET, "Agency FB", 30, 630, 750)
                self.add_text("'Esc' to exit", Colors.VIOLET, "Agency FB", 30, 860, 750)
                if self.game_over == WinCodes.nothing_happened:
                    if self.__current_player == Codes.player_1:
                        self.add_text("Player 1's turn!", Colors.RED, "Cascadia Code", 40, 690, 700)
                        self.screen.blit(self.player1_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))
                    elif self.__current_player == Codes.player_2:
                        self.add_text("Player 2's turn!", Colors.YELLOW, "Cascadia Code", 40, 690, 700)
                        self.screen.blit(self.player2_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))

            if self.__current_player == Codes.player_1:
                self.screen.blit(self.player1_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))
            elif self.__current_player == Codes.player_2:
                self.screen.blit(self.player2_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))

            if self.game_over == WinCodes.nothing_happened:
                self.game_over = self.service.is_win()

            if self.game_over == WinCodes.player1_is_winner:
                self.add_text("Player 1 wins!", Colors.ORANGE, "Elephant", 70, 500, 150)
                self.screen.blit(self.player1_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))
                if not help_menu_active:
                    self.screen.blit(self.player2_piece_image, (820, 554))
                end_game = True
            elif self.game_over == WinCodes.player2_is_winner:
                self.add_text("Player 2 wins!", Colors.ORANGE, "Elephant", 70, 500, 150)
                self.screen.blit(self.player2_piece_image, (self.piece_rect.x + self.offset[0], self.piece_rect.y + self.offset[1]))
                if not help_menu_active:
                    self.screen.blit(self.player1_piece_image, (820, 554))
                end_game = True
            elif self.game_over == WinCodes.draw:
                self.add_text("Draw :(", Colors.ORANGE, "Elephant", 70, 550, 150)
                pygame.draw.circle(self.screen, Colors.COOL_BLUE, (self.piece_rect.x + 35, self.piece_rect.y + 35), 36)
                if not help_menu_active:
                    self.screen.blit(self.player1_piece_image, (820, 554))
                    self.screen.blit(self.player2_piece_image, (900, 554))
                end_game = True

            # Physics ---------------------------------
            movement = [0, 0]
            movement[1] += self.vertical_momentum
            movement[0] += self.horizontal_momentum
            collisions = self.move_check(movement)

            # Max velocity
            if self.vertical_momentum > 8:
                self.vertical_momentum = 8
            if self.horizontal_momentum > 8:
                self.horizontal_momentum = 8

            # Check collisions
            if collisions['bottom'] or collisions['top']:
                self.vertical_momentum *= -0.4
                if abs(self.vertical_momentum) < 1.9:
                    if not first_scripted_bounce_vertical:
                        self.vertical_momentum = 1.3
                        movement[1] += self.vertical_momentum
                        first_scripted_bounce_vertical = True
                    elif not second_scripted_bounce_vertical:
                        self.vertical_momentum = -0.7
                        movement[1] += self.vertical_momentum
                        second_scripted_bounce_vertical = True
                    else:
                        self.vertical_momentum = 0
            else:
                self.vertical_momentum += 0.2

            if collisions['right'] or collisions['left']:
                self.horizontal_momentum *= -0.4

            if in_column and collisions['bottom']:
                bounces_in_column += 1

            # Add pieces -------------------------------------------------
            selected_column = self.check_column_with_checker_rectangles()
            if not in_column:
                if selected_column == -1:
                    self.checker_rectangles()
                else:
                    self.horizontal_momentum = 0
                    self.piece_rect.x = (selected_column - 1) * self.piece_size + 25
                    in_column = True
                    current_column = selected_column
            else:
                if bounces_in_column >= 6:
                    if self.__current_player == Codes.player_1:
                        self.piece_rect.x, self.piece_rect.y = [700, 200]
                        self.horizontal_momentum = 0
                        bounces_in_column = 0
                        in_column = False
                        try:
                            self.service.add_piece_player1(current_column)
                            self.add_piece(current_column)
                            self.__current_player = Codes.player_2
                        except ValueError as ve:
                            pass  # column full
                        self.checker_rectangles()
                    elif self.__current_player == Codes.player_2:
                        self.piece_rect.x, self.piece_rect.y = [700, 200]
                        self.horizontal_momentum = 0
                        bounces_in_column = 0
                        in_column = False
                        try:
                            self.service.add_piece_player2(current_column)
                            self.add_piece(current_column)
                            self.__current_player = Codes.player_1
                        except ValueError as ve:
                            pass  # column full
                        self.checker_rectangles()

            # Buttons
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if help_menu_active:
                            help_menu_active = False
                        else:
                            pygame.quit()
                            sys.exit()
                    if event.key == K_r:
                        return 4
                    if event.key == K_c:
                        pygame.quit()
                        if self.__current_player == Codes.player_1:
                            return 1
                        elif self.__current_player == Codes.player_2:
                            return 2
                        else:
                            return 9
                    if event.key == K_h:
                        if help_menu_active:
                            help_menu_active = False
                        else:
                            help_menu_active = True
                if not end_game:
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            mouse_initial = [mouse_x, mouse_y]
                            self.left_click = True
                        if event.button == 3:
                            self.piece_rect.x, self.piece_rect.y = [700, 200]
                            self.vertical_momentum = 0.2
                            self.horizontal_momentum = 0
                            bounces_in_column = 0
                            in_column = False
                    if event.type == MOUSEBUTTONUP:
                        if event.button == 1:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            mouse_now = [mouse_x, mouse_y]
                            self.set_momentum(mouse_now, mouse_initial)
                            self.left_click = False

            # Update
            pygame.display.flip()
            self.mainClock.tick(60)
