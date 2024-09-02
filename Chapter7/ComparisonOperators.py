def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edwards_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return  is_mustang_edwards_same, is_alphonse_edward_same, is_winry_alphonse_same

def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

def main():
    print(player_1_wins(50, 60))
    print(compare_heights(178, 190, 164, 178))
    print(can_withstand_blow(100, 175))
main()