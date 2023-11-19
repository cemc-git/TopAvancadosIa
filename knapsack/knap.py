import item as item
import random as r
items = [item.item(0,2,5),item.item(1,3,8),item.item(2,5,12),item.item(3,7,10),item.item(4,1,3),item.item(5,4,7),item.item(6,6,6),item.item(7,8,15),item.item(8,9,9),item.item(9,10,8)]
bagWeight = 15
initialPopulation = []
populationLength = 10
mutationP = 0.05
genSize = 100
bestSolutions = []
def battle(player1,player2):
    sum1 = 0
    sum2 = 0
    for i in range(len(player1)):
        if player1[i] == 1:
            sum1 += items[i].value
        if player2[i] == 1:
            sum2 += items[i].value
    if sum1 > sum2:
        return player1
    else:
        return player2

def tournament(population):
    percentage = calculateValues(population)
    choosingPlayer1 = r.randint(0,sum(percentage))
    choosingPlayer2 = r.randint(0,sum(percentage))
    aux = 0
    player1 = 0
    player2 = 0
    for i in range(len(population)):
        aux += percentage[i]
        if(aux>=choosingPlayer1):
            player1 = i
            break
    aux = 0
    for i in range(len(population)):
        aux += percentage[i]
        if(aux>=choosingPlayer2):
            player2 = i
            break
    winner = battle(initialPopulation[player1],initialPopulation[player2])
    return winner

def crossover(dad1,dad2):
    breakpoint = r.randint(0,len(dad1)-1)
    firstPart = dad1[:breakpoint]
    secondPart = dad2[breakpoint:]
    child = firstPart + secondPart
    if checkSolution(child):
        if child is None:
            crossover(dad1, dad2)
        return child
    else:
        crossover(dad1,dad2)

def mutate(child):
    mutated = child
    for i in range(len(mutated)):
        p = r.random()
        if p < mutationP:
            if mutated[i] == 0:
                mutated[i] = 1
            else:
                mutated[i] = 0
    if checkSolution(mutated):
        return mutated
    else:
        return mutate(child)


def newGen(pop):
    new_gen = []
    while len(new_gen) < populationLength:
        dad1 = tournament(pop)
        
        dad2 = tournament(pop)
        
        child = crossover(dad1,dad2)
        if child is not None:
            child = mutate(child)

            new_gen.append(child)
    return new_gen

def checkSolution(candidate):
    auxSum = 0
    for i in range(len(candidate)):
        if candidate[i] == 1:
            auxSum += items[i].weight
    if auxSum > bagWeight:
        
        return False
    else:
        
        return True
def iniatePop():
    while len(initialPopulation) < populationLength:
        candidate = []
        for i in range(len(items)):
            candidate.append(r.randint(0,1))
        if(candidate not in initialPopulation):
            if(checkSolution(candidate)):
                initialPopulation.append(candidate)

def calculateValues(initialPopulation):
    values = []
    for person in initialPopulation:
        sum = 0
        for i in range(len(person)):
            if person[i] == 1:
                sum += items[i].value
        values.append(sum)
    return values


iniatePop()
print(calculateValues(initialPopulation))

for i in range(genSize):
    initialPopulation = newGen(initialPopulation)
    bestSolutions.append(max(calculateValues(initialPopulation)))
print(calculateValues(initialPopulation))
print(bestSolutions)