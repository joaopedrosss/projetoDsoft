class Carro():

  def __init__(self, marca = 'ford', modelo = 'kar', ano = 0, preco = 0,lugares = 0,alugado=False,dono=""):
    self.marca = marca.lower()
    self.modelo = modelo
    self.ano = ano
    self.preco = float(preco)
    self.lugares = int(lugares)
    self.alugado = alugado
    self.dono = dono



  def show(self):
    return "{} {} {}".format(self.marca,self.modelo,self.ano)