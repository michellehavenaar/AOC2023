from Utils.input_tools import *
import re


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


    def puzzle1(instructions, network):
        for el in network:
            data = el.split("=")
            name = data[0].strip()
            adjacents = data[1].split(",")
            left = re.sub("[^a-zA-Z]", "", adjacents[0])
            right = re.sub("[^a-zA-Z]", "", adjacents[1])

            adjacency_matrix[name] = (left,right)

        destination_reached = False

        i = 0
        start = "AAA"
        destination = "ZZZ"
        steps = 0
        while not destination_reached:
            j = i % len(instructions)
            instruction = instructions[j]
            steps = i+1
            # print(f"current instruction is {instruction} and start node is {start}")
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
        







    def puzzle2():
        pass

    result_puzzle1 = puzzle1(instructions, network)
    # result_puzzle2 = puzzle2()

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    # print(f"Puzzle 2 answer: {result_puzzle2}")




if __name__ == "__main__":
    main()