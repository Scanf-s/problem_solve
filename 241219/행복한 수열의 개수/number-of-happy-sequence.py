n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
happy_row = 0
happy_col = 0

if m == 1:
    print(2 * n)
else:
    for i in range(n):
        count = 1
        for j in range(1, n):
            if arr[i][j - 1] == arr[i][j]:
                count += 1
                if count >= m:
                    happy_row += 1
                    break
            else:
                count = 1

    for i in range(n):
        count = 1
        for j in range(1, n):
            if arr[j - 1][i] == arr[j][i]:
                count += 1
                if count >= m:
                    happy_row += 1
                    break
            else:
                count = 1

    print(happy_col + happy_row)
