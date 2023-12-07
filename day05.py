from Utils.input_tools import *

class inputRange:
    def __init__(self, start, length):
        self.start = start
        self.end = start + length-1
        self.length = length
        self.output_found = False
        self.output_start = None
        self.output_length = None
    def __str__(self):
        return str((self.start, self.end, self.length, self.output_found, self.output_start, self.output_length))
    def update_output(self, output_start, output_length):
        self.output_found = True
        self.output_start = output_start
        self.output_length = output_length
    def reset(self):
        if self.output_found:
            self.start = self.output_start
            self.end = self.start + self.output_length-1
            self.length = self.output_length
            self.output_found = False
            self.output_start = None
            self.output_length = None
    

def parse_map(map):
    ranges = []
    for line in map[1:]:
        range = get_clean_list_ints(line.split())
        ranges.append(range)
    return ranges

def find_destination(ranges, source_number):
    for range in ranges:
        destination_start, source_start, range_length = range 
        source_end = source_start + (range_length-1)
        # print(f"looking for number {source_number}: source range starts at {source_start} and ends at {source_end}")
        if source_number >= source_start and source_number <= source_end:
            difference = source_number - source_start
            destination_number = destination_start + difference
            return destination_number
    
    # source_number not in any of the ranges
    destination_number = source_number
    return destination_number

def parse_seed_ranges(seed_numbers):
    seed_start = seed_numbers[::2]
    seed_range = seed_numbers[1::2]
    zipped = zip(seed_start, seed_range)
    seed_ranges = list(zipped)
    return seed_ranges


def process_input_for_map(map, input_range):
    inputs = []
    outputs = []
    # add the initial input range to the input list
    inputs.append(input_range)

    while inputs:
        input = inputs.pop(0)
        input_start, input_end, input_length = input.start, input.end, input.length

        for line in map:
            # print(f"processing {input} against {line}")
            destination_start, source_start, range_length = line
            source_end = source_start + (range_length-1)
            destination_end = destination_start + (range_length-1)
            # print(f"input starts at {input_start} and ends at {input_end}, map-line starts at {source_start} and ends at {source_end}")
            # check if entire input range is found in line
            if input_start >= source_start and input_end <= source_end:
                # print(f"entire range {input_start} to {input_end} falls in this line")
                # calculate output
                difference = input_start - source_start
                output_start = destination_start + difference
                output_length = input_length
                input.update_output(output_start, output_length)
                break
            # check if part of input range is found in line, start is in, end is out 
            elif input_start >= source_start and input_start <= source_end:
                # print(f"start of range {input_start} to {source_end} falls in this line")
                # calculate output
                difference = input_start - source_start
                output_start = destination_start + difference
                output_length = (destination_end - output_start) +1
                input.update_output(output_start, output_length)

                # calculate new input for out of range part
                # print(f" out of range from {source_end + 1} to { input_end}")
                out_of_range_start = source_end +1
                out_of_range_length = (input_end -  out_of_range_start) + 1
                # create new input and add it to the input list
                new_input = inputRange(out_of_range_start,out_of_range_length)
                inputs.append(new_input)
                break
            # check if part of input range is found in line, start is out, end is in 
            elif input_end >= source_start and input_end <= source_end:
                # print(f"end of the range {source_start} to {input_end} falls in this line")
                # calculate output
                difference = input_end - source_start
                output_start = destination_start
                output_length = difference +1
                input.update_output(output_start, output_length)

                # calculate new input for out of range part
                # print(f" out of range from {input_start} to {source_start -1}")
                out_of_range_start = input_start
                out_of_range_length = ((source_start -1) - out_of_range_start) + 1
                # create new input and add it to the input list
                new_input = inputRange(out_of_range_start,out_of_range_length)
                inputs.append(new_input)
                break
            # input range is not found in this line
            else:
                pass

        # when finished looping through map add the current input to the output list
        outputs.append(input)

    return outputs

def process_outputs(outputs):
    new_input_list = []
    for output in outputs:
        # update output so it can be new input
        output.reset()
        new_input_list.append(output)
    return new_input_list
        


def main():

    input = get_input_in_blocks("05", False)
    
    seeds = input[0][0].split(":")
    seed_numbers = get_clean_list_ints(seeds[1].split())

    seed_ranges = parse_seed_ranges(seed_numbers)
    

    seed_to_soil_map = parse_map(input[1])
    soil_to_fertilizer_map = parse_map(input[2])
    fertilizer_to_water_map = parse_map(input[3])
    water_to_light_map = parse_map(input[4])
    light_to_temperature_map = parse_map(input[5])
    temperature_to_humidity_map = parse_map(input[6])
    humidity_to_location_map = parse_map(input[7])


    def puzzle1(seed_numbers):
        lowest_location_number = 0
        for seed in seed_numbers:
            soil_number = find_destination(seed_to_soil_map, seed)
            fertilizer_number = find_destination(soil_to_fertilizer_map, soil_number)
            water_number = find_destination(fertilizer_to_water_map, fertilizer_number)
            light_number = find_destination(water_to_light_map, water_number)
            temperature_number = find_destination(light_to_temperature_map, light_number)
            humidity_number = find_destination(temperature_to_humidity_map, temperature_number)
            location_number = find_destination(humidity_to_location_map, humidity_number)
            if lowest_location_number == 0:
                lowest_location_number = location_number
            elif lowest_location_number > location_number:
                lowest_location_number = location_number

        return lowest_location_number


    def puzzle2(seed_ranges):
        list_of_seed_ranges = [inputRange(sr[0], sr[1]) for sr in seed_ranges]
        list_of_soil_ranges = []
        list_of_fertilizer_ranges = []
        list_of_water_ranges = []
        list_of_light_ranges = []
        list_of_temperature_ranges = []
        list_of_humidity_ranges = []
        list_of_location_ranges = []

        for el in list_of_seed_ranges:
            outputs = process_input_for_map(seed_to_soil_map, el)
            list_of_soil_ranges += process_outputs(outputs)

        # print("starting on soil ranges..")
        for el in list_of_soil_ranges:
            outputs = process_input_for_map(soil_to_fertilizer_map, el)
            list_of_fertilizer_ranges += process_outputs(outputs)

        # print("starting on fertilizer ranges..")
        for el in list_of_fertilizer_ranges:
            outputs = process_input_for_map(fertilizer_to_water_map, el)
            list_of_water_ranges += process_outputs(outputs)

        # print("starting on water ranges..")
        for el in list_of_water_ranges:
            outputs = process_input_for_map(water_to_light_map, el)
            list_of_light_ranges += process_outputs(outputs)

        # print("starting on light ranges..")
        for el in list_of_light_ranges:
            outputs = process_input_for_map(light_to_temperature_map, el)
            list_of_temperature_ranges += process_outputs(outputs)

        # print("starting on temperature ranges..")
        for el in list_of_temperature_ranges:
            outputs = process_input_for_map(temperature_to_humidity_map, el)
            list_of_humidity_ranges += process_outputs(outputs)

        # print("starting on humidity ranges..")
        for el in list_of_humidity_ranges:
            outputs = process_input_for_map(humidity_to_location_map, el)
            list_of_location_ranges += process_outputs(outputs)

        # print("==Location Ranges!!==")
        lowest_location_number = 0
        for el in list_of_location_ranges:
            if lowest_location_number == 0:
                lowest_location_number = el.start
            elif lowest_location_number > el.start:
                lowest_location_number = el.start
        return lowest_location_number



      
    result_puzzle1 = puzzle1(seed_numbers)
    result_puzzle2 = puzzle2(seed_ranges)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()