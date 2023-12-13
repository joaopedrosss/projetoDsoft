class Carro():

  def __init__(self, marca, modelo, ano, preco = 0,lugares = 0,alugado=False):
    self.marca = marca.lower()
    self.modelo = modelo
    self.ano = int(ano)
    self.preco = float(preco)
    self.lugares = int(lugares)
    self.alugado = alugado



  def show(self):
    return "{} {} {}".format(self.marca,self.modelo,self.ano)

