premium_ground_shipping = 125.00


def ground_shipping(weight):
    if weight <= 2:
        return weight * 1.5 + 20
    elif (weight > 2) and (weight <= 6):
        return weight * 3 + 20
    elif (weight > 6) and (weight <= 10):
        return weight * 4 + 20
    else:
        return weight * 4.75 + 20


def drone_shipping(weight):
    if weight <= 2:
        return weight * 4.5
    elif (weight > 2) and (weight <= 6):
        return weight * 9
    elif (weight > 6) and (weight <= 10):
        return weight * 12
    else:
        return weight * 14.25


def cheapest_option(weight):
    ground_cost = ground_shipping(weight)
    drone_cost = drone_shipping(weight)
    if (ground_cost < drone_cost) and (ground_cost < premium_ground_shipping):
        print('Ground shipping is the cheapest option at £' + str(ground_cost))
    elif (drone_cost < ground_cost) and (drone_cost < premium_ground_shipping):
        print('Drone shipping is the cheapest option at £' + str(drone_cost))
    else:
        print('Premium ground shipping is the cheapest option at £' +
              str(premium_ground_shipping))


cheapest_option(4.8)
cheapest_option(41.5)
