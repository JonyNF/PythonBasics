def get_character_record(name, server, level, rank):
    character_record = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
    return character_record

def main():
    run_case1 = ("bloodwarrior123",
        "server1",
        5,
        1)

    character = get_character_record(run_case1[0], run_case1[1], run_case1[2], run_case1[3])
    print(character)

    #To access dictionary values we specify corresponding key in square brackets:
    print(character["id"]) #prints ID:bloodwarrior123#server1


main()