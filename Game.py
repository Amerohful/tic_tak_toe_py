class Game:

    def __init__(self):
        self.order = 0  # type: int
        self.R = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]

    def check_win(self):
        for i in range(3):
            if self.R[i] == ['x', 'x', 'x']:
                return 1
            elif self.R[i] == ['o', 'o', 'o']:
                return 2
            elif [x[i] for x in self.R] == ['x', 'x', 'x']:
                return 1
            elif [x[i] for x in self.R] == ['o', 'o', 'o']:
                return 2
            elif [self.R[x][x] for x in range(3)] == ['x', 'x', 'x'] or \
                    [self.R[0][2], self.R[1][1], self.R[2][0]] == ['x', 'x', 'x']:
                return 1
            elif [self.R[0][0], self.R[1][1], self.R[2][2]] == ['o', 'o', 'o'] or \
                    [self.R[0][2], self.R[1][1], self.R[2][0]] == ['o', 'o', 'o']:
                return 2
        else:
            return 0

    def getOrder(self):
        return self.order

    def set_input(self, row: int, col: int):
        if self.R[row][col] != ' ':
            print("Error enter!!")
            return
        self.R[row][col] = 'x' if self.order % 2 == 0 else 'o'
        self.order += 1
        # if self.order > 4:
        #     if self.check_win() == 1:
        #         print("first win!!")
        #         self.next_game()
        #         return 1
        #     elif self.check_win() == 2:
        #         print("second win!!")
        #         self.next_game()
        #         return 2
        #     elif self.order == 9 and self.check_win() == 0:
        #         print("no winners")
        #         self.next_game()
        #         return 3

    def next_game(self):
        self.order = 0  # type: int
        self.R = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]
    #
    # def show_field(self):
    #     return self.R
print()

if __name__ == '__main__':
    a = Game()
    while True:
        # for i in range(3):
        #     print('|' + a.show_field()[i][0] + '|' + a.show_field()[i][1] + '|' + a.show_field()[i][2] + '|')
        i = input('Enter chose: ')
        if i == '1':
            a.set_input(0, 0)
        elif i == '2':
            a.set_input(0, 1)
        elif i == '3':
            a.set_input(0, 2)
        elif i == '4':
            a.set_input(1, 0)
        elif i == '5':
            a.set_input(1, 1)
        elif i == '6':
            a.set_input(1, 2)
        elif i == '7':
            a.set_input(2, 0)
        elif i == '8':
            a.set_input(2, 1)
        elif i == '9':
            a.set_input(2, 2)