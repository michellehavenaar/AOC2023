from Utils.input_tools import *

class cubesRevealed:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __str__(self):
        return str((self.red, self.green, self.blue))
    def is_possible(self, rules):
        if self.red <= rules['RED'] and self.green <= rules['GREEN'] and self.blue <= rules['BLUE']:
            return True
        else:
            return False


def parse(reveal):
    colors = ["red", "green", "blue"]
    values = [0,0,0]
    list_of_cubes = reveal.split(",")
    for cube in list_of_cubes:
        for i, v in enumerate(colors):
            if v in cube:
                number = cube.split()[0]
                values[i] += int(number)

    return values

def get_max_red(list_of_cubes_revealed):
    max_red = max([el.red for el in list_of_cubes_revealed])

    return max_red

def get_max_green(list_of_cubes_revealed):
    max_green = max([el.green for el in list_of_cubes_revealed])
    
    return max_green

def get_max_blue(list_of_cubes_revealed):
    max_blue = max([el.blue for el in list_of_cubes_revealed])
    
    return max_blue
    
RULES = {
        "RED": 12,
        "GREEN": 13,
        "BLUE": 14
    }


def main():

    input = get_input("02", False)
    list_of_games = get_clean_list_strings(input)


    def puzzle1(list_of_games):
        sum_of_possible_games = 0

        for i, v in enumerate(list_of_games):
            game_nr = i + 1
            _, reveals = v.split(":")
            list_of_reveals= reveals.split(";")
            cubes_revealed = []
            for reveal in list_of_reveals:
                cube_parsed = parse(reveal)
                cube_revealed = cubesRevealed(cube_parsed[0], cube_parsed[1], cube_parsed[2])
                cubes_revealed.append(cube_revealed)

            if all(c.is_possible(RULES) for c in cubes_revealed):
                sum_of_possible_games += game_nr

        return sum_of_possible_games

    def puzzle2(list_of_games):
        sum_of_powers = 0
        
        for i, v in enumerate(list_of_games):
            game_nr = i + 1
            _, reveals = v.split(":")
            list_of_reveals= reveals.split(";")
            cubes_revealed = []
            for reveal in list_of_reveals:
                cube_parsed = parse(reveal)
                cube_revealed = cubesRevealed(cube_parsed[0], cube_parsed[1], cube_parsed[2])
                cubes_revealed.append(cube_revealed)


            power = get_max_red(cubes_revealed) * get_max_green(cubes_revealed) * get_max_blue(cubes_revealed)
            sum_of_powers += power

        return sum_of_powers









    result_puzzle1 = puzzle1(list_of_games)
    result_puzzle2 = puzzle2(list_of_games)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")



if __name__ == "__main__":
    main()