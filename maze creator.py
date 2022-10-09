# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time

## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 11
width = 27
maze = []

# Print final maze
printMaze(maze)