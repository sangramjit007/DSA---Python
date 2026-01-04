from collections import deque
'''
Algorithm of BFS (Visited_Array, Queue, Answer_Array, Adjacency_List/Dictionary to represent Graph)
1) Starts with a Starting_Node (Assume Node=1 Here)
2) Now we have to initialize a 
    2.1) "Visited - Array of N+1 with 0", 
    2.2) "Just take a Queue(empty initially)", 
    2.3) "Just take an answer array where you store your answer"
3) Initialize/Append Queue with starting_node (Assume Node=1 Here)
4) Initialize(store 1 to that index in) the visited array # mark as visited
5) Untill Queue becomes empty
    5.1) pop left_most node from the queue
    5.2) mark that node_index in the visited array to 1 # mark as visited
    5.3) Add that node to the answer array
    5.4) ###----------Check How Many Nodes Are Connected to that Node-------### 
        5.4.1) ###---If that nodes aren't visited---### >>then>> Repeat the same for each and Every Node
            5.4.1.1) Mark as visited 
            5.4.1.2) Append the node to the Queue
'''
def bfs(graph_edges, n, starting_node):
    visited=[0]*(n+1) # 2.1) "Visited — Array of N+1 with 0"
    my_queue = deque() # 2.2) "Just take a Queue(empty initially)"
    ans = [] # 2.3) "Just take an answer array where you store your answer"
    my_queue.append(starting_node)  # 4) Initialize/Append Queue with starting_node (Assume Node=1 Here)
    visited[starting_node]=1  # 5) Initialize(store 1 to that index in) the visited array
    while len(my_queue)!=0:
        node = my_queue.popleft()
        visited[node]=1
        ans.append(node)
        for nodes in graph_edges[node]:
            if visited[nodes]!=1:
                visited[nodes]=1
                my_queue.append(nodes)
    return ans

def main():
    n = 9
    graph_edges = [
        [],
        [2, 8],
        [1, 3, 4],
        [2],
        [2, 5],
        [4, 6],
        [5, 7],
        [6, 8],
        [1, 7, 9],
        [8],
    ]
    print(bfs(graph_edges, n, 3))
main()