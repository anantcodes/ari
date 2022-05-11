from queue import PriorityQueue 
import matplotlib.pyplot as plt 
import networkx as nx 
# for implementing BFS | returns path having lowest cost 
def best_first_search(source, target, n): 
    visited = [0] * n 
    visited[source] = True 
    pq = PriorityQueue() 
    pq.put((0, source)) 
    while pq.empty() == False: 
        u = pq.get()[1] 
        print(u, end=" ") # the path having lowest cost 
        if u == target: 
            break 
        for v, c in graph[u]: 
            if visited[v] == False: 
                visited[v] = True 
                pq.put((c, v)) 
        print() 
# for adding edges to graph 
def addedge(x, y, cost): 
    graph[x].append((y, cost)) 
    graph[y].append((x, cost)) 
G = nx.Graph() 
v = int(input("Enter the number of nodes: ")) 
graph = [[] for i in range(v)] # undirected Graph 
e = int(input("Enter the number of edges: ")) 
print("Enter the edges along with their weights:") 
for i in range(e): 
    x, y, z = list(map(int, input().split())) 
    addedge(x, y, z)
    G.add_edge(x, y, weight = z) 
source = int(input("Enter the Source Node: ")) 
target = int(input("Enter the Target/Destination Node: ")) 
print("\nPath: ", end = "") 
best_first_search(source, target, v)

# Step 1: Place the starting node into the OPEN list.
# Step 2: If the OPEN list is empty, Stop and return failure.
# Step 3: Remove the node n, from the OPEN list which has the lowest value of h(n), and places it in the CLOSED list.
# Step 4: Expand the node n, and generate the successors of node n.
# Step 5: Check each successor of node n, and find whether any node is a goal node or not. If any successor node is goal node, then return success and terminate the search, else proceed to Step 6.
# Step 6: For each successor node, algorithm checks for evaluation function f(n), and then check if the node has been in either OPEN or CLOSED list. If the node has not been in both list, then add it to the OPEN list.
# Step 7: Return to Step 2.
