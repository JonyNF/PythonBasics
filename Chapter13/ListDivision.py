def divide_list(nums, divisor):
    divided_list = []
    for n in nums:
        divided_list.append(n / divisor)
    return divided_list

# def divide_list(nums, divisor):
#     divided_list = [n / divisor for n in nums]  # Using list comprehension for conciseness
#     return divided_list

def main():

    result = divide_list([6, 8, 10], 2)
    print(result)
main()