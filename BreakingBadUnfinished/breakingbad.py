# NOT FINISHED

# python3 breakingbad.py < 1.in 
from itertools import combinations

def split_into_two_groups(input_list):
    n = len(input_list)
    all_splits = []
    
    # Iterate over all possible sizes of the first group
    for i in range(n + 1):
        for group1 in combinations(input_list, i):
            group2 = [item for item in input_list if item not in group1]
            all_splits.append((list(group1), group2))
    
    return all_splits

n = int(input())
ingredients_list = []
for i in range(0, n):
    ingredients_list.append(input())

s = int(input())
illegal_pairs = []
for i in range(0, s):
    illegal_pairs.append(input())

ingredient_combinations = split_into_two_groups(ingredients_list)



