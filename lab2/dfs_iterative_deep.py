from limited_level_dfs import dfs_limit
from get_graph import get_graph

def dfs_iterative_deep(start, finish, graph):
    limit = 0
    prev = {}
    prev[finish] = ""
    while prev[finish] == "":
        
        for key in graph:
            prev[key] = ""
            
        dfs_limit(start, finish, "", graph, prev, limit, 0)
        
        limit += 1
    return prev

def get_way(start, finish, prev):
    v = finish
    way = []
    while v != start:
        way.append(v)
        v = prev[v]
    way.append(start)
    return  list(reversed(way))


if __name__=="__main__":
    graph = get_graph()

    start = "Волгоград"
    finish = "Москва"
    prev = dfs_iterative_deep(start, finish, graph)
    way = get_way(start, finish, prev) 
    print(way)