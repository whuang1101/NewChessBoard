from boardClass import Board
import pygame
import copy

square_size = 64
board_dimension = 512
images = {}


def load_images():
    pieces = ["wp", "bp", "bR", "wR", "wB", "bB", "wN", "bN", "wQ", "bQ", "bK", "wK"]
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(piece + ".png"), (square_size, square_size))


def draw_squares(display):
    for row in range(8):
        for col in range(8):
            if row % 2 == 0 and col % 2 == 1 or row % 2 == 1 and col % 2 == 0:
                pygame.draw.rect(display, (118, 150, 86),
                                 pygame.Rect(row * square_size, col * square_size, square_size, square_size))
            else:
                pygame.draw.rect(display, (238, 238, 210),
                                 pygame.Rect(row * square_size, col * square_size, square_size, square_size))


def draw_pieces(display, board):
    for row in range(8):
        for col in range(8):
            if board[row][col].piece.name != "--":
                display.blit(images[board[row][col].piece.name],
                             pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# row and column need to be switched for any type of printing to board


if __name__ == "__main__":
    chess_board = Board()
    chess_board.print_board()
    load_images()
    chess_display = pygame.display.set_mode((board_dimension, board_dimension))
    chess_open = True
    yellow_size = (64, 64)
    yellow_surface = pygame.Surface(yellow_size, pygame.SRCALPHA)
    yellow_surface.fill((255, 255, 0, 128))
    red_surface = pygame.Surface(yellow_size, pygame.SRCALPHA)
    red_surface.fill((255, 0, 0, 128))
    frames = pygame.time.Clock()
    moves = []
    player = 1
    previous_click = []
    board_states = [copy.deepcopy(chess_board.board)]
    while chess_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chess_open = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # have to use cols, rows because of the way pygame starts at the top left instead of the bottom right.
                col, row = pygame.mouse.get_pos()
                row = int(row/ square_size)
                col = int(col/square_size)
                if len(moves) != 0:
                    for i, j in moves:
                        if i == row and j == col:
                            chess_board.board[previous_click[0][0]][previous_click[0][1]].piece.make_move(chess_board.
                                                                                                          board, i, j, previous_click)
                            board_states.append(copy.deepcopy(chess_board.board))
                            player += 1
                    moves.clear()
                elif chess_board.board[row][col].piece.name != "--":
                    previous_click.clear()
                    if player % 2 == 1 and chess_board.board[row][col].piece.name[0] == "w":
                        if chess_board.get_king_position("white") in chess_board.all_possible_moves(player+1):
                            new_row, new_col = chess_board.get_king_position("white")
                            chess_board.board[new_row][new_col].piece.set_check_status()
                        else:
                            moves = chess_board.board[row][col].piece.possible_moves(chess_board.board, row, col)
                            print(chess_board.get_king_position("white"))
                            print(chess_board.get_king_position("white") in chess_board.all_possible_moves(player+1))
                            print(chess_board.all_possible_moves(player+1))
                    if player % 2 == 0 and chess_board.board[row][col].piece.name[0] == "b":
                        moves = chess_board.board[row][col].piece.possible_moves(chess_board.board, row, col)

                    previous_click.append([row, col])
        draw_squares(chess_display)
        draw_pieces(chess_display, chess_board.board)
        new_row, new_col = chess_board.get_king_position("white")
        if chess_board.board[new_row][new_col].piece.in_check:
            pass
        else:
            if len(moves) != 0:
                for col, row in moves:
                    if chess_board.board[col][row].piece.name == "--":
                        yellow_squares = (row*64, col*64)
                        chess_display.blit(yellow_surface, yellow_squares)
                    elif chess_board.board[col][row].piece.name[0] == "b" or chess_board.board[col][row].piece.name[0] == "w":
                        red_squares = (row*64, col*64)
                        chess_display.blit(red_surface, red_squares)

            pygame.display.update()
            frames.tick(60)
            pygame.display.flip()
    for name in board_states:
        for i in range(len(name)):
            for j in range(len(name[i])):
                print(name[i][j].piece.name, end=" ")
            print()