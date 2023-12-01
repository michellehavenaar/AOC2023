from Utils.input_tools import *
import re

def main():

    input = get_input("01", False)
    

    calibration_document = get_clean_list_strings(input)
    # print(calibration_document)

    LETTERS = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
     

    def puzzle1(calibration_document):
        only_digits = [re.sub('\D', '', calibration) for calibration in calibration_document]
   
        clean_calibration = [cc[0]+cc[-1] for cc in only_digits]
    

        calibrations = get_clean_list_ints(clean_calibration)
        return sum(calibrations)
        

    def puzzle2(calibration_document):

        new_calibration_document = []

        for calibration in calibration_document:
            new_calibration = []
            for i, v in enumerate(calibration):
                if v.isdigit():
                    # print(f"character is {v} at index {i}")
                    new_calibration.append((i, v ))
            for k,v in LETTERS.items():
                for i, _ in enumerate(calibration):
                    if calibration.startswith(k, i):
                        # print(f"found word {k} at index {i}, should replace with {v}")
                        new_calibration.append((i, v))
            new_calibration_document.append(new_calibration)


        final_calibration_document = []
        for el in new_calibration_document:
            sorted_el = sorted(el)
            first_and_last_el = [sorted_el[0],sorted_el[-1]]
            final_cal = [(el[1]) for el in first_and_last_el]
            calibration_value = "".join(final_cal)
            final_calibration_document.append(calibration_value)

        calibrations = get_clean_list_ints(final_calibration_document)

        return sum(calibrations)



    result_puzzle1 = puzzle1(calibration_document)
    result_puzzle2 = puzzle2(calibration_document)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")




if __name__ == "__main__":
    main()