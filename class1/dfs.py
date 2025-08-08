graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E']),
    }
print("Ammen Ramali: ")
def dfs(graph, node, visited):
    if node not in visited:
        print("node:"+node)
        print(f"visited:{visited}")
        visited.append(node)
        print(f"set value: {graph[node]}")
        for n in graph[node]:
            print("n:"+n)
            dfs(graph,n,visited)
    print(f"visited_ before returned:{visited}")
    return visited
visited = dfs(graph1, 'A', [])
print(visited)


# a->b->d->b 
# (base) amn@MacBook-Pro-2 class1 % python dfs.py
# Ammen Ramali: 
# node:A
# visited:[]
# set value: {'C', 'B'}
# n:C
# node:C
# visited:['A']
# set value: {'A', 'F'}
# n:A
# visited_ before returned:['A', 'C']
# n:F
# node:F
# visited:['A', 'C']
# set value: {'E', 'C'}
# n:E
# node:E
# visited:['A', 'C', 'F']
# set value: {'B', 'F'}
# n:B
# node:B
# visited:['A', 'C', 'F', 'E']
# set value: {'D', 'A', 'E'}
# n:D
# node:D
# visited:['A', 'C', 'F', 'E', 'B']
# set value: {'B'}
# n:B
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# n:A
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# n:E
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# n:F
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# n:C
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# n:B
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# visited_ before returned:['A', 'C', 'F', 'E', 'B', 'D']
# ['A', 'C', 'F', 'E', 'B', 'D']
