from get_graph import get_graph

graph = get_graph()
for city in graph:
    print(f"{city} ==> {graph[city]}")