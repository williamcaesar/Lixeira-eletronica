class Stub:
    def __init__(self):
        self.BCM = True
        self.OUT = True

    def PWM(self, *arg, **argv):
        return True
        
    def setup(self, *arg, **argv):
        return True

    def setmode(self, *arg):
        return True

GPIO = Stub()
