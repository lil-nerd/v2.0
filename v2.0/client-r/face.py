#!/usr/bin/python3
import threading
import tkinter as tk

from help import *

class Chat_window():



    def __init__(self, client):

        self.client = client

        window = tk.Tk()
        window.title("Chat#~" + str(client.name))
        window.geometry("500x500")

        self.chat = tk.Text(window)
        self.chat.pack()

        message_box = tk.Entry(window, width = 50)
        message_box.pack(side= 'left')

        cl_thread = threading.Thread(target = self.get_msg)
        cl_thread.deamon = True
        cl_thread.start()

        #send message
        def rvl_msg():
            msg = message_box.get()
            client.send_msg(str(client.name)+ ": " + msg)
            message_box.delete(0, 'end')

        send_btn = tk.Button(window, text = "Send", command = rvl_msg)
        send_btn.pack(side= 'right')

        window.mainloop()


    def get_msg(self):
        while True:
            data = self.client.client_sock_chat.recv(1024)
            if not data:
                print("bye")
                break
            self.show_new_msg(data)


    def show_new_msg(self, data):
        print("show")
        self.chat.insert('end', get_data(data))
        self.chat.insert('end', '\n')
