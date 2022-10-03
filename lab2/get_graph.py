
def get_graph():
    distances = []
    cities = set()
    
    with open("data", "r") as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(" ")
            distances.append(elements)
            cities.add(elements[0])
            cities.add(elements[1])
    f.close()
    
    graph = {}
    for city in cities:
        graph[city] = {}
        
    for distance in distances:
        graph[distance[0]][distance[1]] = int(distance[2])
        graph[distance[1]][distance[0]] = int(distance[2])
    
    return graph

def get_he_graph():
    distance = {}
    
    with open("data_heuristic", "r") as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(" ")
            # print(f"0:{elements[0]} 1:{elements[1]}")
            distance[elements[0]] = int(elements[1][:-1])
    f.close()
    
    return distance