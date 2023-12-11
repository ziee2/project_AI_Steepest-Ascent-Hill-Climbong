distances = {
    'RS_A': {'RS_B': 3.5, 'RS_C': 9.1, 'RS_D': 5.9},
    'RS_B': {'RS_A': 3.5, 'RS_C': 8.5, 'RS_D': 8.5},
    'RS_C': {'RS_A': 9.1, 'RS_B': 8.5, 'RS_D': 9},
    'RS_D': {'RS_A': 5.9, 'RS_B': 8.5, 'RS_C': 9}
}

# Calculate the path based on the random solution
def path_length(distances, solution):
    cycle_length = 0
    for i in range(len(solution) - 1):
        current_location = solution[i]
        next_location = solution[i + 1]
        cycle_length += distances[current_location][next_location]
    return cycle_length

def neighbors(distances, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((neighbor, path_length(distances, neighbor)))

    return neighbors

def steepest_ascent_hill_climbing(distances):
    current_solution = ['RS_A', 'RS_B', 'RS_C', 'RS_D']
    current_path = path_length(distances, current_solution)

    while True:
        print("melalui rute: ",current_solution)
        neighbors_list = neighbors(distances, current_solution)
        
        best_neighbor, best_neighbor_path = min(neighbors_list, key=lambda x: x[1])

        if best_neighbor_path < current_path:
            current_solution = best_neighbor
            current_path = best_neighbor_path
        else:
            break

    return current_path, current_solution

final_solution = steepest_ascent_hill_climbing(distances)
print("Rute terpendek \n", final_solution[1])
print("Total jarak dari rute terpendek: ", final_solution[0])