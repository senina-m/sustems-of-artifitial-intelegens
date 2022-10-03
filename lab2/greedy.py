from get_graph import get_graph
from queue import PriorityQueue

#DONO....
def heuristic(a, b, graph):
   # print(f"a={a}, b={b}")
   if b in graph[a].keys():
      return graph[a][b]
   else:
      return 10000

def greedy(start, finish, graph):
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
            priority = heuristic(finish, neighbour, graph)
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
    for city in graph:
      print(graph[city])

    start = "Волгоград"
    finish = "Москва"
    way, long = greedy(start, finish, graph)
    print(way, long)