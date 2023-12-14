from Utils.input_tools import *
from collections import Counter
from operator import itemgetter


    
translate_cards = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10
}

translate_cards_2 = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 1,
    "T" : 10
}



def determine_type(hand):
    hand_counter = Counter(hand)
    if any (count == 5 for count in hand_counter.values()):
        # print("Five of a kind")
        return 6
    if any (count == 4 for count in hand_counter.values()):
        # print("Four of a kind")
        return 5
    if any (count == 3 for count in hand_counter.values()) and any (count == 2 for count in hand_counter.values()):
        # print("Full house")
        return 4
    if any (count == 3 for count in hand_counter.values()) and any (count == 1 for count in hand_counter.values()):
        # print("Three of a kind")
        return 3
    if any (count == 2 for count in hand_counter.values()):
        pairs = [count for count in hand_counter.values() if count == 2]
        if len(pairs) == 2:
            # print("Two pairs")
            return 2
        elif len(pairs) == 1:
            # print("One Pair")
            return 1
    if all (count == 1 for count in hand_counter.values()):
        # print("High card")
        return 0
    
def determine_type_2(hand):
    hand_counter = Counter(hand)
    if any (count == 5 for count in hand_counter.values()):
        # print("Five of a kind, allready strongest")
        return 6
    if any (count == 4 for count in hand_counter.values()):
        # print("Four of a kind")
        if hand_counter[1] == 1: # there is one J that can be swapped to make a five of a kind
            return 6
        elif hand_counter[1] == 4: # there is four J that can be swapped to make a five of a kind
            return 6
        else: # there is no J that can be swapped to make a five of a kind, remains four of a kind
            return 5
    if any (count == 3 for count in hand_counter.values()) and any (count == 2 for count in hand_counter.values()):
        # print("Full house")
        if hand_counter[1] == 2: # there are two J's that can be swapped to make a five of a kind
            return 6
        elif hand_counter[1] == 3: # there are three J's that can be swapped to make a five of a kind
            return 6
        else: # there is no J that can be swapped, remains full house
            return 4
    if any (count == 3 for count in hand_counter.values()) and any (count == 1 for count in hand_counter.values()):
        # print("Three of a kind")
        if hand_counter[1] == 1: # there is one J that can be swapped to make a four of a kind
            return 5
        elif hand_counter[1] == 3: # there is three J that can be swapped to make a four of a kind
            return 5
        else: # there is no J that can be swapped, remains three of a kind
            return 3
    if any (count == 2 for count in hand_counter.values()):
        pairs = [count for count in hand_counter.values() if count == 2]
        if len(pairs) == 2:
            # print("Two pairs")
            if hand_counter[1] == 1: # there is one J that can be swapped to make a full house
                return 4
            elif hand_counter[1] == 2: # there is two J that can be swapped to make a four of a kind
                return 5
            else:
                return 2
        elif len(pairs) == 1:
            # print("One Pair")
            if hand_counter[1] == 1: # there is one J that can be swapped to make a three of a kind
                return 3
            elif hand_counter[1] == 2: # there is two J that can be swapped to make a three of a kind
                return 3
            else:
                return 1
    if all (count == 1 for count in hand_counter.values()):
        # print("High card")
        if hand_counter[1] == 1: # there is one J that can be swapped to make a pair
            return 1
        else:
            return 0
    

def sort_hands(hands):
    if len(hands) <= 1:
        # none or one hand in the list so it does not need to be sorted
        sorted_hands = hands
    else:
        sorted_hands = sorted(hands, key=itemgetter(0,1,2,3,4))
    return sorted_hands


  

def main():

    input = get_input("07", False)
    unsorted_list_of_hands = get_clean_list_strings(input)
    

    def puzzle1(unsorted_list_of_hands):
        list_of_types = [[],[],[],[],[],[],[]]
        for el in unsorted_list_of_hands:
            hand_str, bid = el.split()
            hand = [h_s for h_s in hand_str]
            new_hand = []
            for h in hand:
                if h in translate_cards:
                    h = translate_cards[h] # translate the letter into a number so it can be more easily compared later
                new_hand.append(int(h))
            new_hand.append(int(bid)) # add the bid amount to the end of the hand so it can be used later
            type = determine_type(new_hand[:-1]) # omit the last element because that is the bid amount
            list_of_types[type].append(new_hand)
        sorted_list_of_hands = []
        for l in list_of_types:
            sorted_list = sort_hands(l)
            sorted_list_of_hands += sorted_list

        total_winnings = 0
        for i, v in enumerate(sorted_list_of_hands):
            rank = i+1
            bid = v[-1]
            winnings = bid * rank
            total_winnings += winnings
        return total_winnings

    def puzzle2(unsorted_list_of_hands):
        list_of_types = [[],[],[],[],[],[],[]]
        for el in unsorted_list_of_hands:
            hand_str, bid = el.split()
            hand = [h_s for h_s in hand_str]
            new_hand = []
            for h in hand:
                if h in translate_cards_2:
                    h = translate_cards_2[h] # translate the letter into a number so it can be more easily compared later
                new_hand.append(int(h))
            new_hand.append(int(bid)) # add the bid amount to the end of the hand so it can be used later
            type = determine_type_2(new_hand[:-1]) # omit the last element because that is the bid amount
            list_of_types[type].append(new_hand)
        sorted_list_of_hands = []
        for l in list_of_types:
            sorted_list = sort_hands(l)
            sorted_list_of_hands += sorted_list

        total_winnings = 0
        for i, v in enumerate(sorted_list_of_hands):
            rank = i+1
            bid = v[-1]
            winnings = bid * rank
            total_winnings += winnings
        return total_winnings

    

    result_puzzle1 = puzzle1(unsorted_list_of_hands)
    result_puzzle2 = puzzle2(unsorted_list_of_hands)

    print(f"Puzzle 1 answer: {result_puzzle1}")
    
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()