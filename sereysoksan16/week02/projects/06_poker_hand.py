# this function is used to test the real poker game that will take 2 parameter as input
def poker_hand(player1, player2):
    from collections import defaultdict

    # dummy dictionary is used to rank the card by value
    card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
                 'A': 14}
    player1_list = player1.split()
    player2_list = player2.split()

    # this function is used to check for the royal card (5 highest card)
    def check_royal(hand):
        values = [i[0] for i in hand]
        if set(values) == {'A', 'T', 'K', 'Q', 'J'}:
            return True
        else:
            return False

    # this function is used to check the flush card (all the same suit)
    def check_flush(hand):
        suits = [i[1] for i in hand]
        if len(set(suits)) == 1:
            return True
        else:
            return False

    # this function is used to check the card is royal flush (highest rank) or not by taking royal and flush function
    # compare together
    def check_royal_flush(hand):
        if check_royal(hand) and check_flush(hand):
            return True
        else:
            return False

    # check the straight card (5 card in one sequence)
    def check_straight(hand):
        values = [i[0] for i in hand]
        # default dictionary that have value equal to lambda for all item in the beginning
        values_count = defaultdict(lambda: 0)
        # write the value into default dict
        for v in values:
            values_count[v] += 1
        # write the card in rank of number (from dummy dict) into a list
        rank_values = [card_rank[i] for i in values]
        # find the number between the lowest rank and the highest rank
        values_range = max(rank_values) - min(rank_values)
        if len(set(values_count.values())) == 1 and values_range == 4:
            return True
        else:
            # this is the smallest straight (special case)
            if set(values) == set(['A', '2', '3', '4', '5']):
                return True
            return False

    # check the straight flush card (5 card in one sequence and same suit)
    def check_straight_flush(hand):
        if check_flush(hand) and check_straight(hand):
            return True
        else:
            return False

    # check the 5 cards that have 4 of them are the same
    def check_four_of_a_kind(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 4]:
            return True
        else:
            return False

    # check the 5 cards that have 3 of them are the same and 2 others is random
    def check_three_of_a_kind(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if set(values_count.values()) == set([3, 1]):
            return True
        else:
            return False

    # check the 5 cards that have 3 of a kind and a pair (2 cards are same)
    def check_full_house(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [2, 3]:
            return True
        else:
            return False

    # check the 5 cards 2 pair and 1 other value
    def check_two_pair(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 2, 2]:
            return True
        else:
            return False

    # check the 5 cards have 2 cards are the same and 3 other cards are random value
    def check_one_pair(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 1, 1, 2]:
            return True
        else:
            return False

    # check each rank card and return the rank value
    def check_hand(hand):
        if check_royal_flush(hand):
            return 10
        elif check_straight_flush(hand):
            return 9
        elif check_four_of_a_kind(hand):
            return 8
        elif check_full_house(hand):
            return 7
        elif check_flush(hand):
            return 6
        elif check_straight(hand):
            return 5
        elif check_three_of_a_kind(hand):
            return 4
        elif check_two_pair(hand):
            return 3
        elif check_one_pair(hand):
            return 2
        else:
            return 1

    # check the rank and value between player 1 and 2 to find the winner
    player1_value = check_hand(player1_list)
    player2_value = check_hand(player2_list)
    # check which one who one
    if player1_value > player2_value:
        return 'Player 1 WIN'
    elif player2_value > player1_value:
        return 'Player 2 WIN'
    else:
        return 'Tie'


# player1_card = '2S 3H 4H 5S 6C'
# player2_card = 'AH AC 5H 6H AS'
# print(poker_hand(player1_card, player2_card))
