
import socket
import threading

from help import *
from srvr_help import *



class Server():



    def __init__(self):

            host = "127.0.0.1"
            port_chat = 8521
            port_video = 8523

            self.server_chat = (host, port_chat)
            self.server_video = (host, port_video)

            self.clients = []

            self.serv_sock_chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0)
            self.serv_sock_video = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0)

            self.serv_sock_chat.bind(self.server_chat)
            self.serv_sock_video.bind(self.server_video)

            self.serv_sock_chat.listen(10)
            self.serv_sock_video.listen(10)


            print("***Server is started!")




    def conn_handler(self, client, address):
        while True:
            data = client.recv(1024)
            for connection in self.clients:
                    connection.send(data)
            if not data:
                break



    def run_Server(self):

            while True:

                client_sock_chat, client_addr_chat = self.serv_sock_chat.accept()
#                client_sock_video, client_addr_video = self.serv_sock_video.accept()
                self.clients.append(client_sock_chat)

                while True:
                    data = client_sock_chat.recv(1024)
                    client_sock_chat.send(to_data("  *\|/*  You've entered chAt!  *\|/*  "))
                    new_name = "\n" + "  *\|/*  " + get_data(data) + " connected!" + "  *\|/*  "

                    for connections in self.clients:
                        connections.send(to_data(new_name))

                    if data:
                        print(get_data(data) + " connected")
                        break


                #THREADS
                conn_Thread = threading.Thread(target = self.conn_handler, args = (client_sock_chat, client_addr_chat))
                conn_Thread.deamon = True
                conn_Thread.start()
