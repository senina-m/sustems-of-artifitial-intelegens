from xmlrpc.client import MAXINT
from get_graph import get_graph

def bfs(v, graph, color, distance):
    queue = []
    queue.append(v)
    color[v] = 1
    distance[v] = 0
    while(len(queue) != 0):
        v = queue.pop()
        color[v] = 1
        for neighbour in graph[v]:
            if color[neighbour] == 0:
                distance[neighbour] = distance[v] + 1
                color[neighbour] = 1
                queue.append(neighbour)
    return
            
def get_way(start, finish, distance):
    v = finish
    way = []
    l = distance[v]
    while l != 0:
        way.append(v)
        for key in graph[v]:
            if distance[key] == l - 1:
                l= l-1
                v = key
    way.append(start)   
    return  list(reversed(way))
graph = get_graph()
color = {}
distance = {}

for key in graph:
    color[key] = 0
    distance[key] = MAXINT
start = "Симферополь"
finish = "Москва"
bfs(start, graph, color, distance)
# [print(f"{key} =>  {distance[key]}") for key in distance]
way = get_way(start, finish, distance) 
print(way)