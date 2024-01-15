from os import system,name

class Menu():
    def __init__(self):
        self.__actions = ["Sair","Listar carros","Procurar carros"]
    
    def mostrar(self):
        print("RENTAL CAR\nDigite o número da ação que deseja fazer\n------------")
        for i,action in enumerate(self.__actions):
            print("[{}] {}".format(i,action))
        print("------------")

    def limparTela(self):
        cmd = input("<Aperte qualquer botão para voltar ao menu principal>")
        if(name == "nt"): #windows
            system("cls")
        else:
            system("clear")

    
class MenuUsuario(Menu):
    pass

class MenuAdmin(MenuUsuario):
    pass