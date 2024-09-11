def join_strings(strings):
    new_string = ""
    for s in strings:
        new_string += f"{s},"

    new_string = new_string[:-1]
    return  new_string

def main():
    strings = ["this", "list", "is", "so", "important"]
    result = join_strings(strings)
    print(result)

if __name__ == '__main__':
    main()