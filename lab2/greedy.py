from get_graph import get_graph, get_he_graph
from queue import PriorityQueue


def heuristic(v, he_graph):
    return he_graph[v]


def greedy(start, finish, graph, he_graph):
   pqueue = PriorityQueue()
   pqueue.put(start, 0)
   prev = {}
   prev[start] = None

   while not pqueue.empty():
      v = pqueue.get()

      if v == finish:
         break
      
      for neighbour in graph[v]:
         if neighbour not in prev:
            priority = heuristic(neighbour, graph)
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
      # print(graph[v][prev[v]])
      v = prev[v]
   # way += graph[v][start]
   way.append(start)
   return  list(reversed(way)), way_long


if __name__=="__main__":
   graph = get_graph()
   he_graph = get_he_graph()
   
   finish = "Ниж.Новгород"
   start = "Харьков"
   way, long = greedy(start, finish, graph, he_graph)
   print(way, long)