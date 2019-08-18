import socket
import threading
import cv2 as cv

from help import *
from face import Chat_window

class Client():

	client_sock_chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	name = "default"



	def send_msg(self, msg):
		print(msg)
		self.client_sock_chat.send(to_data(msg))
		print("***msg sent")


	def __init__(self):

		print("Client is working!!!")

		host = "127.0.0.1"
		port_chat = 8521
		port_video = 8523
		self.server_chat = (host, port_chat)
		self.server_video = (host, port_video)


		self.client_sock_chat.connect(self.server_chat)
		print("You have been connected to " + str(host))

		self.name = input("Enter your nickname: ")
		self.client_sock_chat.send(to_data(self.name))
		self.window = Chat_window(self)
