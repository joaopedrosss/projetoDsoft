from Carro import Carro



def menuOfOptions():
    print("----- RENTAL CAR - Aluguel de Carros -----")
    print("(0) SAIR")
    print("(1) Cadastrar carro")
    print("(2) Listar carros")
    print("(3) Alugar ou devolver carro")
    print("O que deseja fazer?")

"""
 #1. Cadastrar carro
 O usuário consegue cadastrar um carro no sistema passado seus atributos.
"""
def createCar(marca, modelo,ano):
    carro = Carro(marca,modelo,ano)

    return carro

"""
 #2. Ver carros
 O usuário consegue visualizar quais carros estão disponíveis ou não
"""
def listarCarros(array):
  print("-------- lista de carros -------- ")
  print("D: DISPONÍVEL")
  print("N/A: CARRO NÃO DISPONÍVEL")
  print("--------")


  for i in range(0,len(array)):
    disponivel = "D" if array[i].alugado is False else "N/A"
    
    print("[{}] {} ({})".format(i+1,array[i].show(),disponivel))

  print("--------")


"""
  #3. Alugar carro
  O usuário pode alugar um carro mudando o status 'alugado' do objeto da classe Carro para True
"""

"""

  #4 Devolver carro

  O usuário pode devolver um carro mudando o status 'alugado' do objeto da classe Carro para False


  <case 3>
"""



carros_cadastrados = []

carros_cadastrados.append(createCar("Fiat","Uno",2010))
carros_cadastrados.append(createCar("Pegout","Boxer Furgão",2001))
carros_cadastrados.append(createCar("McLaren","Artura",2012))
carros_cadastrados.append(createCar("Ferrari","288 GTO ",1984))




while True:
  menuOfOptions()
  action = int(input(">"))
  
  match action:
    case 0:
      break
      
    case 1:
      print("Insira:")
      marca = input("marca:").lower()
      modelo = input("modelo:").lower()
      ano = int(input("ano:"))
      carros_cadastrados.append(createCar(marca,modelo,ano))
      
    case 2:
      listarCarros(carros_cadastrados)
  
    case 3:

      subAction = int(input("Deseja alugar ou devolver um carro?\n[1] alugar\n[2] devolver\n>"))

      listarCarros(carros_cadastrados)
      
      match subAction:
      
        case 1:
          idx = int(input("Digite o indice do carro que deseja alugar\n>"))
          
          if idx <= 0 or idx > len(carros_cadastrados):
            print("CARRO NÃO ENCONTRADO")
          elif carros_cadastrados[idx-1].alugado is True:
            print("CARRO NÃO DISPONIVEL")
          else:
            carros_cadastrados[idx-1].alugado = True
            print("CARRO ALUGADO COM SUCESSO!")

        case 2:

          idx = int(input("Digite o indice do carro que deseja devolver\n>"))

          if idx <= 0 or idx > len(carros_cadastrados):
            print("CARRO NÃO ENCONTRADO")
          elif carros_cadastrados[idx-1].alugado is False:
            print("CARRO NÃO ALUGADO")
          else:
            carros_cadastrados[idx-1].alugado = False
            print("CARRO DEVOLVIDO")

        case _:
          print("ACAO INVALIDA")
          break
    

    
    case _:
      break

  