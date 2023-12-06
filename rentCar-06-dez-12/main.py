from Carro import Carro
from os import system,name



def menuOfOptions():
    print("----- RENTAL CAR - Aluguel de Carros -----")
    print("(0) SAIR")
    print("(1) Cadastrar carro")
    print("(2) Listar carros")
    print("(3) Alugar ou devolver carro")
    print("(4) Pesquisar carro")
    print("(5) Remover carro")
    print("(6) Editar carro")
    print("O que deseja fazer?")


def limpar_tela():
  if(name == "nt"): #windows
      system("cls")
  else:
    system("clear")

def simOUnao(acao):
  
  while(True):
    confirm = input("Deseja {}? (s/n): ".format(acao)).lower()

    if(confirm[0] == "s" or confirm[0] == "n"):
      break
    else:
      print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
          
  
  return (confirm[0] == "s")
  

"""
 #1. Cadastrar carro
 O usuário consegue cadastrar um carro no sistema passado seus atributos.
"""
def createCar(marca, modelo,ano):
    carro = Carro(marca.lower(),modelo.lower(),ano)

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
    
    print("[{}] {} ({})".format(i+1,array[i].show().capitalize(),disponivel))

  print("--------")

def searchCar(array,carro):
  #retorna uma lista com examtente aquele carro encontrado
  for i in range(0,len(array)):
    match_car = 0
    match_car += array[i].marca == carro.marca
    match_car += array[i].modelo == carro.modelo
    match_car += array[i].ano == carro.ano

    if(match_car == 3):
      return [array[i]]
  return []
  

def searchCarList(array,carro):
  #vai me retornar uma lista com os carros encontrados que deram match com os paramentros dados
  
  deuMatchCom = []
  for i in range(0,len(array)):
    match_car = 0
    match_car += array[i].marca == carro.marca if carro.marca != "" else 1
    match_car += array[i].modelo == carro.modelo if carro.modelo != "" else 1
    match_car += array[i].ano == carro.ano if carro.ano != -1 else 1

    if(match_car == 3):
      deuMatchCom.append(array[i])
      
  return deuMatchCom

  
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

carros_cadastrados.append(createCar("ford","car",2010))
carros_cadastrados.append(createCar("fiat","uno",2010))
carros_cadastrados.append(createCar("pegout","boxer furgão",2001))
carros_cadastrados.append(createCar("mcLaren","artura",2012))
carros_cadastrados.append(createCar("ferrari","288 gto",1984))
carros_cadastrados.append(createCar("honda","civic",2010))
carros_cadastrados.append(createCar("honda","velozte",2005))
carros_cadastrados.append(createCar("lamborguini","aventador",2012))
carros_cadastrados.append(createCar("lamborguini","forza",2012))




