import random

def pop_random(items):
    return items.pop(items.randint(len(items)))

# This solution does a fully random distribution of pizzas
# You can optionally pass in a seed to get the same result.
def run(T2, T3, T4, pizzas, seed=None):
    if seed:
        random.seed(seed)

    teams = [2] * T2 + [3] * T3 + [4] * T4
    deliveries = []

    while len(pizzas) and len(teams):
        team = pop_random(teams)
        if len(pizzas) < team:
            continue
        else:
            deliveries.append(tuple(pop_random(pizzas) for i in range(team)))

    return deliveries
