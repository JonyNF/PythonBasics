def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False),
    ]

    return heroes

def get_first_item(items):
    if not items:
        return "ERROR"
    else: return items[0]


def test():
    heroes = get_heroes()
    for hero in heroes:
        print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")


def main():
    test()
    items = []
    print(get_first_item(items))

main()
