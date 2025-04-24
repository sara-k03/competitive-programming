from itertools import combinations

N = int(input())

ingredients = []
for _ in range(N):
    line = input()                   
    parts = line.split(' ')          
    sourness = int(parts[0])         
    bitterness = int(parts[1])       
    ingredients.append((sourness, bitterness)) 

n = len(ingredients)
min_diff = 1000000000 # max possible

for r in range(1, n + 1):
    for combo in combinations(ingredients, r): # all ingredients choose r 
        sourness = 1
        bitterness = 0
        for s, b in combo:
            sourness *= s
            bitterness += b
        min_diff = min(min_diff, abs(sourness - bitterness))


print(min_diff)
