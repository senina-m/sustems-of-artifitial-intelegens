from get_graph import get_graph

def bi_directional_search(start, finish, graph):
    if start == finish:
        return [start]
    active = {start: [start], finish: [finish]}
    # Vertices we have already examined.
    visited = set()

    while len(active) > 0:
        active_copy = list(active.keys()) #modifiyable copy of active
        for v in active_copy:
            v_path = active[v]
            v_n = set(graph[v]) - visited #current neighbors
            if len(v_n.intersection(active_copy)) > 0:
                #check if current v neighbors has active v, as neighbor
                for union_v in v_n.intersection(active_copy): 
                    if v_path[0] != active[union_v][0]:
                        active[union_v].reverse()
                        return active[v] + active[union_v]
            #if there is no more neighbors we can remove whal path from the start
            if len(set(v_n) - visited - set(active_copy))  == 0:                 
                active.pop(v, None)
                visited.add(v)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                for neighbor_vertex in v_n - visited - set(active_copy):
                    active[neighbor_vertex] = v_path + [neighbor_vertex]
                    active_copy.append(neighbor_vertex)
                active.pop(v, None)
                visited.add(v)

    return ["No path was found!"]

if __name__=="__main__":
    graph = get_graph()
    
    finish = "Ниж.Новгород"
    start = "Харьков"
    way = bi_directional_search(start, finish, graph)
    print(way)

