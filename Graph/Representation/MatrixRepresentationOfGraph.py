def pr():
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[i][j], end="\t")
        print("")
# This is a Undirected Graph
n = 5 # nodes/vertices
m = 6 # edges
edges = [[1,2], [2,4], [3,4], [1,3], [3,5],[5,4]]
# 1 based index graph
matrix = [[0 for _ in range(n+1)] for i in range(n+1)] # List Comprehension
# Before Operation printing matrix
pr()
print("--------------------------------------")
for u, v in edges: # unpacking the list
    matrix[u][v] = 1
    matrix[v][u] = 1
# After Operation printing matrix
pr()

