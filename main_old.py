#show()
from Carro import Carro
from Usuario import Usuario
from os import system,name

#PUSH REMOTE ORIGIN,PLEASE!

def menuOfOptions():
    print("----- RENTAL CAR - Aluguel de Carros -----")
    print("(0) SAIR")
    print("(1) Cadastrar carro")
    print("(2) Listar carros")
    print("(3) Alugar ou devolver carro")
    print("(4) Pesquisar carro")
    print("(5) Remover carro")
    print("(6) Editar dados de carro")
    print(" - ÁREA DO USUÁRIO -")
    print("(7) Cadastrar usuário")
    print("(8) Listar usuários") #função de altar_ordem (implementar)
    print("(9) Buscar usuário")
    print("(10) Ver contratos") 
    print("(11) Remover\editar dados de usuário") 

    print("Digite o número da ação que deseja fazer.")


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

def criarUsuario(nome,id):
  new_usuario = Usuario(nome,id)

  return new_usuario

def listarUsuarios(array):
  print("-------- lista de usuários cadastrados -------- ")
  print("<nome> <[id]>")
  print("--------")
  i = 1
  for user in array:
    print("[{}] {} [{}]".format(i,user.nome,user.id))
    i += 1
  print("--------")

#EXTINTO
def listarCarros(array,idNomeTable):

  print("-------- lista de carros -------- ")
  print("<nome> <preço do aluguel> <número de assentos> <disponibilidade> ")
  print("D: DISPONÍVEL")
  print("N/A: CARRO NÃO DISPONÍVEL (incluindo quem o alugou)")
  print("--------")


  for i in range(0,len(array)):
    disponivel = "D" if array[i].alugado is False else "N/A"

    contratante = "" if array[i].alugado is False else idNomeTable[array[i].getDono()]
    
    #print("[{}] {} ({}) R${:.2f} {} {}".format(i+1,array[i].show().capitalize(),disponivel,array[i].preco,array[i].lugares))

    print("[{}] {} R${:.2f} {} ({}) {}".format(i+1,
                                     array[i].show().capitalize(),
                                     array[i].preco,
                                     array[i].lugares,
                                     disponivel,
                                     contratante))
    

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

def searchUser(array,usuario):
  found = []

  for i in range(0,len(array)):
    match_u = 0
    match_u += usuario.nome in array[i].nome.lower()
    match_u += array[i].id == usuario.id.lower()

    if(match_u >= 1):
      found.append(array[i])
  
  return found
  
#searchCarList(carros_cadastrados,search_car,preco_min,preco_max,assentos,ano_antigo,ano_atual)
def searchCarList(array,carro):
  #vai me retornar uma lista com os carros encontrados que deram match com os paramentros dados
  
  deuMatchCom = []
  for i in range(0,len(array)):
    match_car = 0

    match_car += (array[i].marca == carro.marca) if carro.marca != "" else 1
    match_car += (array[i].modelo == carro.modelo) if carro.modelo != "" else 1

    match_car += (array[i].preco >= carro.preco_min)if carro.preco_min != -1 else 1
    
    match_car += (array[i].preco <= carro.preco_max)if carro.preco_max != -1 else 1

    match_car += (array[i].lugares <= carro.assentos)if carro.assentos != -1 else 1

    match_car += (array[i].ano >= carro.ano_antigo) if carro.ano_antigo != -1 else 1
    
    #print(carro.ano_atual,array[i].ano)
    match_car += (array[i].ano <= carro.ano_atual) if carro.ano_atual != -1 else 1

    #print(match_car)


    if(match_car == 7):
      deuMatchCom.append(array[i])
      
  return deuMatchCom

def juntarNome(array):
  novo = []
  for i in array:
    novo.append(i.capitalize()) 
  
  #print(" ".join(novo))

  return " ".join(novo)


"""
  #3. Alugar carro
  O usuário pode alugar um carro mudando o status 'alugado' do objeto da classe Carro para True
"""

contratos = dict([])

idNomeTable = dict([])

usuarios_cadastrados = []
carros_cadastrados = []

usuariosFile = open("cliente-data.txt","rt")

