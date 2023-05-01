from pieceClass import Piece, Queen, King, Pawn, Rook, Bishop, Knight
import copy

class Board():
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
        self.board[0][1].piece = Knight("black")
        self.board[0][2].piece = Bishop("black")
        self.board[0][3].piece = Queen("black")
        self.board[0][4].piece = King("black")
        self.board[0][5].piece = Bishop("black")
        self.board[0][6].piece = Knight("black")
        self.board[0][7].piece = Rook("black")
        self.board[7][0].piece = Rook("white")
        self.board[7][1].piece = Knight("white")
        self.board[7][2].piece = Bishop("white")
        self.board[7][3].piece = Queen("white")
        self.board[7][4].piece = King("white")
        self.board[7][5].piece = Bishop("white")
        self.board[7][6].piece = Knight("white")
        self.board[7][7].piece = Rook("white")

    def print_board(self):
        for row in range(8):
            for col in range(8):
                print(self.board[row][col].piece.name, end=" ")
            print()

    def get_board(self):
        return self.board

    def update_status(self, current_board):
        # create a new instance of Board
        self.status.append(current_board)

    def all_possible_moves(self, player_number):
        moves = []
        if player_number % 2 == 1:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j].piece.name != "--" and self.board[i][j].piece.color == "white":
                        moves += self.board[i][j].piece.possible_moves(self.board, i, j)
            return moves
        else:
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j].piece.name != "--" and self.board[i][j].piece.color == "black":
                        moves += self.board[i][j].piece.possible_moves(self.board, i, j)
            return moves

    def check_moves(self,player_number,board):
        current_position = []
        moves = []
        move_dict = {}
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                previous_move = [[i, j]]
                if player_number == 1:
                    new_board = copy.deepcopy(board)
                    if new_board.board[i][j].piece.name[0] == "w":
                        piece_moves = new_board.board[i][j].piece.possible_moves(new_board.board,i,j)
                        move_dict[(i, j)] = []
                        for move in piece_moves:
                            new_board = copy.deepcopy(board)
                            new_board.board[i][j].piece.make_move(new_board.board,move[0],move[1],previous_move)
                            if new_board.get_king_position("white") not in new_board.all_possible_moves(2):
                                moves.append(move)
                                move_dict[(i,j)].append(move)
                else:
                    new_board = copy.deepcopy(board)
                    if new_board.board[i][j].piece.name[0] == "b":
                        piece_moves = new_board.board[i][j].piece.possible_moves(new_board.board,i,j)
                        move_dict[(i, j)] = []
                        for move in piece_moves:
                            new_board = copy.deepcopy(board)
                            new_board.board[i][j].piece.make_move(new_board.board,move[0],move[1],previous_move)
                            if new_board.get_king_position("black") not in new_board.all_possible_moves(1):
                                moves.append(move)
                                move_dict[(i,j)].append(move)
        move_dict = {k: v for k, v in filter(lambda item: item[1], move_dict.items())}


        del new_board
        return moves, move_dict



    def get_king_position(self, color):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if color == "white":
                    if self.board[i][j].piece.name == "wK":
                        move = (i, j)
                        return move
                else:
                    if self.board[i][j].piece.name == "bK":
                        move = (i,j)
                        return move
