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

    def place_pieces(self):
        pieces_to_place = self.pieces.copy()
        for piece in pieces_to_place:
            self.print_board()
            player_input = input('Where is the starting position and ending postion of the piece? Please type with a space (A1 A2)')
            positions_list = player_input.split()
            start_position = positions_list[0]
            end_position = positions_list[1]

            if start_position[0] == end_position[0]:
                total_spaces = abs(int(start_position[1]) - int(end_position[1])) + 1
                if total_spaces == piece.size:
                    row_position = start_position[0]
                    column_position = start_position[1]
                    for _ in range(total_spaces):
                        piece.positions.append(f'{row_position}{str(column_position)}')
                        column_position += 1
            

my_board = Board()

my_board.print_board()