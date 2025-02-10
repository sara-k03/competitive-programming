line = input()
n, k = line.split(' ')
n = int(n)
k = int(k)
weights = list(map(int, input().split(' ')))

# Tools: 
# Binary Search 
# Greedy Checking Algorithm: Finds solution at each step in hopes of finding overall solution when iteration is complete 
# max_weight -> current most optimal solution

def partition_exists(weights, max_weight, k):
    weights_sum = 0
    num_boxes = 1

    for weight in weights:
        if (weights_sum + weight) > max_weight:
            # Start a new box
            weights_sum = weight 
            num_boxes += 1
            if num_boxes > k:  
                return False
        else:
            weights_sum += weight  
            
    return True

def binary_search(k):
    maximum_weight = sum(weights)
    minimum_weight = max(weights)

    while minimum_weight < maximum_weight:
        mid = (minimum_weight + maximum_weight) // 2

        if partition_exists(weights, mid, k):
            maximum_weight = mid # if the partition exists with this max weight, we can try going smaller
        else:
            minimum_weight = mid + 1 # we have to try a little larger
    
    return minimum_weight

print(binary_search(k))
