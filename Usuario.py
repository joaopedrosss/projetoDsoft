
class Usuario():
    def __init__(self,nome= '',id = '', carros = []):
        self.__nome = nome
        self.__id = id
        self.__carros = carros

    def getNome(self):
        return self.__nome
    
    def getId(self):
        return self.__id

    def getCarros(self):
        return self.__carros

    def setNome(self, value):
        self.__nome = value
    
    def setId4(self,value):
        self.__id = value

    def alugarCarro(self,carro):
        
        pass

    def devolverCarro(self,carro):
        pass
    
    """
    print("(0) SAIR"
    print("(2) Listar carros"
    print("(3) Alugar ou devolver carro"
    print("(4) Pesquisar carro"
    printt (5)"ver meus alugueis"
    """
class ListaUsuario():
    def __init__(self,lista = []):
        self.__lista = lista

    def mostrar(self):
        pass
    def procurar(self,value):
        pass





