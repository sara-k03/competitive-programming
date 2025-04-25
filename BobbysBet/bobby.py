def solve(R, S, X, Y, W): # S sided die, value of at least R, X out of Y rolls, W bet
    p = (S - R + 1) / S  # probability 
    dp = []
    for _ in range(Y + 2):
        row = [0.0] * (Y + 2)
        dp.append(row)
    
    dp[0][0] = 1.0  # 0 rolls, 0 successes

    for i in range(Y):
        for j in range(i + 1):
            # success
            dp[i + 1][j + 1] += dp[i][j] * p
            # failure
            dp[i + 1][j] += dp[i][j] * (1 - p)

    prob = 0.0
    for j in range(X, Y + 1):
        prob += dp[Y][j]


    expected_return = prob * W

    if ( expected_return > 1 ):
        return "yes"
    else:
        return "no"

N = int(input())
results = []
for _ in range(N):
    R, S, X, Y, W = map(int, input().split())
    results.append(solve(R, S, X, Y, W))
    
for res in results:
    print(res)