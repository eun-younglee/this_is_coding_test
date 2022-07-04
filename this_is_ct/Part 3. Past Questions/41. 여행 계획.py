# n개의 여행지를 잇는 도로가 존재
# 여행 계획을 세우고 계획이 가능한지 판단하기

def find_parent(parent, x):
    # until finding root node
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):  # initialise
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in data:
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))
result = True
for i in range(len(plan) - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False
        break
if result:
    print("Yes")
else:
    print("No")
