def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    print(msg)
    return msg
def main():
    strength = 5
    wisdom = 10
    dex = 2.5
    create_stats_message(strength,wisdom,dex)
main()