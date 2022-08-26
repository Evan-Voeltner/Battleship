class GamePiece():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.appearance = '00'
        self.destroyed = False
