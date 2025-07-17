class PieceRender():
    def __init__(self):
        pass

class Piece(PieceRender):
    def __init__(self):
        super().__init__()

class NullPiece(Piece):
    ID = 0

    def __init__(self):
        super().__init__()