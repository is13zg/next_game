import collections
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    print("==end==",start)
    return visited


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')


graph = nx.DiGraph()

gr = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


for x in gr.keys():
    for xx in gr[x]:
        graph.add_edge(x,xx,weight=1)



print(graph.edges())


nx.draw_circular(graph,
         node_color='red',
        node_size=1000,
         with_labels=True)
plt.show()

print(nx.shortest_path(graph, 0, 2))
print(nx.dag_longest_path(graph, weight="weight"))