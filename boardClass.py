import pygame


class Piece:
    def __init__(self, color):
        self.color = color
        self.name = "--"


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wp"
        else:
            self.name = "bp"


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wR"
        else:
            self.name = "bR"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wB"
        else:
            self.name = "bB"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wN"
        else:
            self.name = "bN"


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wQ"
        else:
            self.name = "bQ"


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wK"
        else:
            self.name = "bK"


class Board:
    class Cell:
        def __init__(self, row, col):
            self.piece = Piece("white")
            self.row = row
            self.col = col

    def __init__(self):
        self.board = []
        for row in range(8):
            add = []
            for col in range(8):
                add.append(Board.Cell(row, col))

            self.board.append(add)
        for row in range(8):
            for col in range(8):
                if row == 1:
                    self.board[row][col].piece = Pawn("black")
                elif row == 6:
                    self.board[row][col].piece = Pawn("white")
        self.board[0][0].piece = Rook("black")
        self.board[0][1].piece = Bishop("black")
        self.board[0][2].piece = Knight("black")
        self.board[0][3].piece = Queen("black")
        self.board[0][4].piece = King("black")
        self.board[0][5].piece = Knight("black")
        self.board[0][6].piece = Bishop("black")
        self.board[0][7].piece = Rook("black")
        self.board[7][0].piece = Rook("white")
        self.board[7][1].piece = Bishop("white")
        self.board[7][2].piece = Knight("white")
        self.board[7][3].piece = Queen("white")
        self.board[7][4].piece = King("white")
        self.board[7][5].piece = Knight("white")
        self.board[7][6].piece = Bishop("white")
        self.board[7][7].piece = Rook("white")

    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col].piece.name, end=" ")
            print()

        else:
            self.name = "bR"


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wB"
        else:
            self.name = "bB"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wN"
        else:
            self.name = "bN"


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wQ"
        else:
            self.name = "bQ"


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wK"
        else:
            self.name = "bK"


class Board:
    class Cell:
        def __init__(self, row, col):
            self.piece = Piece("white")
            self.row = row
            self.col = col

    def __init__(self):
        self.board = []
        for row in range(8):
            add = []
            for col in range(8):
                add.append(Board.Cell(row, col))

            self.board.append(add)
        for row in range(8):
            for col in range(8):
                if row == 1:
                    self.board[row][col].piece = Pawn("black")
                elif row == 6:
                    self.board[row][col].piece = Pawn("white")
        self.board[0][0].piece = Rook("black")
        self.board[0][1].piece = Bishop("black")
        self.board[0][2].piece = Knight("black")
        self.board[0][3].piece = Queen("black")
        self.board[0][4].piece = King("black")
        self.board[0][5].piece = Knight("black")
        self.board[0][6].piece = Bishop("black")
        self.board[0][7].piece = Rook("black")
        self.board[7][0].piece = Rook("white")
        self.board[7][1].piece = Bishop("white")
        self.board[7][2].piece = Knight("white")
        self.board[7][3].piece = Queen("white")
        self.board[7][4].piece = King("white")
        self.board[7][5].piece = Knight("white")
        self.board[7][6].piece = Bishop("white")
        self.board[7][7].piece = Rook("white")

    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col].piece.name, end=" ")
            print()

            
