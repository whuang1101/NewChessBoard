class Piece:
    def __init__(self, color=None):
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

    # have to add an attack for this later
    def possible_moves(self, board, row, column):
        moves = []
        if self.name == "wp":
            if row - 1 >= 0:
                if board[row - 1][column].piece.name == "--":
                    moves.append((row - 1, column))
                    if row - 2 >= 0:
                        if board[row - 2][column].piece.name == "--" and self.move_count == 0:
                            moves.append((row - 2, column))
                if column + 1 <= 7:
                    if board[row - 1][column + 1].piece.name[0] == "b":
                        moves.append((row - 1, column + 1))
                if column - 1 >= 0:
                    if board[row - 1][column - 1].piece.name[0] == "b":
                        moves.append((row - 1, column - 1))
            return moves
        else:
            if row + 1 <= 8:
                if board[row + 1][column].piece.name == "--":
                    moves.append((row + 1, column))
                    if row + 2 >= 0:
                        if board[row + 2][column].piece.name == "--" and self.move_count == 0:
                            moves.append((row + 2, column))
            if column + 1 <= 7:
                if board[row + 1][column + 1].piece.name[0] == "w":
                    moves.append((row + 1, column + 1))
            if column - 1 >= 0:
                if board[row + 1][column - 1].piece.name[0] == "w":
                    moves.append((row + 1, column - 1))
                return moves

    def make_move(self, board, row, col, previous):
        board[row][col].piece = board[previous[0][0]][previous[0][1]].piece
        board[previous[0][0]][previous[0][1]].piece = Piece()
        self.move_count += 1


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wR"
        else:
            self.name = "bR"

    def possible_moves(self, board, row, column):
        moves = []
        if self.color == "white":
            for j in range(column + 1, 8):
                if board[row][j].piece.name == "--" or board[row][j].piece.name[0] == "b":
                    moves.append((row, j))
                    if board[row][j].piece.name[0] == "b":
                        break
                else:
                    break
            for j in range(column - 1, -1, -1):
                if board[row][j].piece.name == "--" or board[row][j].piece.name[0] == "b":
                    moves.append((row, j))
                    if board[row][j].piece.name[0] == "b":
                        break
                else:
                    break
            for i in range(row - 1, -1, -1):
                if board[i][column].piece.name == "--" or board[i][column].piece.name[0] == "b":
                    moves.append((i, column))
                    if board[i][column].piece.name[0] == "b":
                        break
                else:
                    break
            for i in range(row + 1, 8):
                if board[i][column].piece.name == "--" or board[i][column].piece.name[0] == "b":
                    moves.append((i, column))
                    if board[i][column].piece.name[0] == "b":
                        break
                else:
                    break
        else:
            for j in range(column + 1, 8):
                if board[row][j].piece.name == "--" or board[row][j].piece.name[0] == "w":
                    moves.append((row, j))
                    if board[row][j].piece.name[0] == "w":
                        break
                else:
                    break
            for j in range(column - 1, -1, -1):
                if board[row][j].piece.name == "--" or board[row][j].piece.name[0] == "w":
                    moves.append((row, j))
                    if board[row][j].piece.name[0] == "w":
                        break
                else:
                    break
            for i in range(row - 1, -1, -1):
                if board[i][column].piece.name == "--" or board[i][column].piece.name[0] == "w":
                    moves.append((i, column))
                    if board[i][column].piece.name[0] == "w":
                        break
                else:
                    break
            for i in range(row + 1, 8):
                if board[i][column].piece.name == "--" or board[i][column].piece.name[0] == "w":
                    moves.append((i, column))
                    if board[i][column].piece.name[0] == "w":
                        break
                else:
                    break
        return moves

    @staticmethod
    def make_move(board, row, col, previous):
        board[row][col].piece = board[previous[0][0]][previous[0][1]].piece
        board[previous[0][0]][previous[0][1]].piece = Piece()


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == "white":
            self.name = "wB"
        else:
            self.name = "bB"

    def possible_moves(self, board, row, column):
        moves = []
        a = 0
        if self.color == "white":
            for i in range(column + 1, 8):
                a += 1
                if row - a >= 0 and column + a < 8:
                    if board[row - a][column + a].piece.name == "--" or board[row - a][column + a].piece.name[0] == "b":
                        moves.append((row - a, column + a))
                        if board[row - a][column + a].piece.name[0] == "b":
                            break
                    else:
                        break
            a = 0
            for i in range(column - 1, -1, -1):
                a += 1
                if row - a >= 0 and column - a >= 0:
                    if board[row - a][column - a].piece.name == "--" or board[row - a][column - a].piece.name[0] == "b":
                        moves.append((row - a, column - a))
                        if board[row - a][column - a].piece.name[0] == "b":
                            break
                    else:
                        break
            a = 0
            for i in range(row + 1, 8):
                a += 1
                if row + a < 8 and column - a >= 0:
                    if board[row + a][column - a].piece.name == "--" or board[row + a][column - a].piece.name[0] == "b":
                        moves.append((row + a, column - a))
                        if board[row + a][column - a].piece.name[0] == "b":
                            break
                    else:
                        break
            a = 0
            for i in range(row - 1, -1, -1):
                a += 1
                if row+a < 8 and column +a < 8:
                    if board[row + a][column + a].piece.name == "--" or board[row + a][column + a].piece.name[0] == "b":
                        moves.append((row + a, column + a))
                        if board[row + a][column + a].piece.name[0] == "b":
                            break
                    else:
                        break
            return moves
        else:
            for i in range(column + 1, 8):
                a += 1
                if row - a >= 0 and column + a < 8:
                    if board[row - a][column + a].piece.name == "--" or board[row - a][column + a].piece.name[0] == "w":
                        moves.append((row - a, column + a))
                        if board[row - a][column + a].piece.name[0] == "w":
                            break
                    else:
                        break
            a = 0
            for i in range(column - 1, -1, -1):
                a += 1
                if row - a >= 0 and column - a >= 0:
                    if board[row - a][column - a].piece.name == "--" or board[row - a][column - a].piece.name[0] == "w":
                        moves.append((row - a, column - a))
                        if board[row - a][column - a].piece.name[0] == "w":
                            break
                    else:
                        break
            a = 0
            for i in range(row + 1, 8):
                a += 1
                if row + a < 8 and column - a >= 0:
                    if board[row + a][column - a].piece.name == "--" or board[row + a][column - a].piece.name[0] == "w":
                        moves.append((row + a, column - a))
                        if board[row + a][column - a].piece.name[0] == "w":
                            break
                    else:
                        break
            a = 0
            for i in range(row - 1, -1, -1):
                a += 1
                if row + a < 8 and column + a < 8:
                    if board[row + a][column + a].piece.name == "--" or board[row + a][column + a].piece.name[0] == "w":
                        moves.append((row + a, column + a))
                        if board[row + a][column + a].piece.name[0] == "w":
                            break
                    else:
                        break
            return moves

    @staticmethod
    def make_move(board, row, col, previous):
        board[row][col].piece = board[previous[0][0]][previous[0][1]].piece
        board[previous[0][0]][previous[0][1]].piece = Piece()


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
