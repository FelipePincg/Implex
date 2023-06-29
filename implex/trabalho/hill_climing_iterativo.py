import  random

def hill_climbing_iterative(problem, max_iterations):
    current_state = problem.initial_state()
    
    for _ in range(max_iterations):
        neighbors = problem.generate_neighbors(current_state)
        best_neighbor = None
        best_score = problem.evaluate(current_state)
        
        for neighbor in neighbors:
            neighbor_score = problem.evaluate(neighbor)
            if neighbor_score > best_score:
                best_neighbor = neighbor
                best_score = neighbor_score
        
        if best_neighbor is None:
            break
        
        current_state = best_neighbor
    
    return current_state