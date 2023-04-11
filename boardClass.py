import pygame


class Board:
    class Cell:
        def __init__(self):
            self.piece = " "
            self.background_color = " "
            self.x = 0
            self.y = 0

    def __init__(self):
        self.board = []
        self.player = 1
        for i in range(0, 8):
            oneDlist = []
            for j in range(0, 8):
                oneDlist.append(self.Cell())
            self.board.append(oneDlist)
        for i in range(1, 7, 5):
            for j in range(0, 8):
                if i == 1:
                    self.board[j][i].piece = "bp"
                if i == 6:
                    self.board[j][i].piece = "wp"
        self.board[0][0].piece = "bR"
        self.board[1][0].piece = "bB"
        self.board[2][0].piece = "bN"
        self.board[3][0].piece = "bQ"
        self.board[4][0].piece = "bK"
        self.board[5][0].piece = "bN"
        self.board[6][0].piece = "bB"
        self.board[7][0].piece = "bR"
        self.board[0][7].piece = "wR"
        self.board[1][7].piece = "wB"
        self.board[2][7].piece = "wN"
        self.board[3][7].piece = "wQ"
        self.board[4][7].piece = "wK"
        self.board[5][7].piece = "wN"
        self.board[6][7].piece = "wB"
        self.board[7][7].piece = "wR"
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

    def move_pawn(self, x, y):
        x = x
        y = y
        print(x, y)
        if self.board[x][y] == "wp":
            self.board[x][y] = "-"
            if self.player == 1:
                self.board[x-2][y] = "wp"



