import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.colors import LogNorm
from os import system

#TODO create updating grid separate from the game grid that keeps track of where cells are alive.

def initialize_grid(size):
    return np.random.choice([0, 1], size=(size, size))

def dead_state(rows, cols):
    """creates a 'dead' array consisting of all zeroes from dimensions given in arguments"""
    state = [[0 for i in range(cols)] for j in range(rows)]
    return state

def get_neighbors(state, x, y):
    """given an array and coordinates for a cell, finds if that cell should be 1 or 0"""
    xless = x-1
    xmore = x+1
    yless = y-1
    ymore = y+1
    if xless == -1:
        xless = len(state[0])-1

    if yless == -1:
        yless = len(state)-1

    if xmore == len(state[0]):
        xmore = 0

    if ymore == len(state):
        ymore = 0

    sumx = state[yless][xless] + state[yless][x] + state[yless][xmore] + \
    state[y][xless] + state[y][xmore] + \
    state[ymore][xless] + state[ymore][x] + state[ymore][xmore]
    if sumx == 3:
        return 1

    if sumx >= 3 or sumx < 2:
        return 0

    if state[y][x] == 1 and sumx == 2:
        return 1

    return 0

def play_gol(old_state):
    """given an array, finds what new array should be according to rules and returns it """
    cols = len(old_state[1])
    rows = len(old_state)
    new_state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            new_state[i][j] = get_neighbors(old_state, j, i)
    return new_state

def clear():
 
    _ = system('clear')
    
    
def create_heatmap(grid):
    fig = px.imshow(grid)
    fig.show()
    
def main():
    initial_state = initialize_grid(50)
    heat_grid = initial_state.copy()
    next_state = initial_state
    for i in range(1500):
        next_state = play_gol(next_state)
        heat_grid += next_state
    create_heatmap(heat_grid)


main()
