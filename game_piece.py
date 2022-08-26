class GamePiece():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.appearance = 'OO'
        self.destroyed = False
