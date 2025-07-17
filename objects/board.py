from pieces import NullPiece

class BoardRender():
    def __init__(self):
        pass

class Board(BoardRender):
    def __init__(self):
        super().__init__()

        self.board = [[NullPiece.ID for j in range(8)] for i in range(8)]

if __name__ == "__main__":
    board = Board()
    print(board.board)