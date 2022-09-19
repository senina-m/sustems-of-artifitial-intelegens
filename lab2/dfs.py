from get_graph import get_graph

def dfs(v, finish, city_from, graph, prev):
    
    if prev[v] != "":
        return
    else:
        prev[v] = city_from
        if v == finish:
            print("Way was found!")
            return
        for neighbour in graph[v]:
            dfs(neighbour, finish, v, graph, prev)
            
def get_way(start, finish, prev):
    v = finish
    way = []
    while v != start:
        way.append(v)
        v = prev[v]
    way.append(start)
    return  list(reversed(way))
        


graph = get_graph()
prev = {}

for key in graph:
    prev[key] = ""
start = "Волгоград"
finish = "Москва"
dfs(start, finish, "", graph, prev)
way = get_way(start, finish, prev) 
print(way)