from pieceClass import Piece, Queen, King, Pawn, Rook, Bishop, Knight


class Board:
    class Cell:
        def __init__(self, row, col):
            self.piece = Piece()
            self.row = row
            self.col = col

    def __init__(self, board=None):
        self.status = []
        if board is not None:
            self.board = board
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

    def get_board(self):
        return self.board

    def update_status(self,current_board):
        # create a new instance of Board
        self.status.append(current_board)
