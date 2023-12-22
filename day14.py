from Utils.input_tools import *
from Utils.grid_tools import *

def main():

    input = get_input("14", False)
    clean_input = get_clean_list_strings(input)

    grid = make_2d_grid(clean_input)


    def puzzle1(grid):
        list_of_collumns = []

        for col_num in range(len(grid[0])):

            col = get_column_of_grid(grid, col_num)

            all_rocks_in_col = [index for index, val in enumerate(col) if val == "O"]

            block_index = -1 
            for original_pos in all_rocks_in_col:
                # ['O', 'O', '.', 'O', '.', 'O', '.', '.', '#', '#']
                # from each loose rock look and move to the left
                
                for i in (range(original_pos, block_index, -1)):
                    pointer = i-1
                    if pointer == block_index:
                        # block reached, lock the rock in place
                        col[i] = "O"
                        # and empty the spot it left behind (if it moved)
                        if i < original_pos:
                            col[original_pos] = "."
                        block_index = i
                        break
                    elif col[pointer] == ".":
                        continue
                    else:
                        # new obstacle found, lock the rock in place
                        col[i] = "O"
                        # and empty the spot it left behind (if it moved)
                        if i < original_pos:
                            col[original_pos] = "."
                        block_index = i
                        break
            list_of_collumns.append(col)

        new_grid = []
        # make a new grid with the changed collumns
        for i in range(len(list_of_collumns)):
            new_row = [col[i] for col in list_of_collumns]
            new_grid.append(new_row)

        total_load = 0
        for index, row in enumerate(reversed(new_grid)):
            factor = index +1
            rock_count = row.count("O")
            load = rock_count * factor
            total_load += load
        
        return total_load


    def puzzle2():
        pass


    result_puzzle1 = puzzle1(grid)
    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    # result_puzzle2 = puzzle2()
    
    # print(f"Puzzle 2 answer: {result_puzzle2}")



if __name__ == "__main__":
    main()