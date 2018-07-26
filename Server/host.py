__author__ = 'Norman Delorey'
__version__ = '0.2'
"""
    This contains two classes (User and Host) to send and receive text messages.
"""
import socket
import pickle
from Server.packet import Packet
class Host:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname()) #gets host machine
        self.port = 10004
        self.hostName = socket.gethostname()
        self.decoded = ["None"]
        self.users = [] #the de-serialized messges
        self.userName = "server"
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket object
        self.s.bind(('', self.port))

        self.packet = Packet()

    def connect(self):
        """
        Initially connects to the hostname
        :return: none
        """
        self.s.connect((self.host, self.port))
        self.s.send(b'')
        self.s.close()

    def sendMessage(self, message):
        """
            Sends messages to everyone on the server
        :param message: the message to send
        :return:
        """
        for i in self.users: #loops through every connected user
            self.s = socket.create_connection((i[0], self.port)) #connects to the user
            info = [socket.gethostname(), self.port, self.userName, message]
            if len(self.decoded) > 0 and self.decoded[-1] != info[2] + ": " + info[3]:
                self.decoded.append(info[2] + ": " + info[3]) #adds the message to the host's list
            elif len(self.decoded) == 0:
                self.decoded.append(info[2] + ": " + info[3]) #adds the message to the host's list
            data = pickle.dumps(info) #serializes the message
            self.s.send(data) #sends the message
            self.s.close()

    def setPort(self, newPort):
        """
            Sets the port number
        :param newPort: the new port number
        :return: none
        """
        self.port = newPort

    def getPort(self):
        """
        :return: the port number (self.port)
        """
        return self.port

    def getName(self):
        """
        :return: the user's name (self.userName)
        """
        return self.userName

    def getDecoded(self):
        """
        :return: returns the de-serialized messages (self.decoded)
        """
        return self.decoded

    def accept(self):
        """
        Accepts messages from clients
        :return: none
        """
        self.s.listen(5)                 # Now wait for client connection.

        try:
            while True:
                c, addr = self.s.accept()     # Establish connection with client.
                recievedData = c.recv(4096) #receives data

                try:
                    if addr not in self.users:
                         self.users.append(addr) #adds any new users to the user list
                         self.decoded.append("Received connection from: " + str(addr[0])) #informs the host that there is a new user
                    message = pickle.loads(recievedData) #de-serializes the message
                    hostName = message[0]
                    port = message[1]
                    userName = message[2]
                    packet = message[3]
                    decodedMessage = str(hostName) + " " + str(port) + " " + str(userName) + " " + packet.word + " " +str(len(self.decoded) + 1)
                    self.decoded.append(decodedMessage)

                    c.close()                # Close the connection
                except EOFError:
                    pass
        except OSError:
            pass





