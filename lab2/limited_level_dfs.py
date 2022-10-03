from get_graph import get_graph

def dfs_limit(v, finish, city_from, graph, prev, level, current_level):
    
    if prev[v] != "" or current_level >= level:
        return
    else:
        prev[v] = city_from
        if v == finish:
            print("Way was found!")
            return
        for neighbour in graph[v]:
            dfs_limit(neighbour, finish, v, graph, prev, level, current_level + 1)
            
def get_way(start, finish, prev):
    if prev[finish] == "":
        return ["No path was found!"]
    v = finish
    way = []
    while v != start:
        way.append(v)
        v = prev[v]
    way.append(start)
    return  list(reversed(way))
        

if __name__=="__main__":
    graph = get_graph()
    prev = {}

    for key in graph:
        prev[key] = ""
    finish = "Ниж.Новгород"
    start = "Харьков"
    level = 5
    dfs_limit(start, finish, "", graph, prev, level, 0)
    way = get_way(start, finish, prev) 
    print(way)