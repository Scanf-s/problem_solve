# K^2 + (K + 1)^2 <= 5 * 찾은동전 개수
# K = p 인 경우, Grid의 기준점 (i, j)에서 최대 p칸 이동 가능 -> bfs 사용
# bfs 사용해서 움직인 거리 count하고, 움직인 곳에 동전이 놓여있다면 찾은 동전개수++
# bfs 끝나고 맨 마지막에 위에 식 계산해서 부등식 만족하면 max_gold 비교\
# n : size of grid
# m : price of gold

from queue import Queue

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_gold = 0
    k = 0
    while True:
        # print(f"k = {k}")
        for i in range(n):
            for j in range(n):
                # 모든 (i, j)에 대해, (i, j) 중심으로 k번 이동해서 검사
                gold_cnt = 0
                visited = [[False] * n for _ in range(n)]
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                q = Queue()
                q.put((i, j, 0))
                visited[i][j] = True
                if grid[i][j] == 1:
                    gold_cnt += 1

                # bfs
                while not q.empty():
                    cur_x, cur_y, mov = q.get()

                    if mov >= k:
                        continue

                    for direction in directions:
                        nx, ny = cur_x + direction[0], cur_y + direction[1]

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            q.put((nx, ny, mov + 1))
                            visited[nx][ny] = True
                            if grid[nx][ny] == 1:
                                gold_cnt += 1
                
                # print()
                # print(f"{i}, {j} gold count : {gold_cnt}")
                # print(f"{k * k + (k + 1) * (k + 1)} <= {m * gold_cnt}")
                if k * k + (k + 1) * (k + 1) <= m * gold_cnt:
                    max_gold = max(max_gold, gold_cnt)
                # print(f"max gold : {max_gold}")

        if k >= n:
            break
        else:
            k += 1
    return max_gold

print(solve())
