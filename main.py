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

    if confirm == "":
      print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
    elif(confirm[0] == "s" or confirm[0] == "n"):
      break
    else:
      print("Ação inválida\nInsira 'S' para confirma ou 'N' para cancelar")
          
  
  return (confirm[0] == "s")
  

"""
 #1. Cadastrar carro
 O usuário consegue cadastrar um carro no sistema passado seus atributos.
"""
def createCar(marca, modelo,ano,preco,assentos):
    carro = Carro(marca.lower(),modelo.lower(),ano,preco,assentos)

    return carro

"""
 #2. Ver carros
 O usuário consegue visualizar quais carros estão disponíveis ou não
"""
def listarCarros(array):
  print("-------- lista de carros -------- ")
  print("<nome> <disponibilidade> <preço do aluguel> <número de assentos>")
  print("D: DISPONÍVEL")
  print("N/A: CARRO NÃO DISPONÍVEL")
  print("--------")


  for i in range(0,len(array)):
    disponivel = "D" if array[i].alugado is False else "N/A"
    
    print("[{}] {} ({}) R${:.2f} {}".format(i+1,array[i].show().capitalize(),disponivel,array[i].preco,array[i].lugares))

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
  
#searchCarList(carros_cadastrados,search_car,preco_min,preco_max,assentos,ano_antigo,ano_atual)
def searchCarList(array,carro,preco_min,preco_max,assentos,ano_antigo,ano_atual):
  #vai me retornar uma lista com os carros encontrados que deram match com os paramentros dados
  
  deuMatchCom = []
  for i in range(0,len(array)):
    match_car = 0
    match_car += (array[i].marca == carro.marca) if carro.marca != "" else 1
    match_car += (array[i].modelo == carro.modelo) if carro.modelo != "" else 1

    match_car += (array[i].preco >= preco_min)if preco_min != -1 else 1
    
    match_car += (array[i].preco <= preco_max)if preco_max != -1 else 1

    match_car += (array[i].lugares <= assentos)if assentos != -1 else 1

    match_car += (array[i].ano >= ano_antigo)if ano_antigo != -1 else 1

    match_car += (array[i].ano <= ano_atual)if ano_atual != -1 else 1


    if(match_car == 7):
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

carros_cadastrados.append(createCar("ford","car",2010,500,4))
carros_cadastrados.append(createCar("fiat","uno",2010,420,4))
carros_cadastrados.append(createCar("fiat","elba",2008,320,4))
carros_cadastrados.append(createCar("fiat","tempra",1991,320,4))
carros_cadastrados.append(createCar("pegout","boxer furgão",2001,130,6))
carros_cadastrados.append(createCar("mcLaren","artura",2012,1200,2))
carros_cadastrados.append(createCar("ferrari","288 gto",1984,1300,2))
carros_cadastrados.append(createCar("honda","civic",2010,600,4))
carros_cadastrados.append(createCar("honda","velozte",2005,200,3))
carros_cadastrados.append(createCar("bulgati","aventador",2012,1000,2))
carros_cadastrados.append(createCar("bulgati","forza",2012,1500,2))





while True:
  menuOfOptions()
  action = int(input(">"))
  
  match action:
    case 0:
      break
      
    case 1:
      print("- Insira -")
      marca = input("marca:")
      modelo = input("modelo:")
      ano = int(input("ano:"))
      preco = float(input("preço de aluguel:"))
      lugares = int(input("número de lugares:"))

      
      confirm = simOUnao("cadastrar carro '{} {} {}'".format(marca,modelo,ano)) 

      if(confirm is True):
        carros_cadastrados.append(createCar(marca,modelo,ano,preco,lugares))
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
              print("CARRO NÃO ALUGADO, NÃO É POSSÍVEL DEVOLVER")
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
      print("Caso não queira levar um campo em consideração, aperte 'ENTER'")
      print("----------------------------")
      print("- Insira -")
      marca = input("marca:").lower()
      modelo = input("modelo:").lower()
      ano_antigo = input("Do ano (inicial)... ")
      ano_atual = input("até o ano (final)... ")


      preco_min = input("preço (mínimo):")
      preco_max = input("preço (máximo):")
      assentos = input("Número de assentos (máximo):")

      ano_antigo = int(ano_antigo) if ano_antigo != "" else -1
      ano_atual = int(ano_atual) if ano_atual != "" else -1


      assentos = int(assentos) if assentos != "" else -1
      preco_min = float(preco_min) if preco_min != "" else -1
      preco_max = float(preco_max) if preco_max != "" else -1

     
      
      search_car = createCar(marca,modelo,0,0,0)
      

      carros_encontrados = searchCarList(carros_cadastrados,search_car,preco_min,preco_max,assentos,ano_antigo,ano_atual)
      if(carros_encontrados != []):

        print("Carros Encontrados:")
        listarCarros(carros_encontrados)
        """
        for carro in carros_encontrados:
          print("{} R${:.2f}".format(carro.show().capitalize()))
        """
      else:
        print("Nenhum carro encontrado com tais parametros.")

    case 5:
      print("---- Remoção de Carro ---- ")
      print("Digite os dados do carro que deseja remover")
      print("- Insira -")
      # marca, modelo, ano, preco = 0,lugares = 0,alugado=False):
      marca = input("marca:").lower()
      modelo = input("modelo:").lower()
      ano = int(input("ano:"))


      procurarPor = createCar(marca,modelo,ano,0,0)
      
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
          new_marca = input("marca [{}] :".format(carros_cadastrados[idx].marca )).lower()
          new_modelo = input("modelo [{}]:".format(carros_cadastrados[idx].modelo)).lower()

          new_ano = input("ano [{}]:".format(carros_cadastrados[idx].ano))
          new_preco = input("preço de aluguel [ R${:.2f} ]:".format(carros_cadastrados[idx].preco))
          new_lugares = input("número de assentos [{}]:".format(carros_cadastrados[idx].lugares))
          

          carros_cadastrados[idx].marca = carros_cadastrados[idx].marca if new_marca == "" else new_marca

          carros_cadastrados[idx].modelo = carros_cadastrados[idx].modelo if new_modelo == "" else new_modelo

          carros_cadastrados[idx].ano = carros_cadastrados[idx].ano if new_ano == "" else int(new_ano)

          carros_cadastrados[idx].preco = carros_cadastrados[idx].preco if new_preco == "" else float(new_preco)

          carros_cadastrados[idx].lugares = carros_cadastrados[idx].lugares if new_lugares == "" else int(new_lugares)




          print("DADOS EDITADOS COM SUCESSO!")
          
        else:
          print("AÇÃO CANCELADA!")        

  
      
      
      
    case _:
      print("AÇÃO INVÁLIDA")

  voltar_ao_menu = input("<Aperte qualquer botão para voltar ao menu principal>")
  limpar_tela()
  

  