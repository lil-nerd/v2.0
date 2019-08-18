def to_data(message):
    return bytes(str(message), encoding = 'utf-8')

def get_data(message):
    return message.decode('utf-8')

def print_clients(addr, nicks):
    print("List of clients of server: ")
    print()
    for i in range(len(addr)):
        print("    Nickname = " + str(nicks[i]))
        print("        Address = " + str(addr[i]))
        print()
