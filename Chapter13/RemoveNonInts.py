def remove_nonints(nums):
    int_nums = []
    for n in nums:
        if type(n) == int:
            int_nums.append(n)
    print(int_nums)
    return int_nums

def main():

    remove_nonints(['1', 1, '3', '400', 4, 500])
    # Remaining list after removing nonints = [1, 4, 500]
main()