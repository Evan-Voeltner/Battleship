from turtle import position
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
            row_string = ''
            for item in row:
                if item[1:] == '10':
                    row_string += f'|{item}|'
                else:
                    row_string += f'|{item}'
            print(row_string)

    def get_all_possible_positions(self):
        all_positions = []
        for row in self.create_board():
            for item in row:
                all_positions.append(item)
        return all_positions

    def verify_position_input(self):
        user_input = input('Type Here: ').upper()
        # if len(user_input) != 2:
        #     print('That is not a valid position, type another.')
        #     user_input = self.verify_piece_placement_input()
        if user_input not in self.get_all_possible_positions():
            print('That is not a valid position, type another.')
            user_input = self.verify_position_input()
        return user_input

    def get_list_of_positions(self):
        print('What is the starting position?')
        starting_position = self.verify_position_input()
        print('What is the ending position?')
        ending_position = self.verify_position_input()
        positions_list = []
        if starting_position[0] == ending_position[0] or starting_position[1:] == ending_position[1:]:
            positions_list = [starting_position, ending_position]
        else:
            print("Those positions don't line up, please find different ones.")
            positions_list = self.get_list_of_positions()
        return positions_list


    def place_pieces(self):
        pieces_to_place = self.pieces.copy()
        for piece in pieces_to_place:
            piece_not_placed = True
            while piece_not_placed == True:
                piece_not_placed = False
                
                self.print_board()
                print(f'{piece.name} | {str(piece.size)}')
                positions_list = self.get_list_of_positions()
                start_position = positions_list[0]
                end_position = positions_list[1]

                if start_position[0] == end_position[0]:
                    total_spaces = abs(int(start_position[1:]) - int(end_position[1:])) + 1
                    if total_spaces == piece.size:
                        row_position = start_position[0]
                        column_position = int(start_position[1:])
                        for _ in range(total_spaces):
                            unchecked_position = (f'{row_position}{str(column_position)}')
                            if self.find_if_duplicate(unchecked_position):
                                print('One of these spaces are ocuppied!')
                                piece.positions = []
                                piece_not_placed = True
                                break
                            else:
                                piece.positions.append(unchecked_position)
                                column_position += 1
                        
                elif start_position[1:] == end_position[1:]:
                    total_spaces = abs((ord(start_position[0].lower()) - 96) - (ord(end_position[0].lower())- 96) ) + 1
                    if total_spaces == piece.size:
                        row_position = ord(start_position[0]) - 64
                        column_position = start_position[1:] 
                        for _ in range(total_spaces):
                            unchecked_position = (f'{chr(row_position + 96).capitalize()}{str(column_position)}')
                            if self.find_if_duplicate(unchecked_position):
                                print('One of these spaces are ocuppied!')
                                piece.positions = []
                                piece_not_placed = True
                                break
                            else:
                                piece.positions.append(unchecked_position)
                                row_position += 1
                           
                else:
                    print('Input not valid')

                for position in piece.positions:
                    self.draw_game_piece(position)

        self.print_board()
                
                
    def find_if_duplicate(self, position_to_check):
        for piece in self.pieces:
            for position in piece.positions:
                if position == position_to_check:
                    return True        

    def draw_game_piece(self, board_position_to_redraw):
        for row in self.current_board:
            for position in row:
                if position == board_position_to_redraw:
                    row[row.index(position)] = '()'
