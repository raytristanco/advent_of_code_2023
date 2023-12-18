import re

def extract_numbers(single_card: str) -> tuple[set, set]:
    win_regex = r'(?<=: ).+(?=\|)'
    winning_str = re.search(win_regex, single_card).group()
    win_set = set(map(int, winning_str.split()))
    
    self_regex = r'(?<=\| ).+'
    self_str = re.search(self_regex, single_card).group()
    self_set = set(map(int, self_str.split()))
    
    return win_set, self_set

with open('input.txt', 'r') as f:
    all_cards = f.read().splitlines()

"""
point_total = 0
for card in all_cards:
    win_set, self_set = extract_numbers(card)
    exponent = len(win_set.intersection(self_set))-1
    point_total += 2**exponent if exponent >= 0 else 0

print(point_total)
"""

total_card_dict = dict(zip([i for i in range(1, len(all_cards)+1)], 
                           [1]*len(all_cards)))
card_total = 0
for card, amount in total_card_dict.items():
    win_set, self_set = extract_numbers(all_cards[card-1])
    cards_won = len(win_set.intersection(self_set))
    for i in range(amount):
        for j in range(cards_won):
            total_card_dict[card+1+j] += 1

print(sum(total_card_dict.values()))