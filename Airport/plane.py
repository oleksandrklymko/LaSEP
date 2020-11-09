class Plain:

    def __init__(self, board_number, model):
        self.board_number = board_number
        self.model = model
        self.hours_worked = 0

    def __repr__(self):
        return 'Board number: ' + str(self.board_number)
