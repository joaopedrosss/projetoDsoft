class Carro():

  def __init__(self, marca, modelo, ano, alugado=False):
    self.marca = marca
    self.modelo = modelo
    self.ano = int(ano)
    self.alugado = alugado

  def show(self):
    return "{} {} {}".format(self.marca,self.modelo,self.ano)

