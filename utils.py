from __future__ import print_function, division
from builtins import range


def print_values(V, g):
    for i in range(g.width):
        print("-------------------------------------")
        for j in range(g.height):
            v = V.get((i, j), 0)
            if v >= 0:
                print(" %.2f|" % v, end="")
            else:
                print("%.2f|" % v, end="")
        print("")


def print_policy(P, g):
    print("policy:")
    for i in range(g.width):
        print("-------------------------------------")
        for j in range(g.height):
            a = P.get((i, j), ' ')
            print("  %s  |" % a, end="")
        print("")


def print_grid(grid):
    for i in range(grid.width):
        print("------------------------------")
        for j in range(grid.height):
            if grid.i == i and grid.j == j:
                print("  *  ", end="")
            elif (i, j) in grid.finalState:
                if grid.finalState[(i, j)] > 0:
                    print("  +1 ", end="")
                else:
                    print("  -1 ", end="")
            elif (i, j) in grid.actions:
                print("  .  ", end="")
            else:
                print("  x  ", end="")
        print("")
    print("------------------------------")
