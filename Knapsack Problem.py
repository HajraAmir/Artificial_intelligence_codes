import random

items = [(10, 60), (20, 100), (30, 120), (40, 180), (50, 250)]  
max_weight = 100


def init_population_knapsack(pop_size, num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(pop_size)]


def fitness_knapsack(solution):
    total_weight = sum(item[0] * solution[i] for i, item in enumerate(items))
    total_value = sum(item[1] * solution[i] for i, item in enumerate(items))
    return total_value if total_weight <= max_weight else 0


def select_knapsack(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, solution in enumerate(population):
        current += fitnesses[i]
        if current > pick:
            return solution


def crossover_knapsack(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


def mutate_knapsack(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = 1 - solution[i]
    return solution

def genetic_algorithm_knapsack(pop_size, mutation_rate, generations):
    population = init_population_knapsack(pop_size, len(items))
    for gen in range(generations):
        fitnesses = [fitness_knapsack(solution) for solution in population]
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select_knapsack(population, fitnesses)
            parent2 = select_knapsack(population, fitnesses)
            child1 = crossover_knapsack(parent1, parent2)
            child2 = crossover_knapsack(parent2, parent1)
            new_population.extend([mutate_knapsack(child1, mutation_rate), mutate_knapsack(child2, mutation_rate)])
        population = new_population
    best_solution = max(population, key=fitness_knapsack)
    return best_solution, fitness_knapsack(best_solution)

best_solution, best_value = genetic_algorithm_knapsack(pop_size=100, mutation_rate=0.1, generations=500)
print("Best Knapsack Solution:", best_solution)
print("Maximized Value:", best_value)
