from help import *


def say_hello(client_sock):

    hello = "Hello, my name is GORYNsrvr! What is your name?"
    client_sock.send(to_data(hello))

    data = client_sock.recv(1024)
    data = get_data(data)

    hello = "Nice to meet you, " + data
    client_sock.send(to_data(hello))

    return data
