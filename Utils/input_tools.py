def get_input(day_number: str, test: bool):
    # reads lines from the input file and outputs as a list 
    # provide the number of the day as a string and set test to True to run the test input

    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = file.readlines()
        return raw_data
    
def get_input_in_blocks(day_number: str, test: bool):
    # gets raw data from the input file and outputs as a list with each block as a list of elements
    # provide the number of the day as a string and set test to True to run the test input

    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = file.read()
        raw_content_blocks = raw_data.split("\n\n")
        content_blocks = [el.split("\n") for el in raw_content_blocks]

        return content_blocks
    

def get_clean_list_strings(list):
    string_list = [el.replace("\n", "") for el in list]
    return string_list

def get_clean_list_ints(list):
    int_list = [int(el) for el in list]
    return int_list

def split_list_in_chunks(list, chunksize: int):
    # list split into chunks of size (chunksize)
    chunked_list = [list[i: i + chunksize] for i in range(0, len(list), chunksize)]
    return chunked_list