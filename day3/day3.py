import numpy as np

def _find_num_helper(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c].isdigit():
        return
    current_digit = [grid[r][c]]
    grid[r][c] = '.'
    left_digits = go_left(r, c-1)
    right_digits = go_right(r, c+1)
    
    return int(''.join(left_digits+current_digit+right_digits))
    
def go_left(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c].isdigit():
        return []
    current_digit = [grid[r][c]]
    grid[r][c] = '.'
    left_digits = go_left(r, c-1)
    
    return list(''.join(left_digits+current_digit))
    
def go_right(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c].isdigit():
        return []
    current_digit = [grid[r][c]]
    grid[r][c] = '.'
    right_digits = go_right(r, c+1)
    
    return list(''.join(current_digit+right_digits))

def find_num(r, c):
    number = _find_num_helper(r,c)
    return number if number else 0
    

with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

symbols_set = set(i for i in set(''.join(grid)) 
                  if i != '.' and not i.isdigit())

for i, row in enumerate(grid):
    grid[i] = list(row)

rows = len(grid)
cols = len(grid[0])

"""
current_sum = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] in symbols_set:
            current_sum += find_num(r+1,c)
            current_sum += find_num(r-1,c)
            current_sum += find_num(r,c+1)
            current_sum += find_num(r,c-1)
            current_sum += find_num(r+1,c+1)
            current_sum += find_num(r-1,c-1)
            current_sum += find_num(r-1,c+1)
            current_sum += find_num(r+1,c-1)

print(current_sum)
"""

total_gear_ratio = 0
current_gear_ratio = 1
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '*':
            found_nums = []
            found_nums.append(find_num(r+1,c))
            found_nums.append(find_num(r-1,c))
            found_nums.append(find_num(r,c+1))
            found_nums.append(find_num(r,c-1))
            found_nums.append(find_num(r+1,c+1))
            found_nums.append(find_num(r-1,c-1))
            found_nums.append(find_num(r-1,c+1))
            found_nums.append(find_num(r+1,c-1))
            found_nums = [i for i in found_nums if i!=0]
            if len(found_nums) >= 2:
                total_gear_ratio += np.prod(found_nums)

print(total_gear_ratio)