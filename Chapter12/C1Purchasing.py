def purchase_item(price, gold_available):

        if gold_available >= price:
            print("Item purchased!")
            return gold_available - price
        else:
            raise Exception("not enough gold")


def main():
    try:
        gold_remaining = purchase_item(70, 75)
        print(gold_remaining)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()