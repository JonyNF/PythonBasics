def find_min(nums):
    if not nums:
        return "List is empty"
    min_value = float("inf")

    for n in nums:
        if n < min_value:
            min_value = n
    return min_value

def main():
    nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    print(find_min(nums))
main()