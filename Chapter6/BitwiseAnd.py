def get_create_bits(user_permissions):
    can_create_guild = 0b1000
    return can_create_guild & user_permissions


def get_review_bits(user_permissions):
    can_review_guild = 0b0100
    return  can_review_guild & user_permissions


def get_delete_bits(user_permissions):
    can_delete_guild = 0b0010
    return can_delete_guild & user_permissions


def get_edit_bits(user_permissions):
    can_edit_guild = 0b0001
    return can_edit_guild & user_permissions

def main():
    user1= 0b0111

    if get_create_bits(user1):
        print("True")
    else: print("False")
    
    print(get_review_bits(user1))
    get_delete_bits(user1)
    get_edit_bits(user1)

    print(user1)

main()