from Carro import Carro,ListaCarros


lista_carros = ListaCarros()

# PEGUE OS CARROS NO ARQUIVO

carrosFile = open("carro-data.txt","rt")
for line in carrosFile:
  dados = line.split()
  #xprint(dados)

  alugado = True if dados[5] == "True" else False
  dono = dados[len(dados)-1] if len(dados) == 7 else ""
  ano = dados[2]
  marca = dados[0]
  modelo = dados[1]
  preco = dados[3]
  assentos = dados[4]

  carro = Carro(marca,modelo,ano,preco,assentos,alugado,dono)

  lista_carros.setCarro(carro)
carrosFile.close()


lista_carros.mostrar()

carro = Carro()