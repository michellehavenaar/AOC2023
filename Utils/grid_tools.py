def make_2d_grid(input_list):
    # input should be a 1d list of strings
    # each element in the list will be made into a list where each character of the string becomes an element

    grid = [list(el) for el in input_list]
    return grid


def get_column_of_grid(grid, col_number):
    # returns a list of elements that represent a column in a grid
    # grid should be a 2d list like [[1,2,3],[4,5,6],[7,8,9]]
    # column number begins at 0
    # column number 1 returns [2,5,8]

    col = [row[col_number] for row in grid]
    return col

def get_row_of_grid(grid, row_number):
    # returns a list of elements that represent a row in a grid
    # grid should be a 2d list like [[1,2,3],[4,5,6],[7,8,9]]
    # row number begins at 0
    # row number 1 returns [4,5,6]

    row = grid[row_number]
    return row

def get_value_from_grid(grid: list, position: tuple):
    # returns the value found at the intersection of the row and column
    # grid should be a 2d list like [[1,2,3],[4,5,6],[7,8,9]]
    # row number begins at 0
    # column number begins at 0
    # position is a tuple with (col_number, row_number)
    # ( 2, 1 ) returns 6
    col_number, row_number = position
    value = grid[row_number][col_number]
    return value

def get_left_pos(position: tuple, step = 1):
    col_number, row_number = position
    new_position = (col_number - step, row_number)
    return new_position

def get_right_pos(position: tuple, step = 1):
    col_number, row_number = position
    new_position = (col_number + step, row_number)
    return new_position

def get_up_pos(position: tuple, step = 1):
    col_number, row_number = position
    new_position = (col_number, row_number - step)
    return new_position

def get_down_pos(position: tuple, step = 1):
    col_number, row_number = position
    new_position = (col_number, row_number + step)
    return new_position



    


