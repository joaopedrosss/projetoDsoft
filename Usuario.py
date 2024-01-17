
class Usuario():
    
    def __init__(self,nome= '',id = '',logado = False,passw = "",admin = False,carros = []):
        self.__nome = nome
        self.__id = id
        self.__carros = carros
        self.__login = logado
        self.__admin = admin
        self.__password = passw

    """    
    def alugarCarro(self,carro):
        print("------------")
        print("Aluguel/Devolução de Veículos")
        print("------------")
    """

    def mostrarCarrosAlugados(self):
        print("--- CARROS ALUGADOS ---")
        for carro in self.getCarros():
            print("{} R${:.2f}".format(carro.mostrar().capitalize(),carro.getPreco()))
        print("---                 ---")

    def getAdmin(self):
        return self.__admin
   
    def getPass(self):
        return self.__password
    def setPass(self,value):
        self.__password = value

    def getLogin(self):
        return self.__login
    def setLogin(self,value):
        self.__login = value
    
    def getNome(self):
        return self.__nome
    def getId(self):
        return self.__id
    def getCarros(self):
        return self.__carros
    
    def setNome(self, value):
        self.__nome = value
    def setId(self,value):
        self.__id = value

    def logar(self):
        self.setLogin(True)
    def deslogar(self):
        self.setLogin(False)

    def selecionarEm(self,lista): #lista = lista_objeto
        lista.mostrar()

        carro_idx = input("Digite o indíce do item desejado >")

        try:
            carro_idx = int(carro_idx)
        except:
            print("Valor inválido.\nTente novamente")
            return None
        
        if(carro_idx <= 0 or carro_idx > lista.getSize()):
            print("Indíce inválido.\nTente novamente")
            return None
        else:
            return lista.getByIdx(carro_idx-1)
        
    def alugarCarro(self,carro):        
        if(carro.getAlugado() is False):
            carro.setAlugado(True)
            carro.setDono(self.getId())
            self.__carros.append(carro)
            print("Carro alugado com sucesso")
        else:
            print("O veículo já está alugado.\nNão é possível aluga-lo.")

    def devolverCarro(self,carro):
        if((carro.getAlugado() is True) and carro.getDono() == self.getId()):
            carro.setAlugado(False)
            carro.setDono("")
            self.__carros.remove(carro)
            print("Veículo devolvido com sucesso")
        else:
            print("O veículo não foi alugado por você.\nNão é possível devolver tal veículo.")
 
class Admin(Usuario):
    def __init__(self,nome= '',id_ = '',logado = False,passw = "",admin = True,carros = []):
        super().__init__(nome,id_,logado,passw,admin,carros)
    
    def cadastarCarro(self,lista):
        pass

    def cadastrarUsuario(self,lista):
        pass

    def editarCarro(self,carro):
        pass

    def editarUsuario(self,user):
        pass

    def removeCarro(self,lista):
        pass

    def removerUser(self,lista):
        pass

class ListaUsuario():
    def __init__(self,lista = []):
        self.__lista = lista

    def getSize(self):
        return len(self.getUsuarios())
    
    def getByIdx(self,idx): #Retorne o  na posição 'idx'
        return self.__lista[idx]

    def getUsuarios(self):
        return self.__lista
    
    def setUsuarios(self,value):
        self.__lista.append(value)

    def mostrar(self):
        print("Lista de Usuários cadastrados")
        print(" <nome> [<id]>")
        print(" ------------ ")
        
        if(self.getUsuarios() == []):
            print("Não há usuários cadastrados.")
        else:
            for count,user in enumerate(self.getUsuarios()):
                #print("{} [{}] <{}>".format(user.getNome(),user.getId(),user.getPass()))
                word = "{} {} [{}]".format(count+1,user.getNome(),user.getId())
                word += " (admin)" if user.getAdmin() else ""
                print(word)
                
        
        print(" ------------ ")

    def procurar(self,value):
        pass

    def theUserExist(self,value):
        pass
        





