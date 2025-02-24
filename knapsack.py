n, k = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

T = [0] * (k + 1)

for i in range(n):
    for j in range(k, w[i] - 1, -1):
        T[j] = max(T[j], T[j - w[i]] + v[i])

print(max(T))