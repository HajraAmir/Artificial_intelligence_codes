import random
import numpy as np

num_cities = 10
distance_matrix = np.random.randint(1, 100, size=(num_cities, num_cities))

def init_population(pop_size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]

def fitness(tour):
    return 1 / total_distance(tour)


def total_distance(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1)) + distance_matrix[tour[-1], tour[0]]


def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, tour in enumerate(population):
        current += fitnesses[i]
        if current > pick:
            return tour

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    fill_pos = end
    for gene in parent2:
        if gene not in child:
            child[fill_pos % size] = gene
            fill_pos += 1
    return child

def mutate(tour, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm_tsp(pop_size, mutation_rate, generations):
    population = init_population(pop_size, num_cities)
    for gen in range(generations):
        fitnesses = [fitness(tour) for tour in population]
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        population = new_population
    best_tour = max(population, key=fitness)
    return best_tour, total_distance(best_tour)

best_tour, best_distance = genetic_algorithm_tsp(pop_size=100, mutation_rate=0.1, generations=500)
print("Best Tour:", best_tour)
print("Shortest Distance:", best_distance)

