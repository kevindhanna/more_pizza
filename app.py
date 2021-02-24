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

class Pizza:
    def __init__(self, id, *ingredients):
        self.id = id # index of input aray
        self.ingredients = set(ingredients) # set

def read_file(name):
    with open(name, 'r') as f:
        M, T2, T3, T4 = f.readline().strip().split()

        pizzas = []
        for i, line in enumerate(f.readlines()):
            pizzas.append(Pizza(i, *line.strip().split()[1:]))
    return M, T2, T3, T4, pizzas

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

def main():
    M, T2, T3, T4, pizzas = read_file('./test_input.txt')
    deliveries = run(T2, T3, T4, pizzas)
    print_output(deliveries)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
