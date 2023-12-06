from Utils.input_tools import *

def parse_map(map):
    ranges = []
    for line in map[1:]:
        range = get_clean_list_ints(line.split())
        ranges.append(range)
    return ranges

def find_destination(ranges, source_number):
    for range in ranges:
        # print(range)
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



def main():

    input = get_input_in_blocks("05", True)
    
    seeds = input[0][0].split(":")
    seed_numbers = get_clean_list_ints(seeds[1].split())


    """
    test_seeds = parse_seed_ranges([79, 14, 55, 13, 82, 3, 90, 5])
    sorted_seeds = sorted(test_seeds)
    print(sorted_seeds)
    for i, v in enumerate(sorted_seeds):
        if i == 0:
            continue
        current_start, current_end = v[0], v[0] + v[1]-1
        previous_start, previous_end = sorted_seeds[i-1][0], sorted_seeds[i-1][0] + sorted_seeds[i-1][1] -1
        print(f"current start {current_start} and end {current_end}, previous: {sorted_seeds[i-1]} with start {previous_start} and end {previous_end}")


    """


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
        lowest_location_number = 0
        for sr in seed_ranges:
            for i in range(sr[1]):
                seed_num = sr[0] + i

                soil_number = find_destination(seed_to_soil_map, seed_num)
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

    
    result_puzzle1 = puzzle1(seed_numbers)
    result_puzzle2 = puzzle2(seed_ranges)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()