import socket
import threading
import cv2 as cv

from help import *
from face import Chat_window

class Client():

	client_sock_chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_sock_video = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	camera = cv.VideoCapture(0)
	name = "default"



	def send_msg(self, msg):
		print(msg)
		self.client_sock_chat.send(to_data(msg))
		print("***msg sent")



	def get_video(self):

		while True:
			ret, frame = self.camera.read()
			cv.imshow("camera", frame)

			k = cv.waitKey(30) & 0xff
			if k == 27:
				break

		camera.release()
		cv.destroyAllWindows()



	def __init__(self):

		print("Client is working!!!")


		cl_thread = threading.Thread(target = self.get_video)
		cl_thread.deamon = True
		cl_thread.start()


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
