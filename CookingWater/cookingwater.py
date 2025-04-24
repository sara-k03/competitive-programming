N = int(input())
max_start = 0
min_end = 1000

for _ in range(N):
    a, b = map(int, input().split())
    # smallest range 
    max_start = max(max_start, a)
    min_end = min(min_end, b)

if max_start <= min_end: # t needs to always be in the range 
    print("gunilla has a point")
else:
    print("edward is right")