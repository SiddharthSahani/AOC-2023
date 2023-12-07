
from collections import Counter


file = open("day-07/inputs/part_2.txt", 'r')
file_contents = file.read()


def get_hand_type(hand):
    c = Counter(hand)
    joker = c['J'] if 'J' in c else 0
    if joker != 0: del c['J']

    c_vals = sorted(c.values(), reverse=True)
    length = len(c_vals)

    if length == 1 or length == 0:
        return 6
    if length == 2:
        if c_vals[0] + joker == 4:
            return 5
        return 4
    if length == 3:
        if c_vals[0] + joker == 3:
            return 3
        return 2
    if length == 4:
        if c_vals[0] + joker == 2:
            return 1
    return 0



c_to_pow_map = [
    'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'
]
c_to_pow_map.reverse()
def get_power_list(hand):
    type = get_hand_type(hand)
    l = [type]
    for char in hand:
        l.append(c_to_pow_map.index(char))
    return l


hand_info_list = []
for line in file_contents.splitlines():
    hand, bidding = line.split()
    hand_info_list.append((get_power_list(hand), hand, int(bidding)))

hand_info_list.sort(key=lambda x: x[0])

total_winnings = 0
for rank, hand_info in enumerate(hand_info_list, start=1):
    total_winnings += hand_info[2] * rank

print(total_winnings)
