#!/usr/bin/env python3

def solve(problem):
    if not problem:
        return 0
    while len(problem)!=1:
        if problem[1]=="+":
            newProblem = [int(problem[0])  + int(problem[2])]+problem[3:]
            problem=newProblem
        elif problem[1]=="*":
            newProblem = [int(problem[0]) * int(problem[2])] + problem[3:]
            problem=newProblem

    return problem[0] if problem else 0

def main():
    with open("input.txt",'r',encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            parts = stripped.split()
            print(solve(parts))

if __name__ == '__main__':
    main()