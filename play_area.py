from player import Player

class PlayArea:
    def __init__(self):
        self.player_one = Player(1)
        self.player_two = Player(2)


    def play_game(self):
        self.player_one.player_board.place_pieces()
        self.player_two.player_board.place_pieces()

        
