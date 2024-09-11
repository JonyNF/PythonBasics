def main():
    #try block executes until exceptions is raised or code is successfully executed
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    #If exception is raised we handle it
    except Exception as e:
        print(e)


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    #Raising our own exception to tell user that his action is against the intended use
    raise Exception("player id not found")


main()
