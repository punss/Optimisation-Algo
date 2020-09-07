import numpy as np
from random import choice, randint, random, choices, seed

D = 2  # Number of parameters in function to be optimised
NP = 100 # Population Size (Must be greater than or equal to 4)
seed(1)


class Vector:
    def __init__(self, D):
        self.params = (np.ones((1, D)).tolist())[0]
    def fofx(self):
        fx = 0
        for i in self.params:
            fx += i**2
        return fx

'''def fofx(ind):
    fx = 0
    for i in ind.params:
        fx += i**2;
    return fx
'''

def init_pop(NP):
    vector_array = []
    for _ in range(NP):
        vector = Vector(D)
        for idx in range(len(vector.params)):
            vector.params[idx] = random()
        vector_array.append(vector)
    return vector_array


def check_objective(target_vector, trial_vector):
    if target_vector.fofx() >= trial_vector.fofx():
        return trial_vector
    elif target_vector.fofx() < trial_vector.fofx():
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
    print(min(el.fofx() for el in vector_population))
    print("")
    
    for generation in range(1,1001):
        vector_population = crossover(vector_population)
        print("Generation "+str(generation)+":")
        # for el in vector_population:
        #     print(fofx(el))
        ans = (min(el.fofx() for el in vector_population))
        print (ans)
        if(ans<= 1e-10): return
        print("")


if __name__ == "__main__":
    main()
