from Utils.input_tools import *

def find_starting_position(grid):
    for index, row in enumerate(grid):
        starting_pos = row.find("S")
        if starting_pos >= 0:
            return (index, starting_pos)
        
def move_north(position, grid):
    row, col = position
    if row - 1 < 0:
        return None
    else:
        new_row = row -1
        tile = grid[new_row][col]
        incoming_direction = "south"
        return (new_row, col, tile, incoming_direction)
    
def move_south(position, grid):
    row, col = position
    if row + 1 > len(grid)-1:
        return None
    else:
        new_row = row + 1
        tile = grid[new_row][col]
        incoming_direction = "north"
        return (new_row, col, tile, incoming_direction)
    
def move_west(position, grid):
    row, col = position
    if col - 1 < 0:
        return None
    else:
        new_col = col - 1
        tile = grid[row][new_col]
        incoming_direction = "east"
        return (row, new_col, tile, incoming_direction)
    
def move_east(position, grid):
    row, col = position
    if col + 1 > len(grid[row])-1:
        return None
    else:
        new_col = col + 1
        tile = grid[row][new_col]
        incoming_direction = "west"
        return (row, new_col, tile, incoming_direction)

moves = {
    "north" : move_north,
    "south" : move_south,
    "west" : move_west,
    "east" : move_east
}    

tile_map = {
    "|" : {"north" : "south", "south" : "north"},
    "-" : {"east" : "west", "west" : "east"},
    "L" : {"north" : "east", "east": "north"},
    "J" : {"north" : "west", "west" : "north"},
    "7" : {"south" : "west", "west" : "south"},
    "F" : {"south" : "east", "east" : "south"},
    "." : None
}

def find_valid_path(tile, incoming_direction):
    pipe_data = tile_map[tile]
    if pipe_data == None:
        # no pipe in this tile
        return False
    else:
        if incoming_direction in pipe_data:
            return True   
        else:
            # no valid path found
            return False

def find_next_direction(tile, incoming_direction):
    pipe_data = tile_map[tile]
    outgoing_direction = pipe_data[incoming_direction]
    return outgoing_direction

def main():

    input = get_input("10", False)
    tiles = get_clean_list_strings(input)
    starting_pos = find_starting_position(tiles)


    def puzzle1(starting_pos, tiles):
        direction = None

        # look around to see where the loop starts (two possible directions but we only need one)
        # detemine what direction we will start moving in
        try_north = move_north(starting_pos, tiles)
        if try_north:
            row, col, tile, incoming_direction = try_north
            if find_valid_path(tile, incoming_direction): 
                direction = "north"
                print(f"valid path found we will head {direction}")
            else:
                try_south = move_south(starting_pos, tiles)
                if try_south:
                    row, col, tile, incoming_direction = try_south
                    if find_valid_path(tile, incoming_direction):
                        direction = "south"
                        print(f"valid path found we will head {direction}")
                    else: 
                        try_west = move_west(starting_pos, tiles)
                        if try_west:
                            row, col, tile, incoming_direction = try_west
                            if find_valid_path(tile, incoming_direction):
                                direction = "west"
                                print(f"valid path found we will head {direction}")
                            else: 
                                try_east = move_east(starting_pos, tiles)
                                if try_east:
                                    row, col, tile, incoming_direction = try_east
                                    if find_valid_path(tile, incoming_direction):
                                        direction = "east"
                                        print(f"valid path found we will head {direction}")
                                    else: 
                                        print(f"{tile} is not a valid path")
        
        
        # start moving through the pipes                               
        print(f"heading {direction}")

        back_at_start = False
        steps = 0

        while not back_at_start:
            # move in the determined direction
            steps +=1
            next_tile = moves[direction](starting_pos, tiles)
            row, col, tile, incoming_direction = next_tile
            # check if the tile is the starting position
            if tile == "S":
                back_at_start = True 
            else:
                # find the outgoing direction of the pipe
                next_direction = find_next_direction(tile, incoming_direction)
                starting_pos = (row, col)
                direction = next_direction

        print(f"total steps is {steps}")
        midpoint = steps // 2
        print(f"midpoint is {midpoint}")
        return midpoint


    def puzzle2():
        pass

    
    result_puzzle1 = puzzle1(starting_pos, tiles)
    # result_puzzle2 = puzzle2()

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    # print(f"Puzzle 2 answer: {result_puzzle2}")



if __name__ == "__main__":
    main()