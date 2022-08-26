class Board():
    def __init__(self):
        self.current_board = []
        

    def create_board(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for letter in alphabet:
            new_row = []
            for number in range(1,11):
                new_row.append(f'{letter}{str(number)}')
            self.current_board.append(new_row)

