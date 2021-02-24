def get_best_pizza(pizzas, delivery):
    best = {"pizza": None, "diff": 0}

    for pizza in pizzas:
        current = 0
        for d in delivery:
            diff = len(d.ingredients - pizza.ingredients)
            if current < diff:
                current = diff
        if best['diff'] < current:
            best['pizza'] = pizza
            best['diff'] = current
    return best['pizza']

def run(T2, T3, T4, pizzas):
    deliveries = []

    # 4 person teams
    while len(pizzas) > 4 and T4 > 0:
        delivery = [pizzas.pop()]
        for x in range(3):
            pizza = get_best_pizza(pizzas, delivery)
            delivery.append(pizza)
            pizzas.remove(pizza)
        deliveries.append(delivery)
        T4 -= 1

    # 3 person teams
    while len(pizzas) > 3 and T3 > 0:
        delivery = (pizzas.pop())
        for x in range(2):
            pizza = get_best_pizza(pizzas, delivery)
            delivery.append(pizza)
            pizzas.remove(pizza)
        deliveries.append(delivery)
        T3 -= 1

    # 2 person teams
    while len(pizzas) > 2 and T2 > 0:
        delivery = (pizzas.pop())
        pizza = get_best_pizza(pizzas, delivery)
        delivery.append(pizza)
        pizzas.remove(pizza)
        deliveries.append(delivery)
        T2 -= 1

    return deliveries


if __name__ == '__main__':
    sys.exit(run(sys.argv[1:]))
