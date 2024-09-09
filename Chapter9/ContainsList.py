def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]
    return weapon in top_weapons

    # don't touch above this line

    pass

def main():
    print(is_top_weapon("sword of justice"))

main()