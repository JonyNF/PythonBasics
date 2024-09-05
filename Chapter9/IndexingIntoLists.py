def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1
    return inventory[item_index]

def main():
    result = get_leather_scraps()
    print(result)

main()