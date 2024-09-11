import math


def factorial(num):
    factorial_num = 1
    if num == 0:
        return 1
    else:
        for i in range (1, num+1):
            factorial_num = factorial_num * i
    return factorial_num

# def factorial(num):
#     return math.factorial(num)

def main():

    result = factorial(4)
    print(result)
if __name__ == '__main__':
    main()