# Online Python - IDE, Editor, Compiler, Interpreter


def  BFS(graph , start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node  not in visited:
            visited.append(node)
            queue += graph[node]
    print(visited)
       
       
       
       
def DFS(graph , start , visited = None):
    if visited is None:
        visited = [] 
    if start not in visited:
        visited.append(start)
        for  negh in graph[start]:
            DFS(graph , negh , visited)
    return visited
            # TODO: write code...

graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['A'],
    'D': ['C', 'A']
}

BFS(graph ,'A')
list = DFS(graph ,'A')
print(list)