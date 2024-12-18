n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
for i in range(n - 2):
    for j in range(n - 2):

        count = 0
        for k in range(i, i + 3):
            for l in range(j , j + 3):
                if arr[k][l] == 1:
                    count += 1
        
        if count >= max_cnt:
            max_cnt = count

print(max_cnt)