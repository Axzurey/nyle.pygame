import uuid

from classes.sharedUtil import createThread

class connection:
    callback: function;
    idowner: str;
    connected: bool
    def __init__(self, idowner: str, callback: function):
        self.callback = callback
        self.idowner = idowner
        self.connected = True

    def disconnect(self):
        self.connected = False

class phxSignal:

    def __init__(self):
        self.connections: list[connection] = []
        self.mid = str(uuid.uuid4())

    def connect(self, callback: function):
        conn = connection(self.mid, callback)
        self.connections.append(conn)
        return conn

    def emit(self):
        for conn in self.connections:
            if self.mid != conn.idowner: continue
            if conn.connected:
                createThread(conn.callback)
            else:
                self.connections.remove(conn)