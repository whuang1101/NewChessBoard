import pygame


class Piece:
    def __init__(self, color, row, column):
        self.name = " "
        self.color = color
        self.row = row
        self.column = column

    def move_piece(self, row, column):
        self.row = row
        self.column = column


class Pawn(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "pawn"
        self.original_row = self.row
        self.original_column = self.column

    def possible_moves(self, board):
        moves = []
        if self.color == "white" and (self.row == self.original_row and self.column == self.original_column):
            if board[self.row][self.column] == board[self.row-1][self.column]:
                move = [self.row-1,self.column]
                moves.append(move)
                if board[self.row][self.column] == board[self.row - 2][self.column]:
                    move = [self.row - 2, self.column]
                    moves.append(move)
        elif self.color == "white":
            if board[self.row][self.column] == board[self.row-1][self.column]:
                move = [self.row-1, self.column]
                moves.append(move)
        return moves


class Rook(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "rook"


class Knight(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "knight"


class Bishop(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "bishop"


class Queen(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "queen"


class King(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.name = "king"


class Board:
    class Cell:
        def __init__(self):
            self.piece = Piece(" ", 0, 0)
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
                    self.board[i][j].piece = Pawn("black", j, j)
                if i == 6:
                    self.board[i][j].piece = Pawn("white", i, j)
        self.board[0][0].piece = Rook("black", 0, 0)
        self.board[0][1].piece = Bishop("black", 1, 0)
        self.board[0][2].piece = Knight("black", 2, 0)
        self.board[0][3].piece = Queen("black", 3, 0)
        self.board[0][4].piece = King("black", 4, 0)
        self.board[0][5].piece = Knight("black", 5, 0)
        self.board[0][6].piece = Bishop("black", 6, 0)
        self.board[0][7].piece = Rook("black", 7, 0)
        self.board[7][0].piece = Rook("white", 0, 7)
        self.board[7][1].piece = Bishop("white", 1, 7)
        self.board[7][2].piece = Knight("white", 2, 7)
        self.board[7][3].piece = Queen("white", 3, 7)
        self.board[7][4].piece = King("white", 4, 7)
        self.board[7][5].piece = Knight("white", 5, 7)
        self.board[7][6].piece = Bishop("white", 6, 7)
        self.board[7][7].piece = Rook("white", 7, 7)
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

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j].piece.name, end=" ")
            print()
