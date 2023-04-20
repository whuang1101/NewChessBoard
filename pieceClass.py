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
        self.move_count = 0

    def possible_moves(self, board, row, column):
        moves = []
        if self.name == "wp":
            if board[row - 1][column].piece.name == "--":
                moves.append((row - 1, column))
            else:
                return moves
            if board[row - 2][column].piece.name == "--" and self.move_count == 0:
                moves.append((row - 2, column))
            return moves
        else:
            if board[row + 1][column].piece.name == "--":
                moves.append((row + 1, column))
            else:
                return moves
            if board[row + 2][column].piece.name == "--" and self.move_count == 0:
                moves.append((row + 2, column))
            return moves

    def make_move(self, board, row, col, previous):
        board[row][col].piece = board[previous[0][0]][previous[0][1]].piece
        board[previous[0][0]][previous[0][1]].piece = Piece("white")
        self.move_count += 1


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
