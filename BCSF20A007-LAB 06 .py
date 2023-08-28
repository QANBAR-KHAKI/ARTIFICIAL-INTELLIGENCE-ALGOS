from random import random
import random


def population_generation():
    initial_state = [random.randint(0, 7) for _ in range(8)]
    # print(" The Initial State is : ", initial_state)
    return initial_state


def population_():
    population = []
    i = 0
    while i < 8:  # here I am generating 8 different random states
        a = population_generation()
        # if a not in self.initial:
        population.append(a)
        i += 1
    return population


def calculate_fitness(state):
    clashes = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                clashes += 1
    return 28 - clashes


def random_selection(population, calculate_fitness):
    fitness = []
    total_perc = 0
    for i in population:
        n = calculate_fitness(i)
        fitness.append(n)
        total_perc += n
    # print(" The total percentage of the fitness is : ", total_perc)
    # print(" The Fitness Set is : ", fitness)
    fintess_in_percentage = []
    for i in range(len(fitness)):
        v = (fitness[i] / total_perc) * 100
        fintess_in_percentage.append(v)
    # print("Fitness in percentage : ", fintess_in_percentage)
    r_value = random.randint(0, 100)
    index = -1
    curr_sum = 0
    for i in range(len(population)):
        curr_sum += fintess_in_percentage[i]
        if r_value <= curr_sum:
            index = i
            break
    return population[index]


def reproduce(x, y):
    n = len(x)
    crossover_point = random.randint(1, n)

    child1 = x[:crossover_point] + y[crossover_point:]
    return child1


def Genetic_Function(population, calculate_fitness):
    m = len(population)
    n = 0
    best_child = []
    min_clashes = 28
    while n < 100000:
        new_population = []
        for i in range(8):
            x = random_selection(population, calculate_fitness)
            y = random_selection(population, calculate_fitness)
            child1 = reproduce(x, y)  # crossover
            mut_child = mutate(child1)
            new_population.append(mut_child)
        population = new_population

        for i in range(m):

            clash = 28 - calculate_fitness(population[i])
            if clash == 0:
                return population[i]

            if clash < min_clashes:
                min_clashes = clash
                best_child = population[i]
        n = n + 1

    return best_child


# Perform bit mutation
def mutate(state):
    n = len(state)
    index = random.randint(0, n - 1)
    MUTATION_RATE = 0.01

    if random.random() < MUTATION_RATE:
        state[index] = random.randint(0, n - 1)
    return state


# -----------------------------      MAIN FUNCTION    ------------------
# ------->------------->--------------->---------------->--------------->

p = population_()
# state = random_selection(p, calculate_fitness)
# for i in p:
#     print(i)
#     print("Fitness Value: ", calculate_fitness(i))
# print(state)
optimal_state = Genetic_Function(p, calculate_fitness)
clash = calculate_fitness(optimal_state)
print("The Best Child state is : ", optimal_state)
print("The Number of the Clashes : ", 28 - clash)
