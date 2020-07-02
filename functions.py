import math
import random


class Location():
    def __init__(self, x, y, name='nPoint'):
        self.x = x
        self.y = y
        self.name = name
        self.pos = (x, y)


def getPoints(number, bounds=(0, 0, 10, 10)):
    temp = []
    for i in range(number):
        temp.append(Location(
            random.randint(bounds[0], bounds[2]),
            random.randint(bounds[1], bounds[3]),
            'Point_' + str(i)))
    return temp


def distance(tup1, tup2):
    return math.sqrt((tup2[0] - tup1[0])**2 + (tup2[1] - tup1[1])**2)


def getTotal(*array):
    retTot = 0
    for index in range(len(array)):
        if index == 0:
            continue
        retTot += distance(array[index-1].pos, array[index].pos)
    return retTot


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
