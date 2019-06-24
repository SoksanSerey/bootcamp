# this is the program to generate for the 8 queens solution
class NQueens:
    # this class is used to generate all the possible solution for the 8 queens problem
    def __init__(self):
        self.size = 8
        self.result = 0

    def solution(self):
        """
        find all the solution for 8 queen problem and print the number of solution
        :return: result of possible solution that we can find
        """
        position = [-1] * self.size
        self.put_queen(position, 0)
        # print("Found", self.result, "solutions.")
        return self.result

    def put_queen(self, positions, target_row):
        """
        place queen on target_row by checking all 8 possible cases
        :param positions:
        :param target_row:
        """
        if target_row == self.size:
            # self.show_full_board(positions)
            self.result += 1
        else:
            # for all N columns positions try to place a queen
            for col in range(self.size):
                if self.check_place(positions, target_row, col):
                    positions[target_row] = col
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, occupies_rows, col):
        """
        check whether the given position is under occupies or not
        :param positions: place where we going to check
        :param occupies_rows: row that already intersect by other queen
        :param col: N of column
        :return: True is the it available to put and False if the cell already occupies
        """
        for i in range(occupies_rows):
            if positions[i] == col \
                    or positions[i] - i == col - occupies_rows \
                    or positions[i] + i == col + occupies_rows:
                return False
        return True

    def show_full_board(self, positions):
        # show the full NxN board
        for row in range(self.size):
            line = ""
            for col in range(self.size):
                if positions[row] == col:
                    line += 'Q '
                else:
                    line += '. '
            print(line)
        print("\n")

    def show_short_board(self, positions):
        # locate all the position that queen will be there that number is refer to the place that queen occupied
        line = ''
        for i in range(self.size):
            line += str(positions[i]) + ''
        print(line)


def queen_bonus():
    result = NQueens()
    return result.solution()


# print(queen_bonus())
