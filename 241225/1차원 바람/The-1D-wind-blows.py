import sys

n, m, q = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
wind = [list(sys.stdin.readline().split()) for _ in range(q)]


def check_if_same_element(cur_row, other_row):
    for i in range(m):
        if arr[cur_row][i] == arr[other_row][i]:
            return True
    return False


def propagate_up(cur_row, direction):
    while True:
        up_row = cur_row - 1
        if up_row < 0:
            break
        if check_if_same_element(cur_row, up_row):
            next_direction = 'R' if direction == 'L' else 'L'
            shift(up_row, next_direction)
            direction = next_direction
            cur_row = up_row
        else:
            break
                
def propagate_down(cur_row, direction):
    while True:
        down_row = cur_row + 1
        if down_row > n - 1:
            break

        if check_if_same_element(cur_row, down_row):
            next_direction = 'R' if direction == 'L' else 'L'
            shift(down_row, next_direction)
            direction = next_direction
            cur_row = down_row
        else:
            break
                

def shift(cur_row:int, cur_direction: str):
    if cur_direction == 'R':
        temp = arr[cur_row][0]
        for i in range(m - 1):
            arr[cur_row][i] = arr[cur_row][i + 1]
        arr[cur_row][-1] = temp
    else:
        temp = arr[cur_row][-1]
        for i in range(m - 1, 0, -1):
            arr[cur_row][i] = arr[cur_row][i - 1]
        arr[cur_row][0] = temp


def main():
    for row, direction in wind:
        # direction 대로 row번째 행 밀기
        shift(cur_row=int(row) - 1, cur_direction=direction)

        # cur_row 기준으로 위쪽 전파
        propagate_up(cur_row=int(row) - 1, direction=direction)

        # # cur_row 기준으로 아래쪽 전파
        propagate_down(cur_row=int(row) - 1, direction=direction)

    for row in arr:
        print(*row)

main()