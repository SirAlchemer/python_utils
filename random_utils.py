import random


# ______random_slot_setter_______#
def random_slot_setter(number_of_slots, posible_rolls):
    machine = [None] * number_of_slots
    for i in range(len(machine)):
        machine[i] = random.choice(posible_rolls)
    return machine
