import math


def calculate_damage(sword = 5, arrow = 5, spear = 15,  dagger = 7.5, fireball =20):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    print(total_damage)
    print(average_damage)
    return total_damage, average_damage

def main():

    calculate_damage()

main()