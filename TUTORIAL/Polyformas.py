
class CarroEletrico:
    def __init__(self,carga=0):
        self.__carga = carga
        self.__velo = 0

    def getCarga(self):
        return self.__carga
    
    def getVelo(self):
        return self.__velo

    def acelerar(self):
        if(self.getCarga() <= 0):
            return "Sem carga! Não posso acelerar."
            
        self.__carga -= 1
        self.__velo += 1
        return 1

class CarroCombus:
    def __init__(self,gas=0):
        self.__gas = gas
        self.__velo = 0

    def getGas(self):
        return self.__gas
    
    def getVelo(self):
        return self.__velo

    def acelerar(self):
        if(self.getGas() <= 0):
            return "Sem combustível! Não posso acelerar."
        self.__gas -= 2
        self.__velo = self.getVelo() + 3

        return 1

class CarroHibrido:
    def __init__(self,gas=0,carga = 0):
        self.__gas = gas
        self.__carga = carga
        self.__velo = 0

    def getGas(self):
        return self.__gas
    
    def getCarga(self):
        return self.__carga
    
    def getVelo(self):
        return self.__velo

    def acelerar(self):
        
        if(self.getGas() <= 0):
            if(self.getCarga() <=0):
                return "Sem carga ou combustível. Não posso acelerar"
            self.__carga -= 1
            self.__velo += 1
            return 1
        
        self.__gas -= 2
        self.__velo += 2
        return 1

       
def velocimetro(carro):
    return "v: {} km/h".format(carro.getVelo())

ultra = CarroEletrico(5)
chev = CarroCombus(10)
victra = CarroHibrido(8,4)

tempo = 8
while(tempo >= 0):
    

    print("ULTRA: {} {}".format(ultra.acelerar(),velocimetro(ultra)))
    print("CHEV: {} v: {} km/h".format(chev.acelerar(),chev.getVelo()))
    print("VICTRA:{} {}".format(victra.acelerar(),velocimetro(victra)))
    print("----------")
    tempo -= 1







    

    