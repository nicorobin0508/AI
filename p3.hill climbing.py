import random

def hill_climbing(problem):
    current_state = problem.initial_state()
    
    while True:
        neighbors = problem.get_neighbors(current_state)
        if not neighbors:
            break
        
        next_state = max(neighbors, key=lambda state: problem.evaluate(state))
        
        if problem.evaluate(next_state) <= problem.evaluate(current_state):
            break
        
        current_state = next_state
    
    return current_state

class SimpleProblem:
    def initial_state(self):
        return random.randint(0, 100)

    def get_neighbors(self, state):
        return [state - 1, state + 1]

    def evaluate(self, state):
        return -(state - 50) ** 2 + 2500

problem = SimpleProblem()
solution = hill_climbing(problem)
print("Solution:", solution)
