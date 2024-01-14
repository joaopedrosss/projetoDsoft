class Interruptor:
    def __init__(self):
        self.isOn = False
    
    def ligar(self):
        self.isOn = True
    
    def desligar(self):
        self.isOn = False
    
    def show(self):
        print(self.isOn)

switch = Interruptor()

switch.show()
switch.ligar()
switch.show()
switch.desligar()
switch.show()