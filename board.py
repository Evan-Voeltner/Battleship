from game_piece import GamePiece

class Board():
    def __init__(self):
        self.current_board = self.create_board()
        self.pieces = [GamePiece('Destroyer', 2), GamePiece('Submarine', 3), GamePiece('Battleship', 4), GamePiece('Aircraft Carrier', 5)]
        

    def create_board(self):
        new_board = []
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for letter in alphabet:
            new_row = []
            for number in range(1,11):
                new_row.append(f'{letter}{str(number)}')
            new_board.append(new_row)
        return new_board

    def print_board(self):
        for row in self.current_board:
            print(row)

my_board = Board()

my_board.print_board()