def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, len(num)):
        if num[i] % 2 != 0:
            odd_numbers.append(num[i])

    print(odd_numbers)
    return odd_numbers

def main():

    get_odd_numbers([1, 2, 3, 4, 5, 6, 7])

main()