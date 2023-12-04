from Utils.input_tools import *
from collections import Counter 

def double(x, n):
    return x * 2**n

def main():

    input = get_input("04", False)
    scratchcards = get_clean_list_strings(input)


    def puzzle1(scratchcards):
        sum_of_points = 0

        for _,v in enumerate(scratchcards):
            numbers = v.split(":")[1]
            winning_numbers, your_numbers = numbers.split("|")
            winning_numbers_list = winning_numbers.split()   
            your_numbers_list = your_numbers.split() 

            count_numbers = Counter(winning_numbers_list + your_numbers_list)

            wins = 0
            for _,v in count_numbers.items():
                if v >= 2:
                    wins+=1

            if wins != 0:
                points = double(1, wins-1)
                sum_of_points += points
        
        return sum_of_points

    def puzzle2(scratchcards):
        
        instances = {}

        """
        dictionary in which the key is the card number and the value is the amount of instances. 
        initialized for all cards with 1 instance
        {1: 1, 2: 1, 3: 1}
        """

        for i in range(len(scratchcards)):
            instances[i+1] = 1



        for i,v in enumerate(scratchcards):
            card_number = i +1
            instance = instances[card_number]

            numbers = v.split(":")[1]
            winning_numbers, your_numbers = numbers.split("|")
            winning_numbers_list = winning_numbers.split() 
            your_numbers_list = your_numbers.split() 

            count_numbers = Counter(winning_numbers_list + your_numbers_list)

            wins = 0
            for _,v in count_numbers.items():
                if v >= 2:
                    wins+=1

            if wins != 0:
                for i in range(1,wins +1):
                    copy_card_nr = card_number + i
                    copy_amount = instance
                    instance_copy_card = instances[copy_card_nr]
                    new_instance = instance_copy_card + copy_amount
                    instances[copy_card_nr] = new_instance
        
        sum_of_cards=0

        for _, v in instances.items():
            sum_of_cards+= v

        return sum_of_cards







        pass


    result_puzzle1 = puzzle1(scratchcards)
    result_puzzle2 = puzzle2(scratchcards)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")

if __name__ == "__main__":
    main()