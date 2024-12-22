import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
max_size = 0

def check_positive(cord1: tuple, cord2: tuple) -> bool:
    # 왼쪽 위 좌표 ~ 오른쪽 아래 좌표 안에 있는 영역에 음수가 있는지 확인
    i, j = cord1
    k, l = cord2
    for x in range(i, k + 1):
        for y in range(j, l + 1):
            if grid[x][y] < 0:
                return False
    return True

def get_size(cord1: tuple, cord2: tuple) -> int:
    x1, y1 = cord1
    x2, y2 = cord2
    return (x2 - x1 + 1) * (y2 - y1 + 1)


# 왼쪽 위 좌표, 오른쪽 아래 좌표 잡기
for i in range(n):
    for j in range(m):
        left = (i, j)

        for k in range(i, n):
            for l in range(j, m):
                right = (k, l)

                # 왼쪽 위 좌표 ~ 오른쪽 아래 좌표 안에 있는 영역에 음수가 있는지 확인
                if check_positive(left, right):
                    max_size = max(get_size(left, right), max_size)
                else:
                    continue

print(max_size)
