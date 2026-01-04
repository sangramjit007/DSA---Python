# Adjacency List Representation of Graph
def pr():
    for i in range(len(lst)):
        print(i, " -> ",lst[i])
n = 5 # nodes/vertices
m = 6 # edges
edges = [[1,2], [2,4], [3,4], [1,3], [3,5],[5,4]]
# 1 based index graph
lst = [[] for _ in range(n+1)]
# Before Operation printing matrix
pr()
print("--------------------------------------")
for u, v in edges: # unpacking the list
    # This is a Undirected Graph
    lst[u].append(v)
    lst[v].append(u)
# After Operation printing matrix
pr()

