from player import Player

class PlayArea:
    def __init__(self):
        self.player_one = Player(1)
        self.player_one = Player(2)


    def play_game(self):
        self.player_one.board.place_pieces()
