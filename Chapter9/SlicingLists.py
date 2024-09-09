def get_champion_slices(champions):
    champion_list1 = champions[2:]
    print("==============================")
    print("From 3rd champion to the end:", champion_list1)

    champion_list2 = champions[:-3]
    print("==============================")
    print("From start to 3rd champion from end:", champion_list2)

    champion_list3 = champions[::2]
    print("==============================")
    print("Even-indexed champions:", champion_list3)
    return  champion_list1, champion_list2, champion_list3

def main():
    champions = ["Thrundar",
                 "Morgate",
                 "Gandolfo",
                 "Thraine",
                 "Norwad",
                 "Gilforn"]

    get_champion_slices(champions)
main()