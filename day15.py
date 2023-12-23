from Utils.input_tools import *

def hash(string_input):
    current_value = 0
    for c in string_input:
        ascii_code = ord(c)
        current_value += ascii_code
        multiplied = current_value * 17
        current_value = multiplied
        remainder = current_value % 256
        current_value = remainder
    return current_value

def find_lens_by_label(list_of_lenses, label):
    # [(xx, 1), (yy, 2)]
    list_of_indexes = [i for i,v in enumerate(list_of_lenses) if v[0] == label]
    return list_of_indexes

    


def main():

    input = get_input("15", False)
    strings = input[0].split(",")

    boxes = {}



    def puzzle1(strings):
        sum_of_results = 0
        for string in strings:
            result = hash(string)
            sum_of_results += result
        return sum_of_results

    def puzzle2(strings):
        for string in strings:
            # check if the string has a "=" or a "-"
            if string.find("-") >= 0:
                label, focal_length = string.split("-")
                lens_data = (label, focal_length)
                box_nr = hash(label)
                if box_nr in boxes:
                    box = boxes[box_nr]
                    # look through the lenses
                    indexes = find_lens_by_label(box, label)
                    if indexes:
                        # remove the lenses
                        for index in indexes:
                            box.pop(index)

            if string.find("=") >= 0:
                label, focal_length = string.split("=")
                lens_data = (label, focal_length)
                box_nr = hash(label)
                if box_nr in boxes:
                    box = boxes[box_nr]
                    # look through the lenses
                    indexes = find_lens_by_label(box, label)
                    if indexes:
                        # replace the lenses
                        for index in indexes:
                            box[index] = lens_data
                    else:
                        # add the lens
                        box.append(lens_data)
                else:
                    # no box exist yet, create it
                    boxes[box_nr] = [lens_data]

        total_focusing_power = 0
        for box_number, lenses in boxes.items():
            for i, lens in enumerate(lenses):
                slot = i + 1
                focal_length = int(lens[1])
                focusing_power = (box_number + 1) * slot * focal_length
                total_focusing_power += focusing_power
        
        return total_focusing_power


    
    result_puzzle1 = puzzle1(strings)
    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    result_puzzle2 = puzzle2(strings)
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()