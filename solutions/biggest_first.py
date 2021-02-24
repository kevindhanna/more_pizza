def run(T2, T3, T4, pizzas):
    deliveries = []

    for x in range(4, 2):
        while len(pizzas) > x:
            delivery = ()
            for x in 4:
                delivery.append(pizzas.pop())
                deliveries.append(delivery)

    return deliveries

if __name__ == '__main__':
    sys.exit(run(sys.argv[1:]))
