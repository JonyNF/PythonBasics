def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    else: print("You don't have the necessary materials to perform this craft (Iron Ore)")

    return inventory

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)
        print(f"User ID:{player_ids[i]}")

    return player_ids


def main():
    inventory = ["Leather", "Iron Ore", "Healing Potion"]
    smelt_ore(inventory)
    print(inventory)
    generate_user_list(5)
main()