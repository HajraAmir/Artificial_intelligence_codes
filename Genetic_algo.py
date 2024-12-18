import random
def initialize_population(pop_size, string_length):
    return [''.join(random.choice('01') for i in range(string_length)) for j in range(pop_size)]

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    parent1 = tournament_selection(population, fitness_scores)
    parent2 = tournament_selection(population, fitness_scores)
    return parent1, parent2

def tournament_selection(population, fitness_scores, tournament_size=3):
    participants = random.sample(range(len(population)), tournament_size)
    best = max(participants, key=lambda idx: fitness_scores[idx])
    return population[best]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual, mutation_rate):
    return ''.join(
        bit if random.random() > mutation_rate else str(1 - int(bit))
        for bit in individual
    )


def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(best_fitness)]
        print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Individual = {best_individual}")
        
    
        if best_fitness == string_length:
            break
        
    
        new_population = []
        for _ in range(pop_size // 2): 
            parent1, parent2 = select_parents(population, fitness_scores)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            new_population.extend([mutate(offspring1, mutation_rate), mutate(offspring2, mutation_rate)])
        population = new_population
    
    return best_individual, best_fitness


if __name__ == "__main__":
    string_length = 10       
    pop_size = 20            
    num_generations = 100    
    mutation_rate = 0.01     
    
    best_solution, best_fitness = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
    print(f"\nOptimal Solution: {best_solution} with Fitness = {best_fitness}")
