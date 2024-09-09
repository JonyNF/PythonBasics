def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favorite_list = favorite_weapons + favorite_armor + favorite_items
    return favorite_list

def main():
    favorite_weapons= ["sword", "dagger"]
    favorite_armor = ["bracers", "helmet"]
    favorite_items = ["feather", "iron bars"]
    print(concatenate_favorites(favorite_weapons, favorite_armor, favorite_items))
main()