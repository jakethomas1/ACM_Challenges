import heapq
location_distances = { #Note distances are approximations in meters
    "EL": {
        "SH2": 450,  
    },
    "SH2": {
        "SBSB": 25,  
        "KL": 300,   
        "UH": 325,   
    },
    "SBSB": {
        "KL": 320,   
        "UH": 310,   
    },
    "KL": {
        "UH": 80,    
    },
    "UH": {
        "AH": 66,    
    },
    "AH": {
        "KL": 126,   
        "MH": 15,    
        "SH1": 20,   
    },
    "MH": {
        "SH1": 40,   
    },
    "SH1": {
        "AH": 20,    
    },
}



def dijkstra_with_penalty(graph, start, end, penalty=40):
    # Initialize distances to infinity, except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = penalty  # Add 40 meters for the start (top floor)
    
    # Priority queue to select the node with the smallest tentative distance
    priority_queue = [(penalty, start)]  # (distance, node)
    
    # To keep track of the shortest path
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we reached the destination node
        if current_node == end:
            # Reconstruct the shortest path
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return distances[end], path
        
        # Skip if this node has already been visited with a shorter path
        if current_distance > distances[current_node]:
            continue
        
        # Visit each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # Add penalty when traveling to a neighbor (except the last destination)
            distance = current_distance + weight
            if neighbor != end:  # If the destination isn't the end node, add penalty
                distance += penalty
            
            # If we found a shorter path to the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return float('inf'), []  # Return infinity if no path is found

# Example: Find the shortest path from "EL" to "MH"
start = "EL"
end = "MH"
distance, path = dijkstra_with_penalty(location_distances, start, end)

print(f"Shortest distance from {start} to {end}: {distance} meters")
print(f"Shortest path: {' -> '.join(path)}")
