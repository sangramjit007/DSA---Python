def dfs(node, visited, adjacencyList_Graph, ans):
    visited[node]=1
    ans.append(node)
    for nodes in adjacencyList_Graph[node]:
        if visited[nodes]!=1:
            # visited[nodes]=1
            dfs(nodes, visited, adjacencyList_Graph, ans)
    return ans

def main():
    n=8
    adjacencyList_Graph = [
        [],
        [2,4],
        [1,3,6],
        [2],
        [1,5,7],
        [4,8],
        [2],
        [4,8],
        [5,7],
    ]
    visited=[0]*(n+1)
    ans=[]
    print(dfs(1,visited, adjacencyList_Graph, ans))
main()