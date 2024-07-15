from abc import abstractmethod


class Piece:
    @abstractmethod
    def __init__(self, type) -> None:
        self.type = type

    def __str__(self) -> str:
        return self.type


class XPiece(Piece):
    def __init__(self, type='X') -> None:
        super().__init__(type)


class OPiece(Piece):
    def __init__(self, type='O') -> None:
        super().__init__(type)


class Board:
    def __init__(self) -> None:
        self.board = [[' ' for j in range(3)] for i in range(3)]
        self.turn = 'O'

    def place_piece(self, row: int, col: int):
        if self.board[row][col] == ' ':
            self.board[row][col] = OPiece() if self.turn == 'O' else XPiece()
            result = self.is_winner()
            draw = self.is_full() and (not result)
            self.turn = 'X' if self.turn == 'O' else 'O'
            return True, result, draw
        print('This position is full')
        return False, False, False

    def is_winner(self):
        return self.check_rows_cols() or self.check_diagonally()

    def check_diagonally(self):
        main_diag = [self.board[0][0], self.board[1][1], self.board[2][2]]
        anti_diag = [self.board[0][2], self.board[1][1], self.board[2][0]]
        return all([j.__str__() == self.turn for j in main_diag]) or all([j.__str__() == self.turn for j in anti_diag])

    def check_rows_cols(self):
        for i in range(3):
            col = [self.board[0][i], self.board[1][i], self.board[2][i]]
            if all([j.__str__() == self.turn for j in self.board[i]]) or all([j.__str__() == self.turn for j in col]):
                return True

    def is_full(self):
        return all([j.__str__() != ' ' for i in self.board for j in i])
