from datetime import datetime

class Carro():

  def __init__(self, marca, modelo, ano, preco = 0,assentos = 0,alugado=False,dono=""):
    self.__marca = marca.lower()
    self.__modelo = modelo
    self.__ano = ano
    self.__preco = float(preco)
    self.__assentos = int(assentos)
    self.__alugado = alugado
    self.__dono = dono

  def mostrar(self):
    return "{} {} {}".format(self.__marca,self.__modelo,self.__ano)
  
  def getPreco(self):
    return self.__preco
  def setPreco(self,value):
    try:
      newValue = float(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue < 0):
      print("Valor inválido: precisa ser um número positivo ou nulo")
      return
    self.__preco = newValue

  def getAno(self):
    return self.__ano 
  def setAno(self,value):
    try:
      newValue = int(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue < 0 or newValue > datetime.now().year):
      print("Valor inválido: precisa ser um número positivo ou ano até o ano atual: " + str(datetime.now().year))
      return
    self.__ano = newValue
    
  def getAssentos(self):
    return self.__assentos
  def setAssentos(self,value):
    try:
      newValue = int(value)
    except (TypeError, ValueError) as erro:
      raise type(erro)("Valor inválido")
    if(newValue <= 0):
      print("Valor inválido: precisa ser um número positivo")
      return
    self.__assentos = newValue
  
  def getDono(self):
    return self.__dono
  def setDono(self,value):
    self.__dono = value

  #TODO: tratmento de execeção nessas abaixo
  def getMarca(self):
      return self.__marca 
  def setMarca(self,value):
      self.__marca = str(value).lower()

  def getModelo(self):
      return self.__modelo
  def setModelo(self,value):
      self.__modelo = str(value).lower()

  def getAlugado(self):
    return self.__alugado
  def setAlugado(self,value):
    self.__alugado = value
  
class ListaCarros():
  def __init__(self,lista=[]):
        self.__lista = lista
  
  def getCarro(self):
    return self.__lista
  
  def setCarro(self,value):
      self.__lista.append(value)
    
  def mostrar(self):
      print("""
-------- lista de carros --------
<nome> <preço do aluguel> <número de assentos> <disponibilidade>
D: DISPONÍVEL
N/A: CARRO NÃO DISPONÍVEL (incluindo quem o alugou)
--------""")
      for count,carro in enumerate(self.__lista):
        disponivel = "D" if carro.getAlugado() is False else "N/A"

        contratante = "" if carro.getAlugado() is False else carro.getDono()

        print("[{}] {} R${:.2f} {} ({}) {}".format(count+1,
                                     carro.mostrar().capitalize(),
                                     carro.getPreco(),
                                     carro.getAssentos(),
                                     disponivel,
                                     contratante))

      print("--------")
      return None

  def matchAtributes(self,atr_a,atr_b,option=1):
    #a: atributo já presente na lista
    #b: o que o usuario colocou
    
    if(option == 1): #string
      return (atr_a == atr_b) if atr_b != "" else 1

    if(option == 2): #range of values
      min_value = atr_b[0] if atr_b[0] != -1 else 0
      max_value = atr_b[1]+1 if atr_b[1] != -1 else atr_a+1

      return atr_a in range(min_value,max_value)

  def procurar(self,value):

    deuMatchCom = []
    for i,carro in enumerate(self.__lista):
      match_car = 0

      match_car += self.matchAtributes(carro,value.getMarca())
      match_car += self.matchAtributes(carro,value.getModelo())
      match_car += self.matchAtributes(carro.getPreco(),(value.preco_min,value.preco_max),2)
      match_car += self.matchAtributes(carro.getAno(),(value.ano_antigo,value.ano_atual),2)
      match_car += self.matchAtributes(carro.getAssentos(),(0,value.getAssentos),2)
      
      #print(match_car)
      if(match_car == 5):
        deuMatchCom.append(carro)

    return deuMatchCom




  