def countdown_to_start():
    i = 10
    while i > 0:
        if i == 1:
            print(f"{i}...Fight!")
        else:print(f"{i}...")
        i -= 1


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
