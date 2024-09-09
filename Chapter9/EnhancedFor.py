
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if "Potion" in items[i] :
            potion_count+=1
        elif "Shortsword" in items[i]:
            shortsword_count+=1
        elif "Bread" in items[i]:
            bread_count+=1

    print(f"Potion Count {potion_count} / Shortsword Count {shortsword_count} / Bread count {bread_count}")
    # don't touch below this line
    return potion_count, bread_count, shortsword_count

def contains_leather_scraps(items):
    found = False

    for item in items:
        if "Leather Scraps" in item:
            print("Leather Scraps found!!")
            found= True

    return found

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if new_character_levels[i] > old_character_levels[i]:
            print(i)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    print(max_so_far)
    return max_so_far


def main():
    items = [
        "Potion",
        "Potion",
        "Potion",
        "Shortsword",
        "Shortsword",
        "Bread",
        "Leather Scraps"
    ]
    get_item_counts(items)
    contains_leather_scraps(items)
    test()
    find_max([1, 2, 300, 4, 5])

main()