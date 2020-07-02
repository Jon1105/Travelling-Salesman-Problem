import functions as fn
import math
import datetime

numLocations = 3
# gridBounds = [xMin, yMin, xMax, yMax]
gridBounds = (-10, -10, 10, 10)


def recur(ls, count, final):
    amount = len(ls) - 1
    if count == amount:
        final.append([i for i in ls])
    else:
        for i in range(count, amount+1):
            fn.swap(ls, count, i)
            recur(ls, count+1, final)
            fn.swap(ls, count, i)


def getPermutations(number):
    temp = []
    recur([i for i in range(number)], 0, temp)
    return temp

# %%


def brute(numPoints=None, bounds=None, points=None):
    bestCombination = None
    'Finds shortest path going through each city from a list of cities (City) while returning to the original point'

    # Input Logic
    if points:
        numPoints = len(points)
    elif not points:
        if not numPoints:
            raise ValueError(
                'numPoints is required to generate cities')
        if bounds:
            points = fn.getPoints(numPoints, bounds)
        elif not bounds:
            points = fn.getPoints(numPoints)

    # Warning of Duration: O(n!)
    if numPoints > 10:
        response = input(
            'This will take several minutes\nPress "y" to continue or "c" to cancel:\n')
        if response.lower() != 'y':
            return
    points += [points[0]]
    # Make sure Salesman Returns to original location
    recordDist = math.inf
    permutations = getPermutations(numPoints)
    print(len(permutations))
    for combination in permutations:
        temp = fn.getTotal(*[points[num]
                             for num in combination + [combination[0]]])
        if temp < recordDist:
            recordDist = temp
            bestCombination = combination + [combination[0]]
    print(bestCombination)
    print('From', ' '.join([(str(points[num].pos) + ' to')
                            for num in bestCombination])[:-3])
    print(
        f'Distance: {fn.getTotal(*[points[num] for num in bestCombination])}')
    return bestCombination


# %%
begin_time = datetime.datetime.now()

# n = int(input('Number of Points:\n'))


brute(points=[
    fn.Location(0, 0, 'origin'),
    fn.Location(10, 10, 'name'),
    fn.Location(3, 9),
    fn.Location(4, 8, 'mid')
])
print('Time', str(datetime.datetime.now() - begin_time))
