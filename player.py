from board import Board

class Player:
    def __init__(self, player_num):
        self.player_number = player_num
        self.player_board = Board()
        self.opponent_board = Board()
        self.hits = 0
        self.misses = 0