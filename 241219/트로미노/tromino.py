complex_shape = [
    [[1, 0], [1, 1]],
    [[1, 1], [0, 1]],
    [[1, 1], [1, 0]],
    [[0, 1], [1, 1]]
]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for shape in complex_shape:
    for i in range(n - 1):
        for j in range(m - 1):
            cur_sum = 0

            cur_sum += arr[i][j] if shape[0][0] == 1 else 0
            cur_sum += arr[i][j + 1] if shape[0][1] == 1 else 0
            cur_sum += arr[i + 1][j] if shape[1][0] == 1 else 0
            cur_sum += arr[i + 1][j + 1] if shape[1][1] == 1 else 0
    
            if cur_sum >= max_sum:
                max_sum = cur_sum

for i in range(n):
    for j in range(m - 2):
        cur_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

        if cur_sum >= max_sum:
            max_sum = cur_sum

for i in range(n - 2):
    for j in range(m):
        cur_sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j]

        if cur_sum >= max_sum:
            max_sum = cur_sum

print(max_sum)
