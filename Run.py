from loadPoints import *
from scipy.spatial import distance
from graphs import *
import numpy as np


class Run():
    def __init__(self):
        self.n_iterations = 5000
        self.population_size = 50
        self.origin = 0  # Define the origin point index

        self.x_points = LoadPoints().create_random_points()[0]
        self.y_points = LoadPoints().create_random_points()[1]

        # It will mutate x% of the time
        self.mutation_rate = 0.01

    # Gets the cities positions defined on loadPoints file and places the origin at the position 0
    def get_points(self):
        pairs_of_points = list(zip(self.x_points, self.y_points))
        # Define the origin
        self.swap(pairs_of_points, 0, self.origin)
        return pairs_of_points

    def replace_and_pop(self, element, replacements):
        # print(replacements)
        element = replacements[-1]
        replacements.pop()
        return element

    # Perform the crossover operation. The breaking point is at a random position

    def crossover(self, parent1, parent2):
        if (parent1 == parent2):
            res = parent1
        else:
            break_point = random.randint(1, len(parent1))
            parent1_used_slice = parent1[0:break_point]
            parent2_used_slice = parent2[break_point:]
            parent1_not_used_slice = parent1[break_point:]
            parent2_not_used_slice = parent2[:break_point]
            if parent1_used_slice == parent2_not_used_slice:
                res = parent1
            else:
                replacements = list(set(parent2_not_used_slice) - set(parent1_used_slice))
                to_replace = list(set(parent2_used_slice).intersection(parent1_used_slice))
                slice2 = list(
                    map(lambda x: x if x not in to_replace else self.replace_and_pop(x, replacements), parent2_used_slice))
                res = parent1_used_slice + slice2
        return res

    # Chooses the two cities to swap
    def pick_two_swappers(self, points):
        # Never swap position 0
        while 1:
            point_a = random.randint(1, len(points) - 1)
            point_b = random.randint(1, len(points) - 1)
            if point_a != point_b:
                break
        return (point_a, point_b)

    def swap(self, a, i, j):
        cp = list(a)
        temp = cp[i]
        a[i] = cp[j]
        a[j] = temp
        return cp

    def shuffle(self, picked_one):
        swappers = self.pick_two_swappers(picked_one)
        swapped = self.swap(picked_one, swappers[0], swappers[1])
        return swapped

    def first_population(self, picked_one):
        new_pop = list()
        number_of_shuffles = 30
        for i in range(self.population_size):
            for j in range(number_of_shuffles):
                new_pop.append(self.shuffle(picked_one))
        return new_pop

    def new_population(self, last_generation, fitnesses):
        population = list()
        for i in range(self.population_size):
            index_parentA = self.pick_one(fitnesses)
            index_parentB = self.pick_one(fitnesses)

            parentA = last_generation[index_parentA]
            parentB = last_generation[index_parentB]

            if parentA == parentB:
                parentA = self.mutate(parentA)

            child = self.crossover(parentA, parentB)
            population.append(child)
        return population

    def pick_one(self, fitnesses):
        i = 0
        r_number = random.random()
        while 1:
            r_number = r_number - fitnesses[i]
            if r_number - fitnesses[i] < 0:
                break
            i += 1
        return i - 1

    def calc_distance(self, points):
        dist = 0
        for i in range(len(points)):
            if i != (len(points) - 1):
                dist = dist + distance.euclidean(points[i], points[i + 1])
            else:
                dist = dist + distance.euclidean(points[i], points[0])
        return dist

    def calc_fitness(self, distance):
        fitness = 1 / (distance + 0.001)
        return fitness

    # Normalizes fitness array
    def normalize_fitness(self, fitnesses):
        fitnesses = np.array(fitnesses)
        summed_list = np.sum(fitnesses)
        normalized_fits = fitnesses / summed_list
        return normalized_fits

    # For the mutation, I just swap two of the cities randomly
    def mutate(self, points):
        swappers = self.pick_two_swappers(points)
        new_points = self.swap(points, swappers[0], swappers[1])
        return new_points

    def run(self):
        cities = self.get_points()
        rec_dist = float('inf')
        # initialize the first population by shuffling

        new_pop = self.first_population(cities)
        for i in range(self.n_iterations):
            print("Iteration "+str(i))
            distances = list()
            fitness = list()
            for j in range(self.population_size):
                distances.append(self.calc_distance(new_pop[j]))
                fitness.append(self.calc_fitness(distances[j]))
            fitness = self.normalize_fitness(fitness)
            new_pop = self.new_population(new_pop, fitness)

            index = self.pick_one(fitness)
            cities = new_pop[index]
            fitness_list = list(fitness)


            best_of_generation_index = fitness_list.index(max(fitness_list))
            # mutate
            r = random.random()
            if r < self.mutation_rate:
                cities = self.mutate(cities)

            # Check if this is the record distance
            new_dist = distances[best_of_generation_index]
            if new_dist < rec_dist:
                rec_dist = distances[best_of_generation_index]
                rec_cities = cities
                Graphs().create_points_plot(rec_cities)
        return rec_dist


print(Run().run())
