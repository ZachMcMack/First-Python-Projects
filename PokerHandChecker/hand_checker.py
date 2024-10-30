import numpy

# high card     1
# pair          2
# two pair      3
# trips         4
# straight      5
# flush         6
# full house    7
# quad          8
# running flush 9

# Method: convert each type of hand into a code then directly compare hands with <,> or sort() function

def straight(hand: list):
    hand_num_values = [card[2] for card in hand]
    hand_num_values.sort()
    num_temp = hand_num_values[0]
    for i in range(1, len(hand_num_values)):
        if hand_num_values[i] - num_temp != 1:
            return False
        num_temp = hand_num_values[i]

    return True
        
def flush(hand: list):
    card_temp = hand[0]
    for i in range(1, len(hand)):
        if card_temp[1] != hand[i][1]:
            return False
        card_temp = hand[i]
    return True

def straight_flush(hand: list):
    if flush(hand) and straight(hand):
        return True
    return False

def multiples(hand: list):
    hand_num_values = numpy.transpose(hand)[2] # this grabs an array of just the card values
    u, c = numpy.unique(hand_num_values, return_counts=True)
    counts = [int(n) for n in c.tolist()]
    unique = [int(m) for m in u.tolist()]
    counts_list_sorted = sorted(counts)
    
    if counts_list_sorted == [1,4]:
        value_order = [unique[counts.index(4)]] + [unique[counts.index(1)]]
        hand = 'four of a kind', 
    elif counts_list_sorted == [2,3]:
        value_order = [unique[counts.index(3)]] + [unique[counts.index(2)]]
        hand = 'full house'
    elif counts_list_sorted == [1,2,2]:
        value_order = [unique[counts.index(1)]]
        del unique[counts.index(1)]
        value_order = sorted(unique, reverse=True) + value_order
        hand = 'two pair'
    elif counts_list_sorted == [1,1,3]:
        value_order = [unique[counts.index(3)]]
        del unique[counts.index(3)]
        value_order = value_order + sorted(unique, reverse=True)
        hand = 'three of a kind'
    elif counts_list_sorted == [1,1,1,2]:
        value_order = [unique[counts.index(2)]]
        del unique[counts.index(2)]
        value_order = value_order + sorted(unique, reverse=True)
        hand = 'pair'
    else:
        value_order = sorted(unique, reverse=True)
        hand = 'bust'
    value_order_str = ''
    for value in value_order:
        if int(value) < 10:
            value_order_str += '0' + str(value)
        else:
            value_order_str += str(value)
    value_order_int = int(value_order_str)
    return hand, value_order_int


def determine_code(hand: list):
    hand_num_values = [card[2] for card in hand]
    hand_num_values.sort(reverse=True)
    hand_value, value_order_int = multiples(hand)
    if straight_flush(hand):
        hand_value = 'straight flush'
        leading = 90000000000
    elif hand_value == 'four of a kind':
        leading = 80000000000
    elif hand_value == 'full house':
        leading = 70000000000
    elif flush(hand):
        hand_value = 'flush'
        leading = 60000000000
    elif straight(hand):
        hand_value = 'straight'
        leading = 50000000000
    elif hand_value == 'three of a kind':
        leading = 40000000000
    elif hand_value == 'two pair':
        leading = 30000000000
    elif hand_value == 'pair':
        leading = 20000000000
    else:
        leading = 10000000000
    return [hand_value, leading + value_order_int]