import sys

n, t = map(int, sys.stdin.readline().split())
upper = list(map(int, sys.stdin.readline().split()))
middle = list(map(int, sys.stdin.readline().split()))
lower = list(map(int, sys.stdin.readline().split()))
arr = []
for el in upper:
    arr.append(el)
for el in middle:
    arr.append(el)
for el in lower:
    arr.append(el)

for i in range(t):
    temp = arr[-1]
    for j in range(3*n - 1, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = temp

for i in range(n):
    print(arr[i], end=" ")
print()
for i in range(n, 2 * n):
    print(arr[i], end=" ")
print()
for i in range(2 * n, 3 * n):
    print(arr[i], end=" ")