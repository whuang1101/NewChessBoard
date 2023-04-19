import boardClass
from boardClass import Board
import pygame

pygame.init()


X = 560
Y = 560

# initializing white chess images
white_pawn = pygame.image.load("wp.png")
white_pawn = pygame.transform.rotate(white_pawn, 270)
white_rook = pygame.image.load("wR.png")
white_rook = pygame.transform.rotate(white_rook, 270)
white_bishop = pygame.image.load("wB.png")
white_bishop = pygame.transform.rotate(white_bishop, 270)
white_knight = pygame.image.load("wN.png")
white_knight = pygame.transform.rotate(white_knight, 270)
white_queen = pygame.image.load("wQ.png")
white_queen = pygame.transform.rotate(white_queen, 270)
white_king = pygame.image.load("wK.png")
white_king = pygame.transform.rotate(white_king, 270)
black_pawn = pygame.image.load("bp.png")
black_pawn = pygame.transform.rotate(black_pawn, 270)
black_rook = pygame.image.load("bR.png")
black_rook = pygame.transform.rotate(black_rook, 270)
black_bishop = pygame.image.load("bB.png")
black_bishop = pygame.transform.rotate(black_bishop, 270)
black_knight = pygame.image.load("bN.png")
black_knight = pygame.transform.rotate(black_knight, 270)
black_queen = pygame.image.load("bQ.png")
black_queen = pygame.transform.rotate(black_queen, 270)
black_king = pygame.image.load("bK.png")
black_king = pygame.transform.rotate(black_king, 270)


chess_display = pygame.display.set_mode((X, Y))
chessBoard = Board()
chessBoard.print_board()
while True:
    current_board = chessBoard.get_board()
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
                        print(chessBoard.board[i][j].piece.name)
                        if chessBoard.board[i][j].piece.name != " ":
                            moves = chessBoard.board[i][j].piece.possible_moves(current_board)

#
#         # this prints all the pieces on the board
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

                if chessBoard.board[i][j].piece.name == "pawn" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_pawn, piece_rect)
                elif chessBoard.board[i][j].piece.name == "pawn" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_pawn, piece_rect)
                elif chessBoard.board[i][j].piece.name == "rook" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_rook, piece_rect)
                elif chessBoard.board[i][j].piece.name == "knight" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_knight, piece_rect)
                elif chessBoard.board[i][j].piece.name == "queen" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_queen, piece_rect)
                elif chessBoard.board[i][j].piece.name == "bishop" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_bishop, piece_rect)
                elif chessBoard.board[i][j].piece.name == "king" and chessBoard.board[i][j].piece.color == "white":
                    chess_display.blit(white_king, piece_rect)
                elif chessBoard.board[i][j].piece.name == "rook" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_rook, piece_rect)
                elif chessBoard.board[i][j].piece.name == "bishop" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_bishop, piece_rect)
                elif chessBoard.board[i][j].piece.name == "knight" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_knight, piece_rect)
                elif chessBoard.board[i][j].piece.name == "queen" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_queen, piece_rect)
                elif chessBoard.board[i][j].piece.name == "king" and chessBoard.board[i][j].piece.color == "black":
                    chess_display.blit(black_king, piece_rect)

        rotated_surface = pygame.Surface(chess_display.get_size(), pygame.SRCALPHA)
        rotated_surface.blit(chess_display, (0, 0))
        rotated_surface = pygame.transform.rotate(rotated_surface, 90)
        chess_display.blit(rotated_surface, (0, 0))

        pygame.display.flip()

