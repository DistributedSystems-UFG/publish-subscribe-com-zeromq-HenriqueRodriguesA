import zmq, time
import random
from constPS import * #-

def Jogar_Dado():
	resultado = random.radint(1, 6)
	if resultado == 1
		msg = "1"
	elif resultado == 2
		msg ="2"
	elif resultado == 3
		msg ="3"
	elif resultado == 4
		msg ="4"
	elif resultado == 5
		msg ="5"
	elif resultado == 6
		msg ="6"
	else:
		msg = "erro!"

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("JOGAR DADO " + Jogar_dado())
	s.send(msg) # publish the current time
