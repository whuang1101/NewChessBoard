import pygame


class Piece:
    def __init__(self, color):
        self.name = None
        self.color = color


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "pawn"


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "rook"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "knight"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "bishop"


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "queen"


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "king"


class Board:
    class Cell:
        def __init__(self):
            self.piece = Piece("none")
            self.background_color = " "
            self.x = 0
            self.y = 0

    def __init__(self):
        self.board = []
        self.player = 1
        for i in range(0, 8):
            one_dlist = []
            for j in range(0, 8):
                one_dlist.append(self.Cell())
            self.board.append(one_dlist)
        for i in range(1, 7, 5):
            for j in range(0, 8):
                if i == 1:
                    self.board[j][i].piece = Pawn("black")
                if i == 6:
                    self.board[j][i].piece = Pawn("white")
        self.board[0][0].piece = Rook("black")
        self.board[1][0].piece = Bishop("black")
        self.board[2][0].piece = Knight("black")
        self.board[3][0].piece = Queen("black")
        self.board[4][0].piece = King("black")
        self.board[5][0].piece = Knight("black")
        self.board[6][0].piece = Bishop("black")
        self.board[7][0].piece = Rook("black")
        self.board[0][7].piece = Rook("white")
        self.board[1][7].piece = Bishop("white")
        self.board[2][7].piece = Knight("white")
        self.board[3][7].piece = Queen("white")
        self.board[4][7].piece = King("white")
        self.board[5][7].piece = Knight("white")
        self.board[6][7].piece = Bishop("white")
        self.board[7][7].piece = Rook("white")
        for i in range(0, 8):
            for j in range(0, 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.board[i][j].background_color = "white"
                        self.board[i][j].x = 70 * i
                        self.board[i][j].y = 70 * j
                    else:
                        self.board[i][j].background_color = "black"
                        self.board[i][j].x = 70 * i
                        self.board[i][j].y = 70 * j
                elif i % 2 == 1:
                    if j % 2 == 0:
                        self.board[i][j].background_color = "black"
                        self.board[i][j].x = 70 * i
                        self.board[i][j].y = 70 * j
                    else:
                        self.board[i][j].background_color = "white"
                        self.board[i][j].x = 70 * i
                        self.board[i][j].y = 70 * j

        self.player = 1

    def set_player(self, a):  # makes it so that it is either player one or 2;
        self.player = a

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j].piece, end=" ")
            print()
