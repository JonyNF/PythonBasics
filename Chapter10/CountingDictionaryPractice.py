# def count_enemies(enemy_names):
#     enemies_dict = {}
#
#     for enemy_name in enemy_names:
#         counter = 0
#         for n in enemy_names:
#             if enemy_name == n:
#                 counter+=1
#         enemies_dict[enemy_name] = [counter]
#
#     return enemies_dict

def count_enemies(enemy_names):
    enemies_dict = {}

    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1  # Increment count if enemy is already in the dictionary
        else:
            enemies_dict[enemy_name] = 1   # Initialize count if enemy is not in the dictionary yet

    return enemies_dict

def main():
    enemies = ["jackal", "kobold", "soldier","jackal", "kobold", "jackal"]
    print(count_enemies(enemies))

main()