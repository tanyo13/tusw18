#!/usr/bin/env python3

import sys

def solve(n, x, lst_ab):
    bmax = max([b for [a,b] in lst_ab])
    s = sum([a*b for [a,b] in lst_ab])
    return s + bmax*x

def readQuestion():
    [n, x] = [int(s) for s in sys.stdin.readline().strip().split()]
    lst_ab = [[int(s) for s in line.strip().split()] for line in sys.stdin]
    return (n, x, lst_ab)

def main():
    n, x, lst_ab = readQuestion()
    answer = solve(n, x, lst_ab)
    print(answer)
    
if __name__ == '__main__':
    main()
