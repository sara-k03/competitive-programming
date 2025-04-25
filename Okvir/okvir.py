def frame(M, N, U, L, R, D, crossword):
    total_rows = U + M + D # up, down
    total_cols = L + N + R # left, right
    
    framed = []
    
    for i in range(total_rows):
        row = []
        for j in range(total_cols):
            if (U <= i < U + M) and (L <= j < L + N):  # words
                crossword_row = i - U
                crossword_col = j - L
                row.append(crossword[crossword_row][crossword_col])
            else: # frame
                if (i + j) % 2 == 0:
                    row.append('#')
                else:
                    row.append('.')
        framed.append(''.join(row))
    return framed

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
crossword = []
for i in range(M):
    crossword.append(input())

framed = frame(M, N, U, L, R, D, crossword)

for line in framed:
    print(line)