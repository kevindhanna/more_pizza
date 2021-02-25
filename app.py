# Pizza helper functions, parse from input etc
# agree on pizza interface

#input
# 5   1   2   1
# 3   onion   pepper   olive
# 3   mushroom   tomato   basil
# 3   chicken   mushroom   pepper
# 3   tomato   mushroom   basil
# 2   chicken   basil

# [ pizza1, pizza2, pizza3 ]

import sys
from functools import reduce

class Pizza:
    def __init__(self, id, *ingredients):
        self.id = id # index of input aray
        self.ingredients = set(ingredients) # set

    def __str__(self):
        return f"id: {self.id}, ingreds: {self.ingredients}"

    def __repr__(self):
        return self.__str__()

def parse_file(lines):
    with open(name, 'r') as f:
        M, T2, T3, T4 = lines[0].strip().split()

        pizzas = []
        for i, line in enumerate(lines[1:]):
            pizzas.append(Pizza(i, *line.strip().split()[1:]))
        
        return T2, T3, T4, pizzas

def read_file(name):
    with open(name, 'r') as f:
        M, T2, T3, T4 = f.readline().strip().split()

        pizzas = []
        for i, line in enumerate(f.readlines()):
            pizzas.append(Pizza(i, *line.strip().split()[1:]))

        return T2, T3, T4, pizzas

def score_total(deliveries):
    return sum(score_delivery(d) for d in deliveries)

def score_delivery(pizzas):
    unique_ingredients = reduce(lambda a, b: a | b.ingredients, pizzas, set())
    return len(unique_ingredients) ** 2

def print_delivery(delivery):
    args = [len(delivery)]
    for pizza in delivery:
        args.append(pizza.id)

    print(' '.join(args))

def print_output(deliveries):
    print(len(deliveries))
    for delivery in deliveries:
        print_delivery(delivery)

def run(T2, T3, T4, pizzas):
    deliveries = []
    #create deliveries (tuple with id's) and add them to deliveries
    return deliveries

def main(filename='./test_input.txt'):
    M, T2, T3, T4, pizzas = read_file(filename)
    deliveries = run(T2, T3, T4, pizzas)
    print_output(deliveries)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
