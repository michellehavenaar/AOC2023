from Utils.input_tools import *
import math

def calculate_options(time, distance):
    count = 0
    
    #check if the mid point is one or two points
    is_two_point_mid = False
    if time % 2 == 1:
        is_two_point_mid = True

    if is_two_point_mid:
        middle_time = time //2
        middle_time_1 = middle_time
        middle_time_2 = middle_time +1
        middle_distance = middle_time_1 * middle_time_2
        print(f"mid point time is {middle_time_1} and {middle_time_2} mid point distance {middle_distance}")

        for i in range(middle_time_1 + 1):
            distance_at_time = (time - i) * i
            if distance_at_time > distance:
                count +=1

        # print(f"x for record distance are {middle_time_1 - count} and {middle_time_2 + count}")
        
        mirrored_count = count*2
        

    else:
        middle_time = time //2
        middle_distance = middle_time **2
        print(f"mid point time is {middle_time} and mid point distance {middle_distance}")
        
        for i in range(middle_time + 1):
            distance_at_time = (time - i) * i
            if distance_at_time > distance:
                count +=1
        
        # print(f"x for record distance are {middle_time- count} and {middle_time + count}")

        mirrored_count = (count *2) -1 # because it only has one midpoint
        
    return mirrored_count

def main():

    input = get_input("06", False)
    clean_input = get_clean_list_strings(input)
    time_input, distance_input = clean_input
    times_str = time_input.split(":")[1].split()
    
    times = get_clean_list_ints(times_str)
    distances_str = distance_input.split(":")[1].split()
    distances = get_clean_list_ints(distances_str)
    
    time_and_distances = list(zip(times, distances))
    
    times_2 = int(time_input.split(":")[1].replace(" ", ""))
    distances_2 = int(distance_input.split(":")[1].replace(" ", ""))
    time_and_distances_2 = (times_2,distances_2)
    


    def puzzle1(time_and_distances):
        list_of_total_options = []
        for el in time_and_distances:
            time, distance = el
            list_of_total_options.append(calculate_options(time, distance))
        
        return math.prod(list_of_total_options)


            

    def puzzle2(time_and_distances_2):
        time, distance = time_and_distances_2
        return calculate_options(time, distance)

    

    result_puzzle1 = puzzle1(time_and_distances)
    result_puzzle2 = puzzle2(time_and_distances_2)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()