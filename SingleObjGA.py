import random
import string

letter_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

class Dna:
    def __init__(self, length):
        self.string = "".join(random.choice(
            letter_set) for _ in range(length))
        self.length = length
        self.fitness = -1

    def __str__(self):
        print("string:" + str(self.string) + "Fitness: " + str(self.fitness))


def generate_species(population, length):
    return[Dna(length) for _ in range(population)]


def selection(species):
    # species = sorted(species, key=lambda dna: dna.fitness, reverse=True)
    species = sorted(species, key=lambda dna: dna.fitness, reverse=True)
    new_species = species[0:int(0.2*population)]
    return new_species


def crossover(species):
    required_children = population - len(species)
    for _ in range(0, required_children):
        parentA = random.choice(species)
        parentB = random.choice(species)
        split = random.randint(0, parentA.length-1)
        childA = Dna(word_length)
        childB = Dna(word_length)
        childA.string = parentA.string[0:split] + parentB.string[split:]
        childB.string = parentB.string[0:split] + parentB.string[split:]
        species.append(childA)
        species.append(childB)
    return species


def mutation(species, prob):
    for dna in species:
        mutate = random.random()
        if (mutate <= prob):
            split = random.randint(0, dna.length-1)
            string_letters = list(dna.string)
            string_letters[split] = random.choice(list(letter_set))
            dna.string = "".join(string_letters)
    return species


def fitness(species):
    # print("run")
    for dna in species:
        score = 0
        for i in range(0, word_length):
            if dna.string[i] == word[i]:
                score += (1/word_length)
        dna.fitness = score
        # print(score)
    return species


def check_result(species):
    # print("run")
    species = sorted(species, key=lambda dna: dna.fitness, reverse=True)
    if species[0].fitness >= 0.99:
        print("Final Word: " + str(species[0].string) + " Fitness: " + str(
            species[0].fitness))
        exit(0)
    else:
        print("Best Word: " + str(species[0].string) + " Fitness: " + str(
            species[0].fitness))

population = 100
generations = 10000
word = "this is a sentence"
word_length = len(word)


def main():
    species = generate_species(population, word_length)
    species = fitness(species)
    for i in range(generations):
        print("Generation: " + str(i) + "\n")
        species = selection(species)
        species = crossover(species)
        species = mutation(species, 0.1)
        species = fitness(species)
        check_result(species)


if __name__ == "__main__":
    main()
