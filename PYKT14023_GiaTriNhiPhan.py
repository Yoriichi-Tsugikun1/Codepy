def build_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_tree(arr, tree, node*2, start, mid)
        build_tree(arr, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] = (end - start + 1) - tree[node] # đảo ngược giá trị của node
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if start > right or end < left:
        return
    if start >= left and end <= right:
        tree[node] = (end - start + 1) - tree[node] # đảo ngược giá trị của node
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        return
    mid = (start + end) // 2
    update_range(tree, lazy, node*2, start, mid, left, right)
    update_range(tree, lazy, node*2+1, mid+1, end, left, right)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, lazy, node, start, end, index):
    update_lazy(tree, lazy, node, start, end)
    if start == end:
        return tree[node]
    mid = (start + end) // 2
    if index <= mid:
        return query(tree, lazy, node*2, start, mid, index)
    else:
        return query(tree, lazy, node*2+1, mid+1, end, index)

N, Q = map(int, input().split())

arr = [0] * N
tree = [0] * (4*N)
lazy = [0] * (4*N)

build_tree(arr, tree, 1, 0, N-1)

for i in range(Q):
    x, y = map(int, input().split())
    update_range(tree, lazy, 1, 0, N-1, x-1, y-1)

res = ""
for i in range(N):
    res =res + str(query(tree, lazy, 1, 0, N-1, i))+ ' '
print(res)