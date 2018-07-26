import threading
from Server.host import Host
class ServerEngine:
    def __init__(self, window):
        self.window = window

        self.messages = []
        self.host = Host()

        self.hostThread = threading.Thread(target=self.host.accept, daemon=True) #daemon is True so the thread closes with the window
        self.hostThread.start()

    def runGame(self):
        self.updateMessages()


    def updateMessages(self):
        received = self.host.getDecoded()
        if len(received) > len(self.messages):
            for i in range(len(self.messages), len(received)): #adds any messages not in self.messageBox to self.messages
                self.messages.append(received[i])