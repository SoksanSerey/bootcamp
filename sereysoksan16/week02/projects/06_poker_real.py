# this function is used to test the real poker game that will take 2 parameter as input
def poker_real(player1, player2):
    from collections import defaultdict
    import operator

    # dummy dictionary is used to rank the card by value
    card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
                 'A': 14}
    player1 = player1.upper()
    player2 = player2.upper()
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
            return True, values_count
        else:
            # this is the smallest straight (special case)
            if set(values) == set(['A', '2', '3', '4', '5']):
                values_count = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
                return True, values_count
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
            return True, values_count
        else:
            return False

    # check the 5 cards that have 3 of them are the same and 2 others is random
    def check_three_of_a_kind(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if set(values_count.values()) == set([3, 1]):
            return True, values_count
        else:
            return False

    # check the 5 cards that have 3 of a kind and a pair (2 cards are same)
    def check_full_house(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [2, 3]:
            return True, values_count
        else:
            return False

    # check the 5 cards 2 pair and 1 other value
    def check_two_pair(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 2, 2]:
            return True, values_count
        else:
            return False

    # check the 5 cards have 2 cards are the same and 3 other cards are random value
    def check_one_pair(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 1, 1, 2]:
            return True, values_count
        else:
            return False

    # all the 5 cards are difference
    def check_high_card(hand):
        values = [i[0] for i in hand]
        values_count = defaultdict(lambda: 0)
        for v in values:
            values_count[v] += 1
        if sorted(values_count.values()) == [1, 1, 1, 1, 1]:
            return True, values_count
        else:
            return False

    # this function is used to sorted the dictionary from each above functions to compare for the greater rank
    def list_number_rank(hand):
        sorted_list_rank = []
        for k, v in sorted(hand.items(), key=lambda item: item[1], reverse=True):
            sorted_list_rank.append(k)
        return [card_rank[i] for i in sorted_list_rank]

    # sorted the dictionary by value if the value equal sort by key
    def check_pair_rank(hand):
        sorted_list_rank = []
        sorted_pair = sorted(sorted(hand.items(), reverse=True), key=operator.itemgetter(1), reverse=True)
        for k, v in sorted_pair:
            sorted_list_rank.append(k)
        return [card_rank[i] for i in sorted_list_rank]

    # check when all the card value is difference
    def check_flush_rank(hand):
        values = [i[0] for i in hand]
        rank_card = [card_rank[i] for i in values]
        return sorted(rank_card, reverse=True)

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
        elif check_high_card(hand):
            return 1

    # check the rank and value between player 1 and 2 to find the winner
    player1_value = check_hand(player1_list)
    player2_value = check_hand(player2_list)
    # if the card is in the difference rank
    if player1_value > player2_value:
        return 'Player 1 WIN'
    elif player2_value > player1_value:
        return 'Player 2 WIN'
    # if the card is in the same rank
    else:
        # both players in the same rank which is straight and straight flush
        if (player1_value == 9 == player2_value) or (player1_value == player2_value == 5):
            a, b = check_straight(player1_list)
            pl1_sorted_straight = sorted(b.keys(), reverse=True)
            c, d = check_straight(player2_list)
            pl2_sorted_straight = sorted(d.keys(), reverse=True)
            if pl1_sorted_straight[0] > pl2_sorted_straight[0]:
                return 'Player 1 WIN'
            elif pl1_sorted_straight[0] < pl2_sorted_straight[0]:
                return 'Player 2 WIN'
            else:
                return 'Tie'
        # if both players have 4 of a kind
        elif player1_value == player2_value == 8:
            a, b = check_four_of_a_kind(player1_list)
            c, d = check_four_of_a_kind(player2_list)
            rank_value_1 = list_number_rank(b)
            rank_value_2 = list_number_rank(d)
            if rank_value_1[0] > rank_value_2[0]:
                return 'Player 1 WIN'
            else:
                return 'Player 2 WIN'
        # both players have full house card
        elif player1_value == player2_value == 7:
            a, b = check_full_house(player1_list)
            c, d = check_full_house(player2_list)
            rank_value_1 = list_number_rank(b)
            rank_value_2 = list_number_rank(d)
            if rank_value_1[0] > rank_value_2[0]:
                return 'Player 1 WIN'
            elif rank_value_1[0] < rank_value_2[0]:
                return 'Player 2 WIN'
        # both players have flush card
        elif player1_value == player2_value == 6:
            count = 0
            rank_value_1 = check_flush_rank(player1_list)
            rank_value_2 = check_flush_rank(player2_list)
            for index in range(0, 5):
                if rank_value_1[index] > rank_value_2[index]:
                    return 'Player 1 WIN'
                elif rank_value_1[index] < rank_value_2[index]:
                    return 'Player 2 WIN'
                else:
                    count += 1
            if count == 5:
                return 'Tie'
        # both players have three of a kind
        elif player1_value == player2_value == 4:
            count = 0
            a, b = check_three_of_a_kind(player1_list)
            c, d = check_three_of_a_kind(player2_list)
            rank_value_1 = check_pair_rank(b)
            rank_value_2 = check_pair_rank(d)
            for index in range(0, 3):
                if rank_value_1[index] > rank_value_2[index]:
                    return 'Player 1 WIN'
                elif rank_value_1[index] < rank_value_2[index]:
                    return 'Player 2 WIN'
                else:
                    count += 1
            if count == 1:
                return 'Tie'
        # both players have 2 pairs
        elif player1_value == player2_value == 3:
            count = 0
            a, b = check_two_pair(player1_list)
            c, d = check_two_pair(player2_list)
            rank_value_1 = check_pair_rank(b)
            rank_value_2 = check_pair_rank(d)
            # print(rank_value_1, rank_value_2)
            for index in range(0, 3):
                if rank_value_1[index] > rank_value_2[index]:
                    return 'Player 1 WIN'
                elif rank_value_1[index] < rank_value_2[index]:
                    return 'Player 2 WIN'
                else:
                    count += 1
            if count == 3:
                return 'Tie'
        # both players have 1 pair
        elif player1_value == player2_value == 2:
            count = 0
            a, b = check_one_pair(player1_list)
            c, d = check_one_pair(player2_list)
            rank_value_1 = check_pair_rank(b)
            rank_value_2 = check_pair_rank(d)
            for index in range(0, 4):
                if rank_value_1[index] > rank_value_2[index]:
                    return 'Player 1 WIN'
                elif rank_value_1[index] < rank_value_2[index]:
                    return 'Player 2 WIN'
                else:
                    count += 1
            if count == 4:
                return 'Tie'
        # both players have no pair and we check for the highest card
        elif player1_value == player2_value == 1:
            count = 0
            rank_value_1 = check_flush_rank(player1_list)
            rank_value_2 = check_flush_rank(player2_list)
            for index in range(0, 5):
                if rank_value_1[index] > rank_value_2[index]:
                    return 'Player 1 WIN'
                elif rank_value_1[index] < rank_value_2[index]:
                    return 'Player 2 WIN'
                else:
                    count += 1
            if count == 5:
                return 'Tie'


# player1_card = '7S 4D 7H 7S AS'
# player2_card = '7H 7C 7H 6H 5S'
# print(poker_real(player1_card, player2_card))
