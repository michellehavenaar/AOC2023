from Utils.input_tools import *

def calculate_difference(sequence):
    new_sequence = []
    for i in range(len(sequence)-1):
        difference = sequence[i +1] - sequence[i]
        new_sequence.append(difference)
    return new_sequence

def predict_next_value(list_of_last_values):
    next_value = 0
    for el in list_of_last_values:
        new_add = el + next_value
        next_value = new_add
    return next_value

def predict_previous_value(list_of_first_values):
    previous_value = 0
    for el in list_of_first_values:
        new_subtract = el - previous_value
        previous_value = new_subtract
    return previous_value



def main():

    input = get_input("09", False)
    clean_input = get_clean_list_strings(input)
    histories =[]
    for el in clean_input:
        history = el.split(" ")
        histories.append(get_clean_list_ints(history))
        


    def puzzle1(histories):
        sum_of_next_values = 0
        for history in histories:
            last_values = []
            last_values.append(history[-1])
            zero_difference = False

            while zero_difference == False:
                differences = calculate_difference(history)
                last_values.insert(0, differences[-1])
                if all(d == 0 for d in differences):
                    zero_difference = True
                else:
                    history = differences

            next_value = predict_next_value(last_values)
            sum_of_next_values += next_value
        return sum_of_next_values

        

    def puzzle2(histories):
        sum_of_previous_values = 0
        for history in histories:
            first_values = []
            first_values.append(history[0])
            zero_difference = False

            while zero_difference == False:
                differences = calculate_difference(history)
                first_values.insert(0, differences[0])
                if all(d == 0 for d in differences):
                    zero_difference = True
                else:
                    history = differences

            previous_value = predict_previous_value(first_values)
            sum_of_previous_values += previous_value
        return sum_of_previous_values

    result_puzzle1 = puzzle1(histories)
    result_puzzle2 = puzzle2(histories)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")




if __name__ == "__main__":
    main()