while True:
  menuOfOptions()
  action = int(input(">"))
  
  match action:
    case 0:
      break
      
    case 1:
      print("Insira:")
      marca = input("marca:")
      modelo = input("modelo:")
      ano = int(input("ano:"))
      
      confirm = simOUnao("cadastrar carro '{} {} {}'".format(marca,modelo,ano)) 

      if(confirm is True):
        carros_cadastrados.append(createCar(marca,modelo,ano))
        print("Carro cadastrado com sucesso!")
      else:
        print("Cadastro cancelado!")  
      
    case 2:
      listarCarros(carros_cadastrados)
  
    case 3:

      while(True):

        subAction = int(input("Deseja alugar ou devolver um carro?\n[1] alugar\n[2] devolver\n>"))
  
        match subAction:
        
          case 1:
            listarCarros(carros_cadastrados)
            idx = int(input("Digite o indice do carro que deseja alugar\n>"))
            
            if idx <= 0 or idx > len(carros_cadastrados):
              print("CARRO NÃO ENCONTRADO")
            elif carros_cadastrados[idx-1].alugado is True:
              print("CARRO NÃO DISPONIVEL")
            else:
              #nome_carro = carros_cadastrados[idx-1].show()
  
              confirm = simOUnao("alugar carro {}".format(carros_cadastrados[idx-1].show().capitalize()))
  
              if(confirm is True):
                carros_cadastrados[idx-1].alugado = True
                print("CARRO ALUGADO COM SUCESSO!")
              else:
                print("AÇÃO CANCELADA!")
  
          case 2:
            listarCarros(carros_cadastrados)
            idx = int(input("Digite o indice do carro que deseja devolver\n>"))
  
            if idx <= 0 or idx > len(carros_cadastrados):
              print("CARRO NÃO ENCONTRADO")
            elif carros_cadastrados[idx-1].alugado is False:
              print("CARRO NÃO ALUGADO")
            else:
              confirm = simOUnao("devolver carro {}".format(carros_cadastrados[idx-1].show().capitalize()))
  
              if(confirm is True):
                carros_cadastrados[idx-1].alugado = True
                print("CARRO DEVOLVIDO COM SUCESSO!")
              else:
                print("AÇÃO CANCELADA!")
              carros_cadastrados[idx-1].alugado = False
              print("CARRO DEVOLVIDO")
  
          case _:
            print("ACAO INVALIDA")

        mais_alguma_coisa = simOUnao("alugar ou devolver mais carros") 

        if(mais_alguma_coisa is True):
          continue
        else:
          break

    case 4:
      print("---- Pesquisa de Carro ---- ")
      print("Preencha os campos abaixo para realizar a pesquisa")
      print("Caso queira deixar campo vazio, aperte 'ENTER'")
      print("----------------------------")
      print("Insira:")
      marca = input("marca:").lower()
      modelo = input("modelo:").lower()
      ano = input("ano:")

      ano = int(ano) if ano != "" else -1
      
      search_car = createCar(marca,modelo,ano)
      

      carros_encontrados = searchCarList(carros_cadastrados,search_car)
      if(carros_encontrados != []):
        print("Carros Encontrados:")
        for carro in carros_encontrados:
          print(carro.show().capitalize())
      else:
        print("Nenhum carro encontrado com tais parametros.")

    case 5:
      print("---- Remoção de Carro ---- ")
      print("Digite os dados do carro que deseja remover")
      print("Insira:")
      marca = input("marca:").lower()
      modelo = input("modelo:").lower()
      ano = input("ano:")

      procurarPor = createCar(marca,modelo,ano)
      
      carro_encontrado = searchCar(carros_cadastrados,procurarPor)
      if(carro_encontrado != []):
        print("Carro encontrado!")
        confirm = simOUnao("remover carro '{}'".format(carro_encontrado[0].show().capitalize()))

        if(confirm is True):
          carros_cadastrados.remove(carro_encontrado[0])
      else:
        print("Carro não encontrado.")
        
    case 6:
      print("---- Editar dados de carro ----")
      listarCarros(carros_cadastrados)
      idx = int(input("Digite o indice do carro que deseja editar\n>"))

      if idx <= 0 or idx > len(carros_cadastrados):
        print("CARRO NÃO ENCONTRADO")
      elif carros_cadastrados[idx-1].alugado is True:
        print("Carro já está alugado.\nNão é possível editar dados.")
      else:
        idx -= 1 
        confirmar = simOUnao("editar dados do carro '{}'".format(carros_cadastrados[idx].show()))

        if(confirmar is True):
          print("Insira os novos dados")
          print("Caso não queira fazer modificações, aperter ENTER no campo selecionado")
          new_marca = input("marca:").lower()
          new_modelo = input("modelo:").lower()
          new_ano = input("ano:")

          carros_cadastrados[idx].marca = carros_cadastrados[idx].marca if new_marca == "" else new_marca
          carros_cadastrados[idx].modelo = carros_cadastrados[idx].modelo if new_modelo == "" else new_modelo
          carros_cadastrados[idx].ano = carros_cadastrados[idx].ano if new_ano == "" else new_ano
          print("DADOS EDITADOS COM SUCESSO!")
          
        else:
          print("AÇÃO CANCELADA!")        

  
      
      
      
    case _:
      print("AÇÃO INVÁLIDA")

  voltar_ao_menu = input("<Aperte qualquer botão para voltar ao menu principal>")
  limpar_tela()
  

  