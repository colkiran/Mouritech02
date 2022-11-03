import sys

class Handler:

    def __init__(self, myoutput):
        self.file = myoutput

    def emit(self, message):
        self.file.write(message)
        self.file.flush()

class FilteredLogger:
    def __init__(self, pattern, handler):
        self.pattern= pattern
        self.handler = handler

    def log(self, message):
        if self.pattern in message:
            self.handler.emit(message)

class CustomHandler:

    def write(self, msg):
        print(f"This is from custom handler.....[{msg}]")

    def flush(self):
        pass


cstHandler = CustomHandler()

handler = Handler(cstHandler)
logger = FilteredLogger("Oranges", handler)

logger.log("Ignored: this will not be logged")
logger.log("Error: This is important")
logger.log("Apple: Apples from Ooty")
logger.log("Oranges: Oranges from Kanpur")
