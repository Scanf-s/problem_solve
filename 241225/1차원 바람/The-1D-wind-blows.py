import sys

n, m, q = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
wind = [list(sys.stdin.readline().split()) for _ in range(q)]


def propagate_up(cur_row, direction):
    if cur_row > 0:
        for i in range(m):
            if arr[cur_row][i] == arr[cur_row - 1][i]:
                next_direction = 'R' if direction == 'L' else 'L'
                shift(cur_row - 1, next_direction)
                propagate_up(cur_row - 1, next_direction)
                break

def propagate_down(cur_row, direction):
    if cur_row < n - 1:
        for i in range(m):
            if arr[cur_row][i] == arr[cur_row + 1][i]:
                next_direction = 'R' if direction == 'L' else 'L'
                shift(cur_row + 1, next_direction)
                propagate_down(cur_row + 1, next_direction)
                break


def shift(row:int, direction: str):
    if direction == 'L':
        temp = arr[row][0]
        for i in range(m - 1):
            arr[row][i] = arr[row][i + 1]
        arr[row][-1] = temp
    else:
        temp = arr[row][-1]
        for i in range(m - 1, 0, -1):
            arr[row][i] = arr[row][i - 1]
        arr[row][0] = temp


def main():
    for row, direction in wind:
        # direction 대로 row번째 행 밀기
        shift(int(row), direction)

        # cur_row 기준으로 위쪽 전파
        propagate_up(cur_row=int(row), direction=direction)

        # cur_row 기준으로 아래쪽 전파
        propagate_down(cur_row=int(row), direction=direction)

    for row in arr:
        print(*row)

main()
