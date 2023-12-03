from Utils.input_tools import *
from Utils.grid_tools import *
import re
import math



def check_part(grid, row, indexes):
    # take all the positions of the possible engine part number
    for i in indexes:
        pos = (i, row)
        # look around and get all the positions around the current position
        neighbours = look_around(pos)
        for n in neighbours:
            if in_range(grid, n):
                neighbour_value = get_value_from_grid(grid,n)
                # get the value of the neighbour in the grid
                if not re.match("\d|[.]", neighbour_value):
                    # check if the neighbour is a symbol (not a digit or a dot)
                    return True
    return False

def get_gear_neighbours(grid, row, col):
    # take the possible gear location
    pos = (col, row)
    # look around and get all the positions around the current position
    neighbours = look_around(pos)
    number_neighbours_positions = []
    for n in neighbours:
        if in_range(grid, n):
            neighbour_value = get_value_from_grid(grid,n)
            # get the value of the neighbour in the grid
            if re.match("\d", neighbour_value):
                # check if the neighbour is a digit
                number_neighbours_positions.append(n)
                    # add the position to a list
    return number_neighbours_positions




def main():

    input = get_input("03", False)
    schematic = get_clean_list_strings(input)
    grid = make_2d_grid(schematic)


    def puzzle1(schematic, grid):
        possible_engine_parts = []
        for s in schematic:
            parts = {m.start(): (m.group(0)) for m in re.finditer('\d+', s)} # {0: '467', 5: '114'}
            possible_engine_parts.append(parts)

        sum_of_part_numbers = 0

        for line_number, line in enumerate(possible_engine_parts):
            for k,v in line.items():
                indexes = [index for index in range(k, k + len(v))] # fill out a list of indexes for every digit of the possible engine part
                if check_part(grid, line_number, indexes):
                    part_number = int(v)
                    sum_of_part_numbers += part_number

        return sum_of_part_numbers

    def puzzle2(schematic, grid):
        list_of_part_numbers = []
        for s in schematic:
            row = []
            parts = {m.start(): (m.group(0)) for m in re.finditer('\d+', s)}
            for k,v in parts.items():
                indexes = [index for index in range(k, k + len(v))] # fill out a list of indexes for every digit of the possible engine part
                extended_part = {v: indexes} # make an extended dict with all the indexes of the part in stead of just the starting index
                row.append(extended_part)
            list_of_part_numbers.append(row)

        possible_gears = []
        for s in schematic:
            gears = {m.start(): (m.group(0)) for m in re.finditer('[*]', s)}
            possible_gears.append(gears)

        sum_of_gear_ratios = 0

        for line_number, line in enumerate(possible_gears):
            for k,v in line.items():
                col = k
                gear_neighbours = get_gear_neighbours(grid, line_number, col)
                part_numbers = []
                for pos in gear_neighbours:
                    col, row = pos
                    # look through all the neighbours that are numbers
                    parts = list_of_part_numbers[row]
                    # compare them to the list of part numbers to find the numbers at that position, a number can be found multiple times
                    for part in parts:
                        for k,v in part.items():
                            if col in v:
                                part_numbers.append(int(k))
                set_part_numbers = list(set(part_numbers))
                # remove duplicates
                if len(set_part_numbers) == 2:
                    gear_ratio = math.prod(set_part_numbers) # multiply the numbers
                    sum_of_gear_ratios += gear_ratio
        
        return sum_of_gear_ratios
            


    result_puzzle1 = puzzle1(schematic, grid)
    result_puzzle2 = puzzle2(schematic, grid)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")




if __name__ == "__main__":
    main()