def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers_int = int(num_servers, 2)
    num_players_int = int(num_players, 2)
    num_admins_int = int(num_admins, 2)
    return num_servers_int, num_players_int, num_admins_int

def main():

    data_a, data_b, data_c = binary_string_to_int("1010", "10100", "11010")
    print(data_a, data_b, data_c)

main()





















