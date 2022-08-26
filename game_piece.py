class GamePiece():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.position = []
        self.appearance = 'OO'
        self.destroyed = False
