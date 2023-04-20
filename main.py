import boardClass
from boardClass import Board
import pygame


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


if __name__ == "__main__":
    chess_board = Board()
    chess_board.print_board()
    load_images()
    chess_display = pygame.display.set_mode((board_dimension, board_dimension))
    chess_open = True
    while chess_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chess_open = False
        draw_squares(chess_display)
        draw_pieces(chess_display, chess_board.board)
        pygame.display.flip()
