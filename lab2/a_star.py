from get_graph import get_graph, get_he_graph
from queue import PriorityQueue

def heuristic(v, he_graph):
    return he_graph[v]

def a_star(start, finish, graph, he_graph):
    pqueue = PriorityQueue()
    pqueue.put(start, 0)
    prev = {}
    path_v = {} # how far is v from the start
    prev[start] = None
    path_v[start] = 0

    while not pqueue.empty():
        v = pqueue.get()

        if v == finish:
            break
      
        for neighbor in graph[v]:
            new_cost = path_v[v] + graph[v][neighbor]
            if neighbor not in path_v or new_cost < path_v[neighbor]:
                path_v[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, he_graph)
                pqueue.put(neighbor, priority)
                prev[neighbor] = v
                
    return get_way(start, finish, prev, graph)         
      
def get_way(start, finish, prev, graph):
   v = finish
   way = []
   way_long = 0
   while v != start:
      way.append(v)
      way_long += graph[v][prev[v]]
    #   print(graph[v][prev[v]])
      v = prev[v]
   # way += graph[v][start]
   way.append(start)
   return  list(reversed(way)), way_long  


if __name__=="__main__":
    graph = get_graph()
    he_graph = get_he_graph()
    
    finish = "Ниж.Новгород"
    start = "Харьков"
    
    way, long = a_star(start, finish, graph, he_graph)
    print(way, long)
