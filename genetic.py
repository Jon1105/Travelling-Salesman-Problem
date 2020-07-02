import random
import functions as fn
import math


def cross(combination1, combination2, population):
    'Returns a new child combination from 2 parent combinations'
    start = random.randrange(0, len(combination1.order) - 1)  # 1
    end = random.randrange(start+1, len(combination1.order))
    new = list(combination1.order[start:end])
    # count = 0
    for idx in range(len(combination2.order)):
        if combination2.order[idx] not in new:
            new.append(combination2.order[idx])
    return Combination(*new, population=population)


def output():
    pass


class Combination:
    def __getDistance(self):
        return fn.getTotal(
            *[self.points[self.order[num]] for num in range(len(self.points) + 1)])

    def __init__(self, *indices, population):
        self.population = population
        self.points = population.points
        self.order = indices + tuple([indices[0]])
        self.distance = self.__getDistance()
        if self.distance == 0:
            self.fitness = 1
            return
        else:
            self.fitness = 1/self.distance

    def mutate(self, rate):
        for i in range(len(self.order)):
            if random.random() < rate:
                fn.swap(self.order, i, random.randrange(0, len(self.order)))
        return self


class Population:
    def __init__(self, rate, points, numCombinations=200, maxSame=300):
        self.bestDist = math.inf
        self.mutationRate = rate
        self.points = points
        self.max = maxSame
        self.count = 0
        self.totalCombinations = numCombinations
        self.combinations = self.randCombinations()
        print(self.combinations[0].order)
        # for comb in self.combinations:
        #     if comb.distance == 0:
        #         return comb
        self.generations = 0
        self.totalDistance = self.__getTotalDistance()
        self.totalFitness = self.getTotalFitness()
        while self.count < maxSame:
            self.newGeneration()

    def output(self, dist, comb, gen):
        pass

    def getTotalFitness(self):
        return sum([combination.fitness for combination in self.combinations])

    def __getTotalDistance(self):
        total = 0
        for combination in self.combinations:
            self.count += 1
            if combination.distance < self.bestDist:
                self.count = 0
                self.bestCombination = combination
                self.bestDist = combination.distance
                print(
                    f'New Best Distance\nDistance: {self.bestDist}\nCombination: {self.bestCombination.order}\nGeneration: {self.generations + 1}\n')
            total += combination.distance
        return total

    def randCombinations(self):
        s = [i for i in range(len(self.points))]
        ret = []
        for _ in range(self.totalCombinations):
            random.shuffle(s)
            ret.append(Combination(*s, population=self))
        return ret

    def newGeneration(self):
        'Creates new different combinations (children) from "parents"'
        self.combinations = [cross(self.pickParent(), self.pickParent(
        ), self) for _ in range(self.totalCombinations)]
        self.totalDistance = self.__getTotalDistance()
        self.totalFitness = self.getTotalFitness()
        self.generations += 1

    def pickParent(self):
        sortls = sorted(self.combinations,
                        key=lambda comb: comb.fitness, reverse=True)
        randnum = random.random() * self.totalFitness
        ctot = 0
        for comb in sortls:
            if comb.fitness > self.totalFitness - ctot - randnum:
                return comb
            ctot += comb.fitness


points = [
    fn.Location(0, 0, 'origin'),
    fn.Location(10, 10, 'name'),
    fn.Location(3, 9),
    fn.Location(4, 8, 'mid'),
]

pop = Population(rate=0.1, points=fn.getPoints(10),
                 maxSame=1000, numCombinations=400)
print(pop.bestCombination.order)
