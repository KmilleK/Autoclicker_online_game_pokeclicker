# message_bus.py
import threading

class MessageBus:
    def __init__(self):
        self.subscribers = {}
        self.exit_event = threading.Event()
        self.isRunning=False

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def publish(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)
    
    def set_isRunning(self):
        self.isRunning=True
    
    def unset_isRunning(self):
        self.isRunning=False
                
    def set_exit_event(self):
        self.exit_event.set()


