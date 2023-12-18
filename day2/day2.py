import re
import numpy as np

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
COLORS = ['red', 'green', 'blue']
MAX_DICT = dict(zip(COLORS, [MAX_RED, MAX_GREEN, MAX_BLUE]))

def is_game_valid(single_game_dict: dict) -> bool:
    for color in COLORS:
        if single_game_dict[color] > MAX_DICT[color]:
            return False
    
    return True

def analyze_game(single_game: str) -> dict:
    single_game_dict = {}
    for color in COLORS:
        regex_pattern = r'\d+(?= {})'.format(color)
        single_game_dict[color] = count_single_color(single_game, 
                                                     regex_pattern)

    return single_game_dict
    
def count_single_color(single_game: str, pattern: str) -> int:
    if single_color_amt := re.search(pattern, single_game):
        return int(single_color_amt.group())
    else:
        return 0
    
def extract_id_if_nonvalid(game_string: str) -> int:
    id_regex_pattern = r'(?<=Game )\d+(?=:)'
    game_id = int(re.search(id_regex_pattern, game_string).group())
    
    game_regex = r'(?<=: ).+'
    actual_game = re.search(game_regex, game_string).group()
    
    single_games = actual_game.split('; ')
    for single_game in single_games:
        single_game_dict = analyze_game(single_game)
    
        if not is_game_valid(single_game_dict):
            return 0
        
    return game_id

def calculate_min_power(game_string: str) -> int:
    game_regex = r'(?<=: ).+'
    actual_game = re.search(game_regex, game_string).group()
    
    min_dict = dict(zip(COLORS, [0]*len(COLORS)))
    single_games = actual_game.split('; ')
    for single_game in single_games:
        single_game_dict = analyze_game(single_game)
        for color in COLORS:
            min_dict[color] = single_game_dict[color] if \
                single_game_dict[color] > min_dict[color] else min_dict[color]
    
    return np.prod(list(min_dict.values()))
    
with open('input.txt', 'r') as f:
    all_games = f.readlines()
    
current_sum = 0
for game in all_games:
    current_sum += calculate_min_power(game)
    
print(current_sum)