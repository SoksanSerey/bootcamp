# this function will take 2 dimensional list as parameter
def sudoku(board):
    dummy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # check whether the line and col have 9x9 or not
    def check_line_col_format(board_check):
        count = 0
        if len(board_check) == 9:
            for i in range(0, 9):
                if len(board_check[i]) == 9:
                    count += 1
            if count == 9:
                return check_value_format(board_check)
            else:
                return True
        else:
            return True

    # check the value of the sudoku that must be between 1-9
    def check_value_format(board_check):
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if board_check[i][j] in dummy_list:
                    count += 1
        if count == 81:
            return False
        else:
            return True

    # check each line of the sudoku have duplicate value or not
    def check_line_completion(board_check):
        count = 0
        for i in range(0, 9):
            if len(board_check[i]) == len(set(board_check[i])):
                count += 1
            else:
                continue
        if count == 9:
            return False
        else:
            return True

    # check each column has duplicate value or not
    def check_column_completion(board_check):
        new_list = []
        for i in range(0, 9):
            temp_list = []
            for j in range(0, 9):
                temp_list.append(board_check[j][i])
            new_list.append(temp_list)
        return check_line_completion(new_list)

    # divide the original sudoku into each region
    def check_each_region(board_check, i_min, i_max, j_min, j_max):
        temp_list = []
        for i in range(i_min, i_max):
            for j in range(j_min, j_max):
                temp_list.append(board_check[i][j])
        if len(temp_list) == len(set(temp_list)):
            return 1
        else:
            return 0

    # check each region has duplicate value or not
    def check_region_completion(board_check):
        reg1 = check_each_region(board_check, 0, 3, 0, 3)
        reg2 = check_each_region(board_check, 0, 3, 3, 6)
        reg3 = check_each_region(board_check, 0, 3, 6, 9)
        reg4 = check_each_region(board_check, 3, 6, 0, 3)
        reg5 = check_each_region(board_check, 3, 6, 3, 6)
        reg6 = check_each_region(board_check, 3, 6, 6, 9)
        reg7 = check_each_region(board_check, 6, 9, 0, 3)
        reg8 = check_each_region(board_check, 6, 9, 3, 6)
        reg9 = check_each_region(board_check, 6, 9, 6, 9)
        result_reg = reg1 + reg2 + reg3 + reg4 + reg5 + reg6 + reg7 + reg8 + reg9
        if result_reg == 9:
            return False
        else:
            return True

    # check the whole value of sudoku by calling all the above function to check
    def check_sudoku(board_check):
        if check_line_col_format(board_check):
            return 1
        elif check_column_completion(board_check):
            return 2
        elif check_region_completion(board_check):
            return 2
        elif check_line_completion(board_check):
            return 2
        else:
            return 3

    # call the check sudoku function and get the result
    result = check_sudoku(board)
    if result == 1:
        return 'Invalid Format'
    elif result == 2:
        return 'Not Finished'
    elif result == 3:
        return 'Finished'
