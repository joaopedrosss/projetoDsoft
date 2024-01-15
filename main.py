from Carro import Carro,ListaCarros
from Menu import Menu

# INSTANCIE OBJETOS

lista_de_carros = ListaCarros()
menu_de_opcoes = Menu() 

# PEGUE OS CARROS NO ARQUIVO

carrosFile = open("carro-data.txt","rt")
for line in carrosFile:
  dados = line.split()
  #xprint(dados)

  alugado = True if dados[5] == "True" else False
  dono = dados[len(dados)-1] if len(dados) == 7 else ""
  ano = int(dados[2])
  marca = dados[0]
  modelo = dados[1]
  preco = dados[3]
  assentos = dados[4]

  carro = Carro(marca,modelo,ano,preco,assentos,alugado,dono)

  lista_de_carros.setCarro(carro)
carrosFile.close()

# INTERFACE 

# _ SEM LOGIN

while True:
  menu_de_opcoes.mostrar()
  
  action = input(">")
  try:
    action = int(action)  
  except:
    print("Valor inválido. Digite novamente")
  match action:
    case 0:
      break

    case 1:
      lista_de_carros.mostrar()
    
    case 2:
      carro_procurado = lista_de_carros.criarCarroParaPesquisa()
      
      if(carro_procurado != None):
        carros_encontrados = lista_de_carros.procurar(carro_procurado)
        print(" ----------- ")
        print("Carros econtrados:")

        if(carros_encontrados == []):
          print("Nenhum carro encontrado com tais parametros!")
        else:
          for carro in carros_encontrados:
            dispo = "DISPONIVEL" if carro.getAlugado() is False else "NÃO DISPONIVEL"

            print("{} R$ {:.2f} {}".format(carro.mostrar().capitalize(),carro.getPreco(),dispo))
        print(" ----------- ")

      pass
    
    case _:
      print("Ação invalida")
  
  menu_de_opcoes.limparTela()
# _ COM LOGIN DE USUÁRIO

# _ COM LOGIN DE ADMIN