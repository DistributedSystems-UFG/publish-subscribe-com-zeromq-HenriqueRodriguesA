import zmq
from constPS import * #-

context = zmq.Context()
s1 = context.socket(zmq.SUB)          # create a subscriber socket
p1 = "tcp://"+ HOST1 +":"+ PORT        # how and where to communicate
s1.connect(p1)                         # connect to the server
s1.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

context = zmq.Context()
s2 = context.socket(zmq.SUB)          # create a subscriber socket
p2 = "tcp://"+ HOST2 +":"+ PORT        # how and where to communicate
s2.connect(p2)                         # connect to the server
s2.setsockopt_string(zmq.SUBSCRIBE, "JOGAR DADO")  # subscribe to JOGAR DADO messages

for i in range(5):  # Five iterations
	resp1 = s1.recv()   # receive a message
	print (bytes.decode(resp1))
	resp2 = s2.recv()   # receive a message
	print (bytes.decode(resp2))