import heapq
import json


# Nodes and edges
edges_dict = {'node201': {'201nav252': 1.5},
              'node252': {'201nav252': 1.5},
              'node202': {'202nav251': 1.5},
              'node251': {'202nav251': 1.5},
              'node203': {'203nav': 1.5},
              'node204': {'204nav250': 1.5},
              'node250': {'204nav250': 1.5},
              'node205': {'205nav': 1.5},
              'node249': {'249nav': 1.5},
              'node206': {'206nav': 1.5},
              'node248': {'248nav': 1.5},
              'node207': {'207nav': 1.5},
              'node208': {'208nav': 1.5},
              'node209': {'209nav': 1.5},
              'node210': {'210nav': 1.5},
              'node211': {'211nav247': 1.5},
              'node247': {'211nav247': 1.5},
              'node212': {'212nav246': 1.5},
              'node246': {'212nav246': 1.5},
              'node213': {'213nav245': 1.5},
              'node245': {'213nav245': 1.5},
              'node214': {'214nav233': 1.5},
              'node233': {'214nav233': 1.5},
              'node215': {'215nav232': 1.5},
              'node232': {'215nav232': 1.5},
              'node216': {'216nav231': 1.5},
              'node231': {'216nav231': 1.5},
              'node217': {'217nav': 1.5},
              'node218': {'218nav': 1.5},
              'node219': {'219nav': 1.5},
              'node220': {'220nav': 1.5},
              'node221': {'221nav230': 1.5},
              'node230': {'221nav230': 1.5},
              'node222': {'222nav': 1.5},
              'node223': {'223nav229': 1.5},
              'node229': {'223nav229': 1.5},
              'node224': {'224nav': 1.5},
              'node225': {'225nav228': 1.5},
              'node228': {'225nav228': 1.5},
              'node226': {'226nav227': 1.5},
              'node227': {'226nav227': 1.5},
              'node244': {'244nav': 1},
              'node243': {'243nav': 1},
              'node242': {'242nav': 1.5},
              'node241': {'241nav': 1.5},
              'node240': {'navcs': 1.5},
              'node239': {'239nav': 1.5},
              'node238': {'238nav': 1.5},
              'node237': {'237nav': 1},
              'node236': {'236nav': 1},
              'node235': {'235nav': 1, 'node234': 4},
              'node234': {'node235': 4},

              '201nav252': {'202nav251': 4, 'node201': 1.5, 'node252': 1.5},
              '202nav251': {'201nav252': 4, 'node202': 1.5, 'node251': 1.5, '203nav': 7},
              '203nav': {'202nav251': 7, '204nav250': 7, 'navcw': 22},
              '204nav250': {'203nav': 7, 'node204': 1.5, 'node250': 1.5, '205nav': 2},
              '205nav': {'204nav250': 2, 'node205': 1.5, '249nav': 3},
              '249nav': {'node249': 1.5, '205nav': 3, '206nav': 2},
              '206nav': {'node206': 1.5, '249nav': 2, '248nav': 2},
              '248nav': {'node248': 1.5, '206nav': 2, '207nav': 5},
              '207nav': {'node207': 1.5, '248nav': 5, '208nav': 3},
              '208nav': {'node208': 1.5, '207nav': 3, '209nav': 7},
              '209nav': {'node209': 1.5, '208nav': 7, '210nav': 7},
              '210nav': {'node210': 1.5, '211nav247': 7, '209nav': 7},
              '211nav247': {'210nav': 7, 'node211': 1.5, 'node247': 1.5, '212nav246': 7},
              '212nav246': {'211nav247': 7, '213nav245': 7, 'node212': 1.5, 'node246': 1.5},
              '213nav245': {'212nav246': 7, 'node212': 1.5, 'node246': 1.5, 'nodelounge': 5},
              'nodelounge': {'nodeloungelane': 22, '213nav245': 5, '214nav233': 10},
              '214nav233': {'nodelounge': 10, '215nav232': 7, 'node214': 1.5, 'node233': 1.5},
              '215nav232': {'214nav233': 7, '216nav231': 7, 'node215': 1.5, 'node232': 1.5},
              '216nav231': {'215nav232': 7, '217nav': 1.5, 'node216': 1.5, 'node231': 1.5},
              '217nav': {'node217': 1.5, '216nav231': 1.5, '218nav': 6},
              '218nav': {'node218': 1.5, '217nav': 6, '219nav': 7},
              '219nav': {'node219': 1.5, '218nav': 7, '220nav': 3},
              '220nav': {'node220': 1.5, '219nav': 3, '221nav230': 9},
              '221nav230': {'220nav': 9, '222nav': 7, 'node221': 1.5, 'node230': 1.5},
              '222nav': {'node222': 1.5, '221nav230': 7, '223nav229': 8},
              '223nav229': {'222nav': 8, '224nav': 3, 'node223': 1.5, 'node229': 1.5},
              '224nav': {'223nav229': 3, '225nav228': 7, 'node224': 1.5, 'navce': 22},
              '225nav228': {'224nav': 7, '226nav227': 4, 'node225': 1.5, 'node228': 1.5},
              '226nav227': {'225nav228': 4, 'node226': 1.5, 'node227': 1.5},
              'nodeloungelane': {'nodelounge': 22, '244nav': 6, '234nav': 6},
              '244nav': {'nodeloungelane': 6, 'node244': 1, '243nav': 8},
              '243nav': {'244nav': 8, 'node243': 1, '242nav': 8},
              '242nav': {'node242': 1, 'navcw': 2, 'navcn': 5, '243nav': 8},
              'navcw': {'203nav': 22, 'navcs': 5, '241nav': 3, '242nav': 2},
              '241nav': {'node241': 1, 'navcw': 3, 'navcs': 3},
              'navcs': {'241nav': 3, 'navcw': 5, 'node240': 2, '239nav': 3, 'navce': 5},
              '239nav': {'node239': 2, 'navcs': 3, 'navce': 3},
              'navce': {'224nav': 22, 'navcs': 5, 'navcn': 5, '239nav': 3, '238nav': 2},
              'navcn': {'navcw': 5, 'navce': 5, '242nav': 4, '238nav': 5, '237nav': 4},
              '238nav': {'navce': 2, 'navcn': 5, '237nav': 4, 'node238': 1},
              '237nav': {'navcn': 4, '238nav': 4, '236nav': 4, 'node237': 1},
              '236nav': {'237nav': 4, '235nav': 4, 'node236': 1},
              '235nav': {'236nav': 4, 'node235': 1, 'node234': 4},
              '234nav': {'nodeloungelane': 6, '235nav': 4}}

