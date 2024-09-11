def remove_duplicates(lst):
    singular_collectible = set(lst) #converting list to set trough function makes it way easier
    return singular_collectible

def main():
    lst = [
            "Frostmourne",
            "Abyssal Whip",
            "Staff of Armadyl",
            "Frostmourne",
            "Abyssal Whip",
        ]
    collectibles = remove_duplicates(lst)
    print(collectibles)
main()