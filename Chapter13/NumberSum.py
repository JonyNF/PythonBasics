def number_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def main():

    print(number_sum(18)) #Expected: 171

if __name__ == '__main__':
    main()