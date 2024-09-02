def calculate_guild_perms(user1, user2, user3, user4):
    overall_perms = user1 | user2 | user3 | user4
    return overall_perms

def main():
    glorfindel = 0b1000
    galadriel = 0b0100
    elendil = 0b0010
    elrond = 0b0001
    can_invite = 0b1000
    can_kick = 0b0100
    can_enter_dungeon = 0b0010
    can_surrender = 0b0001
    print( calculate_guild_perms(glorfindel, galadriel, elendil, elrond))
    if calculate_guild_perms(glorfindel, galadriel, elendil, elrond) & can_invite:
        print("The guild can invite players")

main()