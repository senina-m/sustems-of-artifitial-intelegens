from get_graph import get_graph
from queue import PriorityQueue

#DONO....
def heuristic(a, b, graph):
   # print(f"a={a}, b={b}")
    # if b in graph[a].keys():
    #     return graph[a][b]
    # else:
    #    return 10000
    return 0

def a_star(start, stop, graph):
    pqueue = PriorityQueue()
    pqueue.put(start, 0)
    prev = {}
    cost_so_far = {}
    prev[start] = None
    cost_so_far[start] = 0

    while not pqueue.empty():
        v = pqueue.get()

        if v == finish:
            break
      
        for neighbour in graph[v]:
            new_cost = cost_so_far[v] + graph[v][neighbour]
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic(finish, neighbour, graph)
                pqueue.put(neighbour, priority)
                prev[neighbour] = v
                
    return get_way(start, finish, prev, graph)         
      
def get_way(start, finish, prev, graph):
   v = finish
   way = []
   way_long = 0
   while v != start:
      way.append(v)
      way_long += graph[v][prev[v]]
      print(graph[v][prev[v]])
      v = prev[v]
   # way += graph[v][start]
   way.append(start)
   return  list(reversed(way)), way_long  


if __name__=="__main__":
    graph = get_graph()

    finish = "Орел"
    start = "Волгоград"
    
    way, long = a_star(start, finish, graph)
    print(way, long)
