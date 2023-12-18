from typing import Optional

DIGIT_LIST = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 
              'eight', 'nine']
DIGIT_DICT = dict(zip(DIGIT_LIST, [str(i) for i in range(1, 10)]))

def extract_number(value: str) -> int:
    first_digit, adjusted_value = find_first_digit(value)
    second_digit = find_second_digit(adjusted_value)
    if first_digit and second_digit:
        return int(''.join([first_digit, second_digit]))
    else:
        return int(''.join([first_digit]*2))
    
def find_first_digit(value: str) -> tuple[str, str]:
    character_return = ''
    stack = []
    for i, char in enumerate(value):
        if char.isdigit():
            character_return = char
            break
        else:
            stack.append(char)
            combined_string = ''.join(stack)
            if any(digit_string in combined_string for digit_string in 
                   DIGIT_LIST):
                for word, digit in DIGIT_DICT.items():
                    combined_string = combined_string.replace(word, digit)
                character_return = combined_string[-1]
                break
    
    return character_return, value[i+1:]

def find_second_digit(value: str) -> Optional[str]:
    character_return = ''
    for i in range(-1, -1*len(value)-1, -1):
        combined_string = ''.join(value[i:])
        if combined_string[0].isdigit():
            character_return = combined_string[0]
            break
        else:
            if any(digit_string in combined_string for digit_string in 
                   DIGIT_LIST):
                for word, digit in DIGIT_DICT.items():
                    combined_string = combined_string.replace(word, digit)
                character_return = combined_string[0]
                break
    
    return character_return

with open('input.txt', 'r') as f:
    all_values = f.readlines()
    
current_sum = 0
for value in all_values:
    current_sum += extract_number(value)
    
print(current_sum)