# Function to precompute all shortest paths and distances
def precompute_shortest_paths(graph):
    all_shortest_paths = {}
    for source in graph:
        shortest_paths = {}
        for destination in graph:
            path, distance = dijkstra(graph, source, destination)
            shortest_paths[destination] = (path, distance)
        all_shortest_paths[source] = shortest_paths
    return all_shortest_paths

# Function to find the shortest path and distance using Dijkstra's algorithm
def dijkstra(graph, source, destination):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    previous_nodes = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == destination:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes.get(current_node)
            return path[::-1], distances[destination]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, None

# Precompute all shortest paths and distances
all_shortest_paths = precompute_shortest_paths(edges_dict)

# Save precomputed data to a JSON file
with open("precomputed_data.json", "w") as f:
    json.dump(all_shortest_paths, f)

# Function to load precomputed data from the JSON file
def load_precomputed_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Main function
def main():
    # Load precomputed data
    all_shortest_paths = load_precomputed_data("precomputed_data.json")

    source = input("Enter source node: ")
    destination = input("Enter destination node: ")

    if source not in edges_dict or destination not in edges_dict:
        print("Invalid source or destination node.")
        return

    if source in all_shortest_paths and destination in all_shortest_paths[source]:
        path, distance = all_shortest_paths[source][destination]
        print("Shortest path:", ' -> '.join(path))
        print("Distance traveled:", distance)
    else:
        print("There is no path between the source and destination.")

if __name__ == "__main__":
    main()
