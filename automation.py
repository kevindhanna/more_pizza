import os
import importlib

from . import app

def parse_lines(lines):
    M, T2, T3, T4 = next(lines).strip().split()

    pizzas = []
    for i, line in enumerate(lines):
        pizzas.append(app.Pizza(i, *line.strip().split()[1:]))
    
    return T2, T3, T4, pizzas

def load_solution(arg):
    if isinstance(arg, str):
        return importlib.import_module('solutions.' + arg).run
    elif callable(arg):
        return arg
    elif hasattr(arg, 'run'):
        return arg.run
    
def load_input(arg):
    if arg in os.listdir('inputs'):
        with open(arg) as f:
            return parse_lines(f.readlines())
    elif isinstance(arg, str):
        return parse_lines(arg.split())
    else:
        return arg

def run(solution, input):
    runner = load_solution(solution)
    args = load_input(input)

    deliveries = runner(*args)
    score = app.score_total(deliveries)
    
    return score, deliveries

if __name__ == '__main__':
    run('random', 'example')