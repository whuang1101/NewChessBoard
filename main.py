import boardClass
from boardClass import Board
import pygame

pygame.init()


X = 560
Y = 560

# initializing white chess images
white_pawn = pygame.image.load("wp.png")
white_rook = pygame.image.load("wR.png")
white_bishop = pygame.image.load("wB.png")
white_knight = pygame.image.load("wN.png")
white_queen = pygame.image.load("wQ.png")
white_king = pygame.image.load("wK.png")

black_pawn = pygame.image.load("bp.png")
black_rook = pygame.image.load("bR.png")
black_bishop = pygame.image.load("bB.png")
black_knight = pygame.image.load("bN.png")
black_queen = pygame.image.load("bQ.png")
black_king = pygame.image.load("bK.png")


chess_display = pygame.display.set_mode((X, Y))
chessBoard = Board()
while True:
    pygame.display.set_caption("Chess Game")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(0, 8):
                for j in range(0, 8):
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if((i + 1) * 70 >= mouse_y >= i * 70) and (j * 70 <= mouse_x <= (j + 1) * 70):
                        print(chr(97+i), j+1)

        # this prints all the pieces on the board
        for i in range(0, 8):
            for j in range(0, 8):
                piece_rect = white_pawn.get_rect()
                piece_rect.x = chessBoard.board[i][j].x + 4
                piece_rect.y = chessBoard.board[i][j].y + 4
                if chessBoard.board[i][j].background_color == "white":
                    rect = pygame.Rect(chessBoard.board[i][j].x, chessBoard.board[i][j].y, 70, 70)
                    pygame.draw.rect(chess_display, [235, 236, 211], rect)

                if chessBoard.board[i][j].background_color == "black":
                    rect = pygame.Rect(chessBoard.board[i][j].x, chessBoard.board[i][j].y, 70, 70)
                    pygame.draw.rect(chess_display, [125, 148, 93], rect)

                if chessBoard.board[i][j].piece == "wp":
                    chess_display.blit(white_pawn, piece_rect)
                elif chessBoard.board[i][j].piece == "bp":
                    chess_display.blit(black_pawn, piece_rect)
                elif chessBoard.board[i][j].piece == "wR":
                    chess_display.blit(white_rook, piece_rect)
                elif chessBoard.board[i][j].piece == "wN":
                    chess_display.blit(white_knight, piece_rect)
                elif chessBoard.board[i][j].piece == "wQ":
                    chess_display.blit(white_queen, piece_rect)
                elif chessBoard.board[i][j].piece == "wB":
                    chess_display.blit(white_bishop, piece_rect)
                elif chessBoard.board[i][j].piece == "wK":
                    chess_display.blit(white_king, piece_rect)
                elif chessBoard.board[i][j].piece == "bR":
                    chess_display.blit(black_rook, piece_rect)
                elif chessBoard.board[i][j].piece == "bB":
                    chess_display.blit(black_bishop, piece_rect)
                elif chessBoard.board[i][j].piece == "bN":
                    chess_display.blit(black_knight, piece_rect)
                elif chessBoard.board[i][j].piece == "bQ":
                    chess_display.blit(black_queen, piece_rect)
                elif chessBoard.board[i][j].piece == "bK":
                    chess_display.blit(black_king, piece_rect)

        pygame.display.flip()

