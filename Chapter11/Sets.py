def remove_duplicates(spells):
    non_duplicate_spells = set()

    for spell in spells:
        #set values are unique so adding spells to a set will remove duplicates
        non_duplicate_spells.add(spell)

    #to remove a value in a set user remove() function
    non_duplicate_spells.remove("fireball")
    return non_duplicate_spells

def main():

    spells =  [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ]

    singular_spells = remove_duplicates(spells)
    print(singular_spells)
main()