import copy

initial = [
    [1, 2, 3],
    [None, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, None]
]

def print_state(state):
    for row in state:
        for x in row:
            print(x, end=" ")
        print()

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if(state[i][j] != goal[i][j]):
                count += 1
    return count

def empty_tile(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j] == None):
                return i, j
    return -1, -1

def get_neighbours(state):
    i, j = empty_tile(state)
    neighbours = []
    if(i>0):
        tmp = copy.deepcopy(state)
        tmp[i][j], tmp[i-1][j] = tmp[i-1][j], tmp[i][j]
        neighbours.append(tmp)
    if(i<2):
        tmp = copy.deepcopy(state)
        tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]
        neighbours.append(tmp)
    if(j>0):
        tmp = copy.deepcopy(state)
        tmp[i][j], tmp[i][j-1] = tmp[i][j-1], tmp[i][j]
        neighbours.append(tmp)
    if(j<2):
        tmp = copy.deepcopy(state)
        tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]
        neighbours.append(tmp)
    return neighbours

def hill_climbing():
    state = initial
    while(True):
        print('Current State : ')
        print_state(state)
        state_h = heuristic(state)
        print('Heuristic Value = ', state_h)
        print()

        neighbours = get_neighbours(state)
        best_neighbour = min(neighbours, key=heuristic)
        best_neighbour_h = heuristic(best_neighbour)

        if(best_neighbour_h >= state_h):
            print('Stuck in Local Minima.')
            return

        state = best_neighbour
    print('Goal Achieved.')

hill_climbing()












    
