from Utils.input_tools import *
import re
import math

"""
adjacency_matrix = {
    "AAA" : ("BBB", "CCC")
}
"""    


def main():

    input = get_input_in_blocks("08", False)
    instructions = input[0][0]
    network = input[1]

    adjacency_matrix = {}

    list_of_starting_nodes = []

    for el in network:
            data = el.split("=")
            name = data[0].strip()
            if name[2] == "A": # get starting nodes for puzzle 2
                list_of_starting_nodes.append(name)
            adjacents = data[1].split(",")
            left = re.sub("[^a-zA-Z0-9]", "", adjacents[0])
            right = re.sub("[^a-zA-Z0-9]", "", adjacents[1])

            adjacency_matrix[name] = (left,right)


    def puzzle1(instructions):
        destination_reached = False

        i = 0
        start = "AAA"
        destination = "ZZZ"
        steps = 0
        while not destination_reached:
            j = i % len(instructions)
            instruction = instructions[j]
            steps = i+1
            # get next node
            adjacent_nodes = adjacency_matrix[start]
            if instruction == "L":
                next_node = adjacent_nodes[0]
                if next_node == destination:
                    destination_reached = True
            elif instruction == "R": 
                next_node = adjacent_nodes[1]
                if next_node == destination:
                    destination_reached = True
            # update start node
            start = next_node
            i+=1
        
        return steps
        

    def puzzle2(instructions, list_of_starting_nodes):

        i = 0
        steps = 0
        starting_nodes = list_of_starting_nodes

        cycles = []
        for node in starting_nodes:
            i = 0
            steps = 0
            start = node
            destination_reached = False
            while not destination_reached:
                j = i % len(instructions)
                instruction = instructions[j]
                steps = i+1
                # get next node
                adjacent_nodes = adjacency_matrix[start]
                if instruction == "L":
                    next_node = adjacent_nodes[0]
                    if next_node[2] == "Z":
                        destination_reached = True
                elif instruction == "R": 
                    next_node = adjacent_nodes[1]
                    if next_node[2] == "Z":
                        destination_reached = True
                # update start node
                start = next_node
                i+=1
            print(f"for starting node {node} the first time Z is reached takes {steps} steps") 
            # and I'm assuming (correctly) that this is the start of a cycle because the internet and the test input told me so
            cycles.append(steps)
        

        # find lcm (lowest common multiple) of the list of steps
        # lcm of first 2 elements, then lcm of lcm and next element etc. until end of the list

        lcm = cycles[0]
        for i in range(1, len(cycles)):
            print(f"find lcm of {lcm} and {cycles[i]}")
            lcm = lcm * cycles[i]//math.gcd(lcm, cycles[i])
            print(lcm)
        
        return lcm



    result_puzzle1 = puzzle1(instructions)
    result_puzzle2 = puzzle2(instructions, list_of_starting_nodes)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")




if __name__ == "__main__":
    main()