from Chapter7.ComparisonOperators import player_1_wins


def print_status(player_health):
    if player_health <= 0:
        print("dead")
    elif player_health <= 5:
        print("injured")
    else: return "healthy"
    print("status check complete")

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    else:
        return "incorrect amount"

def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")

def test_swords(swords, army_size):
    print(f"Amount of swords: {swords}")
    print(f"Army size is: {army_size}")
    print("Checking status...")
    check_swords_for_army(swords,army_size)
    print("=====================================")

def check_high_score(player_name, high_scoring_player_name,low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else: return "neither"

def does_attack_hit(attack_roll, armor_class):
    if attack_roll != 1 and attack_roll >= armor_class:
        return True
    elif attack_roll == 20:
        return True
    else: return False

def should_serve_customer(customer_age, on_break, time):
    if (customer_age >= 21 and on_break == False) and (5 <= time <= 10):
        return True
    else: return False

def main():
    test(0)
    test(5)
    test(3)
    test_swords(7, 5)
    print(should_serve_customer(21, False, 7))
main()
