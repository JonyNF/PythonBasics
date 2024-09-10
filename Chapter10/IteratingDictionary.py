def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None

    most_common_enemy = None
    max_so_far = float("-inf")
    for key in enemies_dict:
        if enemies_dict[key] > max_so_far:
            most_common_enemy = key
            max_so_far = enemies_dict[key]
    return most_common_enemy


def main():
    enemies = {"jackal": 3, "kobold": 3, "soldier": 7, "gremlin": 3}
    most_common_enemy = get_most_common_enemy(enemies)
    print(most_common_enemy)
main()
