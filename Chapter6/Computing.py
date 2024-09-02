#exponents 2^3 = 2**3 in python
# to ++ you use +=/-=/*=/ /=


def update_player_score(current_score, increment):
    new_score = current_score + increment
    print(new_score)
    return new_score

def get_hurt(current_health, damage):
    current_health-=damage
    print(current_health)
    return current_health

def max_players_on_server():
    small_server_cap = 1.024e18
    medium_server_cap = 1.024e19
    large_server_cap = 1.024e20
    print(f"{small_server_cap:.0f}")
    print(f"{medium_server_cap:.0f}")
    print(f"{large_server_cap:.0f}")
    return small_server_cap, medium_server_cap, large_server_cap


def main():
    update_player_score(5,6)
    get_hurt(100, 25)
    max_players_on_server()
    print(0b111110)


main()