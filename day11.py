from Utils.input_tools import *
from Utils.grid_tools import *

def calculate_distance(pos_a, pos_b):
    row_a, col_a = pos_a
    row_b, col_b = pos_b

    vertical_distance = abs(row_a - row_b)
    horizontal_distance = abs(col_a - col_b)
    distance = vertical_distance + horizontal_distance
    return distance



def calculate_expanded_location(pos, total_rows_to_expand, total_columns_to_expand):
    row, col = pos
    factor = 999999
    expand_rows = [r for r in total_rows_to_expand if r < row]
    expanded_row = row + (len(expand_rows) * factor)
    expand_cols = [c for c in total_columns_to_expand if c < col]
    expanded_col = col + (len(expand_cols) * factor)
    return (expanded_row, expanded_col)

def main():

    input = get_input("11", False)
    image = get_clean_list_strings(input)


    unexpanded_universe = make_2d_grid(image)

    rows_to_expand = [index for index, row in enumerate(unexpanded_universe) if "#" not in row]
    
    columns_to_expand = []
    for i in range(len(unexpanded_universe[0])):
        col = get_column_of_grid(unexpanded_universe, i)
        if "#" not in col:
            columns_to_expand.append(i)

    row_offset = 0
    for row in rows_to_expand:
        index = row +1
        new_row = ["."]*len(unexpanded_universe[0])
        unexpanded_universe.insert(index + row_offset, new_row)
        row_offset += 1


    col_offset = 0
    for col in columns_to_expand:
        index = col +1
        for row in unexpanded_universe:
            row.insert(index + col_offset, ".")
        col_offset += 1

    expanded_universe = unexpanded_universe



    def puzzle1(expanded_universe):

        galaxies = {}

        galaxy_nr = 1
        for index_row, row in enumerate(expanded_universe):
            for index_col, col in enumerate(row):
                if col == "#":
                    galaxies[galaxy_nr] = (index_row, index_col)
                    galaxy_nr += 1



        sum_of_shortest_paths = 0
        for i in range(1, len(galaxies) +1):
            for j in range(i + 1, len(galaxies) +1):
                distance = calculate_distance(galaxies[i], galaxies[j])
                sum_of_shortest_paths += distance
        return sum_of_shortest_paths
    

    def puzzle2(image):

        universe = make_2d_grid(image)

        galaxies = {}

        galaxy_nr = 1
        for index_row, row in enumerate(universe):
            for index_col, col in enumerate(row):
                if col == "#":
                    galaxies[galaxy_nr] = (index_row, index_col)
                    galaxy_nr += 1


        sum_of_shortest_paths = 0
        for i in range(1, len(galaxies) +1):
            for j in range(i + 1, len(galaxies) +1):
                expanded_galaxy_a = calculate_expanded_location(galaxies[i], rows_to_expand, columns_to_expand)
                expanded_galaxy_b = calculate_expanded_location(galaxies[j], rows_to_expand, columns_to_expand)
                distance = calculate_distance(expanded_galaxy_a, expanded_galaxy_b)
                sum_of_shortest_paths += distance
        return sum_of_shortest_paths
        


    result_puzzle1 = puzzle1(expanded_universe)
    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    result_puzzle2 = puzzle2(image)
    
    print(f"Puzzle 2 answer: {result_puzzle2}")



if __name__ == "__main__":
    main()