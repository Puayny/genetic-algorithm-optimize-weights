#testing genetic algo. Create lists of N numbers which add up to a specified number
import random
import numpy as np
import math
from functools import reduce

def create_indiv(indiv_len, indiv_min, indiv_max):
    return [random.randint(indiv_min, indiv_max) for i in range(indiv_len)]

def init_pop(ppn_num, indiv_len, indiv_min, indiv_max):
    return [create_indiv(indiv_len, indiv_min, indiv_max) for i in range(ppn_num)]

def calc_sum_fitness(indiv, target_sum):
    func = sum(indiv)
    # func = reduce(lambda x,y: x*y, indiv)
    return 100 - abs(func - target_sum)


def calc_avg_ppn_sum_fitness(ppn, target_sum):
    return sum([calc_sum_fitness(indiv, target_sum) for indiv in ppn])



def choose_top_n_percent(ppn, idx, survival_chance_top):
    num_survive = math.floor(len(ppn) * survival_chance_top)
    idx_survive = idx[:num_survive]
    return [ppn[idx] for idx in idx_survive]

def random_select_for_survival(ppn, idx, survival_chance_top, survival_chance_remainder):
    num_survive_top = math.floor(len(ppn) * survival_chance_top)
    idx_remainder = idx[num_survive_top:]
    selected_for_survival = []
    for idx in idx_remainder:
        if survival_chance_remainder > random.random():
            selected_for_survival.append(ppn[idx])
    return selected_for_survival

def crossover_remainder(ppn, target_ppn):
    new_ppn = []
    num_indiv_to_generate = target_ppn - len(ppn)
    indiv_len = len(ppn[0])
    while len(new_ppn) < num_indiv_to_generate:
        male_idx = random.randint(0, len(ppn)-1)
        female_idx = random.randint(0, len(ppn) - 1)
        if male_idx != female_idx:
            # crossover
            num_to_crossover_male = random.randint(1,indiv_len-1)
            num_to_crossover_female = indiv_len - num_to_crossover_male
            male_idx_to_crossover = random.sample(range(indiv_len), num_to_crossover_male)
            female_idx_to_crossover = random.sample(range(indiv_len), num_to_crossover_female)
            new_indiv = [ppn[male_idx][i] for i in male_idx_to_crossover]
            new_indiv.extend([ppn[female_idx][i] for i in female_idx_to_crossover])
            new_ppn.append(new_indiv)
    return new_ppn

def random_mutate_indiv(indiv, mutate_chance_indiv):
    for idx_val in range(len(indiv)):
        if random.random() < mutate_chance_indiv:
            indiv[idx_val] += (random.random() - 0.5)*10
    return indiv

def random_mutate(ppn, mutate_chance_ppn, mutate_chance_indiv):
    for idx_indiv in range(2, len(ppn)):
        if random.random() < mutate_chance_ppn:
            ppn[idx_indiv] = random_mutate_indiv(ppn[idx_indiv], mutate_chance_indiv)
    return ppn

def evolve(ppn, target_sum, survival_chance_top, survival_chance_remainder, mutate_chance_ppn, mutate_chance_indiv):
    new_ppn = []

    fitness_levels = np.array([calc_sum_fitness(indiv, target_sum) for indiv in ppn])
    fitness_levels_sorted_idx = fitness_levels.argsort()[-1::-1]

    new_ppn.extend(choose_top_n_percent(ppn, fitness_levels_sorted_idx, survival_chance_top))

    new_ppn.extend(random_select_for_survival(ppn, fitness_levels_sorted_idx, survival_chance_top, survival_chance_remainder))

    new_ppn.extend(crossover_remainder(new_ppn, len(ppn)))

    new_ppn = random_mutate(new_ppn, mutate_chance_ppn, mutate_chance_indiv)

    avg_fitness_history.append(calc_avg_ppn_sum_fitness(ppn, target_sum))

    print([calc_sum_fitness(indiv, target_sum) for indiv in new_ppn])

    return new_ppn


ppn = init_pop(10, 6, 1, 100)

avg_fitness_history = []

for i in range(100):
    ppn = evolve(ppn, 100, 0.25, 0.10, 0.2, 0.3)

print(ppn[0])
print(ppn[1])