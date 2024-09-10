
def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    for number in numbers:
        if number % 2 != 0:
            num_odds+=1
        else:
            num_evens+=1
    return num_odds, num_evens

def main():
    numbers = [0, 99, 2, 33, 61, 44, 9, 10, 12, 240, 35, 9082, 1234] #Expected [5 odd numbers, 8 even numbers]
    odd_numbers, even_numbers = get_odds_and_evens(numbers)
    print(odd_numbers)
    print(even_numbers)

main()