for line in usuariosFile:
  dados = line.split()

  id_cliente = dados[len(dados)-1]

  nome_cliente = [] 

  for i in range(0,len(dados) - 1):
    nome_cliente.append(dados[i])
  
  nome_cliente = juntarNome(nome_cliente)

  clienteObject = criarUsuario(nome_cliente,id_cliente)

  usuarios_cadastrados.append(clienteObject)

usuariosFile.close()

carrosFile = open("carro-data.txt","rt")

for line in carrosFile:
  dados = line.split()
  #xprint(dados)

  alugado = True if dados[5] == "True" else False

  dono = dados[len(dados)-1] if len(dados) == 7 else ""

  ano = dados[2]

  carro = Carro(dados[0],dados[1],ano,dados[3],dados[4],alugado,dono)

  carros_cadastrados.append(carro)

carrosFile.close()

for user in usuarios_cadastrados:
  idNomeTable[user.id] = user.nome


"""
for usuario in usuarios_cadastrados:
  nomes = usuario.nome.split()
  novo = []
  for i in nomes:
    novo.append(i.capitalize()) 
  
  print(" ".join(novo))
  idNomeTable[usuario.id] = " ".join(novo)
"""

while True:
  menuOfOptions()
  action = int(input(">"))
  
  match action:
    case 0:
      break
      
    case 1:
      while True:

        print("---- Cadastro de Carro ----")
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
        
        continuar = simOUnao("cadastrar mais algum carro")

        if(not(continuar)):
           break
        limpar_tela()
      
    case 2:
      listarCarros(carros_cadastrados,idNomeTable)
  
    case 3:

      while(True):

        subAction = int(input("Deseja alugar ou devolver um carro?\n[1] alugar\n[2] devolver\n>"))
  
        match subAction:
        
          case 1:
            listarCarros(carros_cadastrados,idNomeTable)
            idx = int(input("Digite o indice do carro que deseja alugar\n>"))
            
            if idx <= 0 or idx > len(carros_cadastrados):
              print("CARRO NÃO ENCONTRADO")
            elif carros_cadastrados[idx-1].alugado is True:
              print("CARRO NÃO DISPONIVEL")
            else:
              #nome_carro = carros_cadastrados[idx-1].show()

              print("Para qual usuário o carro '{}' será alugado?".format(carros_cadastrados[idx-1].show()))

              listarUsuarios(usuarios_cadastrados)

              while True:

                encontrado = False
                id_user = input("Digite o ID do usuário escolhido:")

                for u in usuarios_cadastrados:
                  if id_user == u.id:
                    encontrado = True
                    break
                
                if(not(encontrado)):
                  print("ID não econtrado.\nDigite novamente.")
                else:
                  break

                    
              confirm = simOUnao("alugar carro '{}' para {}".format(carros_cadastrados[idx-1].show().capitalize(),idNomeTable[id_user].capitalize()))
  
              if(confirm is True):

                carros_cadastrados[idx-1].alugado = True
                carros_cadastrados[idx-1].setDono(id_user)

                if id_user in contratos:
                  contratos[id_user].append(carros_cadastrados[idx-1])
                else:
                  contratos[id_user] = [carros_cadastrados[idx-1]]


                print("CARRO ALUGADO COM SUCESSO!")
              else:
                print("AÇÃO CANCELADA!")
  
          case 2:
            listarCarros(carros_cadastrados,idNomeTable)
            idx = int(input("Digite o indice do carro que deseja devolver\n>"))
  
            if idx <= 0 or idx > len(carros_cadastrados):
              print("CARRO NÃO ENCONTRADO")
            elif carros_cadastrados[idx-1].alugado is False:
              print("CARRO NÃO ALUGADO, NÃO É POSSÍVEL DEVOLVER")
            else:
              confirm = simOUnao("devolver carro '{}'".format(carros_cadastrados[idx-1].show().capitalize()))
  
              if(confirm is True):
                
                contratos[carros_cadastrados[idx-1].getDono()].remove(carros_cadastrados[idx-1])

                if contratos[carros_cadastrados[idx-1].getDono()] == []:
                  contratos.pop(carros_cadastrados[idx-1].getDono())

                carros_cadastrados[idx-1].alugado = False
                carros_cadastrados[idx-1].setDono("")

                print("CARRO DEVOLVIDO COM SUCESSO!")
              else:
                print("AÇÃO CANCELADA!")
              """
              carros_cadastrados[idx-1].alugado = False
              print("CARRO DEVOLVIDO")
              """
  
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
      search_car.preco_min = preco_min
      search_car.preco_max = preco_max

      search_car.assentos = assentos
      search_car.ano_antigo = ano_antigo
      search_car.ano_atual = ano_atual
      

      carros_encontrados = searchCarList(carros_cadastrados,search_car)
      if(carros_encontrados != []):

        print("Carros Encontrados:")
        listarCarros(carros_encontrados,idNomeTable)
        """
        for carro in carros_encontrados:
          print("{} R${:.2f}".format(carro.show().capitalize()))
        """
      else:
        print("Nenhum carro encontrado com tais parametros.")

    case 5:
      print("---- Remoção de Carro ---- ")

      for carro in carros_cadastrados:
        dispo = "D" if carro.alugado is False else "N/A" 
        print("- {} R${:.2f} {}".format(carro.show(),carro.preco,dispo))

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

        if(carro_encontrado[0].alugado):
          print("CARRO NÃO PODE SER REMOVIDO POIS JÁ ESTÁ ALUGADO")
          print("Contrante:",carro_encontrado[0].getDono())
        else:

          confirm = simOUnao("remover carro '{}'".format(carro_encontrado[0].show().capitalize()))

          if(confirm is True):
            carros_cadastrados.remove(carro_encontrado[0])
            print("CARRO REMOVIDO")
          else:
            print("AÇÃO CANCELADA")
      else:
        print("Carro não encontrado.")
        
    case 6:
      print("---- Editar dados de carro ----")
      listarCarros(carros_cadastrados,idNomeTable)
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

          carros_cadastrados[idx].ano = carros_cadastrados[idx].ano if new_ano == "" else new_ano

          carros_cadastrados[idx].preco = carros_cadastrados[idx].preco if new_preco == "" else new_preco

          carros_cadastrados[idx].lugares = carros_cadastrados[idx].lugares if new_lugares == "" else new_lugares




          print("DADOS EDITADOS COM SUCESSO!")
          
        else:
          print("AÇÃO CANCELADA!")        

    case 7:
      while True:
        print("---- Cadastrar usuário ----")
        print("Digite os dados do usuário que deseja cadastrar")
        print("Nome: <nome do usuário>\nId: <indetificação única>")
        print("- Insira -")
        nome_usuario = input("Nome:").lower().split()

        nome_usuario = juntarNome(nome_usuario)

        #print(nome_usuario)

        id_usuario = ""
        while True:
          id_usuario = input("Id:").lower()

          if id_usuario in idNomeTable or id_usuario != "":
            print("Esse id já existe.\nInsira outro,por favor.")
          else:
            break

          """
          for id_u in usuarios_cadastrados:
            if(id_usuario == id_u.id):
              
              stop = False
              break
          
          if(stop):
            break
          """

        confirm = simOUnao("cadastrar usuário '{} [{}]'".format(nome_usuario,id_usuario)) 
        if(confirm):
          usuarios_cadastrados.append(criarUsuario(nome_usuario,id_usuario))
          idNomeTable[id_usuario] = nome_usuario

          print("USUÁRIO CADASTRADO COM SUCESSO!")
        else:
          print("CADASTRO CANCELADO.")

        continuar = simOUnao("cadastrar mais algum usuário") 

        if(not(continuar)):
          break
        limpar_tela()
    
    case 8:
      listarUsuarios(usuarios_cadastrados)
       
    
    case 9:
      print("---- Pesquisa de usuário ---- ")
      print("Preencha os campos abaixo para realizar a pesquisa")
      print("Caso não queira levar um campo em consideração, aperte 'ENTER'")
      print("----------------------------")
      print("- Insira -")
      nome = input("Nome:").lower()
      id = input("Id:").lower()

      usuario_pesquisar = criarUsuario(nome,id)

      user_found = searchUser(usuarios_cadastrados,usuario_pesquisar)

      if(user_found == []):
        print("Usuário não encontrado")
      else:
        print("USUÁRIO(S) ENCONTRADO(S) COM TAIS PARÂMETROS:")
        for i in user_found:
          print("{} [{}]".format(i.nome,i.id))

    case 10:
      print("---- Área de Contratos ---- ")
      #print("<nomeDeUsuário> A(N): 'o usuário <nomeDeUsuário> alugou N carros' ")
      print("----------------------------")
      
      if contratos.keys() == []:
        print("NÃO HÁ NENHUM ALUGUEL NO MOMENTO")

      else:
        for user_id in contratos.keys():
          print("{} alugou {} carro(s):".format(idNomeTable[user_id].capitalize(), len(contratos[user_id])))
          for carro in contratos[user_id]:
            print("   ",carro.show().capitalize())
        
      #print(idNomeTable)
    
    case 11:
      print("---- Editar ou Remover dados de usuário ----")
      listarUsuarios(usuarios_cadastrados)
      idx = int(input("Digite o indice do usuário que deseja editar / remover\n>"))

      if idx <= 0 or idx > len(usuarios_cadastrados):
        print("USUÁRIO NÃO ENCONTRADO")
      elif usuarios_cadastrados[idx-1].id in contratos:
        print("USUÁRIO JÁ TEM CONTRATO DE ALUGUEL DE CARRO.\nNão é possível editar/remover dados.")
      else:
        idx -= 1 

        subAction = int(input("Deseja remover ou editar dados de usuário?\n[1] editar dados\n[2] remover usuário\n>"))
  
        match subAction:
          case 1:
            confirmar = simOUnao("editar dados do usuário '{}'".format(usuarios_cadastrados[idx].nome))

            if(confirmar is True):
              print("Insira os novos dados")
              print("Caso não queira fazer modificações no campo, aperter ENTER no campo selecionado")
              new_nome = input("NOME [{}]:".format(usuarios_cadastrados[idx].nome)).lower().split()
              new_id = input("ID [{}]:".format(usuarios_cadastrados[idx].id)).lower()
            
              new_nome = juntarNome(new_nome)

              id_antigo = usuarios_cadastrados[idx].id

              usuarios_cadastrados[idx].nome = usuarios_cadastrados[idx].nome if new_nome == "" else new_nome

              usuarios_cadastrados[idx].id = usuarios_cadastrados[idx].id if new_id == "" else new_id

              print(id_antigo in idNomeTable)
              #idNomeTable.pop(id_antigo)

              idNomeTable[usuarios_cadastrados[idx].id] = usuarios_cadastrados[idx].nome

              if(new_nome == "" and new_id == ""):
                print("NENHUMA MODIFICAÇÃO FEITA!")
              else:
                print("MODIFICAÇÕES SALVAS!")
            else:
              print("AÇÃO CANCELADA")
          case 2:
            confirmar = simOUnao("remover '{}'".format(usuarios_cadastrados[idx].nome))

            if(confirmar):
              usuarios_cadastrados.remove(usuarios_cadastrados[idx])

            else:
              print("AÇÃO CANCELADA")
          case _:
            print("AÇÃO INVÁLIDA")        
    case _:
      print("AÇÃO INVÁLIDA")

  voltar_ao_menu = input("<Aperte qualquer botão para voltar ao menu principal>")
  limpar_tela()
  
usuariosFile = open("cliente-data.txt","wt")

for user in usuarios_cadastrados:
  usuariosFile.write("{} {}\n".format(user.nome,user.id))

usuariosFile.close()

carrosFile = open("carro-data.txt","wt")

for carro in carros_cadastrados:
  carrosFile.write("{} {} {} {} {} {} {}\n".format(carro.marca,
                                                 carro.modelo,
                                                 carro.ano,
                                                 carro.preco,
                                                 carro.lugares,
                                                 carro.alugado,
                                                 carro.getDono()))  

carrosFile.close()
  