def reverse_array(items):
    inverted_array = []
    for i in range(len(items), 0, -1):
        inverted_array.append(items[i-1])
    return inverted_array

def main():
    items = ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"]
    newlist = reverse_array(items)
    print(newlist)
main()