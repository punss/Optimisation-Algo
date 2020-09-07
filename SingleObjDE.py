import numpy as np
from random import choice, randint, random, choices, seed
import math
import sys

D = 2  # Number of parameters in function to be optimised
NP = 100 # Population Size (Must be greater than or equal to 4)
seed(1)


class Vector:
    def __init__(self, D):
        self.params = (np.ones((1, D)).tolist())[0]


def fofx(ind):
    x, y = ind.params[0], ind.params[1]
    fx = -(math.cos(x)*math.cos(y)*math.exp(-(((x-math.pi)**2) + ((y-math.pi)**2))))
    return fx


def init_pop(NP):
    vector_array = []
    for _ in range(NP):
        vector = Vector(D)
        for idx in range(len(vector.params)):
            vector.params[idx] = random()
        vector_array.append(vector)
    return vector_array


def check_objective(target_vector, trial_vector):
    if fofx(target_vector) >= fofx(trial_vector):
        return trial_vector
    elif fofx(trial_vector) > fofx(target_vector):
        return target_vector


def crossover(vector_array, cross_prob=0.6, weight=0.8):

    new_pop = []

    for i in range(NP):
        # print(len(vector_array))
        temp_arr = []
        for el in vector_array:
            temp_arr.append(el)
        target_vector = temp_arr[i]
        temp_arr.remove(target_vector)
        choice_arr = choices(temp_arr, k=3)

        noisy_vector = Vector(D)
        for j in range(D):
            noisy_vector.params[j] = (
                choice_arr[0].params[j] - choice_arr[1].params[j]
                ) * weight + choice_arr[2].params[j]

        trial_vector = Vector(D)
        for j in range(D):
            if random() <= cross_prob:
                trial_vector.params[j] = noisy_vector.params[j]
            else:
                trial_vector.params[j] = target_vector.params[j]

        new_pop.append(check_objective(target_vector, trial_vector))
    return new_pop


def main():
    vector_population = init_pop(NP)
    print("Initial population: ")
    print(min(fofx(el) for el in vector_population))
    print("")
    
    ans = 1000
    va = [0, 0]

    for generation in range(1,1001):
        vector_population = crossover(vector_population)
        print("Generation "+str(generation)+":")
        # for el in vector_population:
        #     print(fofx(el))
        # ans = (min(fofx(el) for el in vector_population))
        
        for el in vector_population:
        	temp = ans
        	ans = min(ans, fofx(el))
        	if ans != temp:
        		va[0], va[1] = el.params[0], el.params[1]

        if(ans == -1):
        	break
        print("")

    print(va, ans)

if __name__ == "__main__":
    main()
