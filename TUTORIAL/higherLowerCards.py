from random import shuffle

class Carta:
    def __init__(self,naipe,rank,valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor
    
    def show(self):
        return "{} {}".format(self.naipe,self.rank) 

class Baralho:
    NAIPE = ('Spades','Hearts','Clubs','Diamonds')
    RANK = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

    def __init__(self,lista=[]):
        self.lista = lista

    def embaralhar(self):
        nova_lista = self.lista.copy()
        shuffle(nova_lista)
        self.lista = nova_lista
    
    def getCard(self):
        carta = self.lista.pop()
        return carta

    def dealCards(self):
        self.lista = []

        for naipe in self.NAIPE:
            for valor,rank in enumerate(self.RANK):
                carta = Carta(naipe,rank,valor+1)
                self.lista.append(carta)
    
    def showCards(self):
        for number,carta in enumerate(self.lista):
            print(number+1,carta.show())
            if (number+1)%13 == 0:
                print("--------")

class Jogador:
    POINT = 5 

    def __init__(self,score=10):
        self.score = score
    
    def lose(self):
        print("Errou!\n-{} pontos".format(self.POINT)) 
        self.score -= self.POINT

    def win(self):
        print("Acertou!\n+{} pontos".format(self.POINT))
        self.score += self.POINT

print("------CARTO-MASTER------")
print("Diga se a próxima carta é maior ou menor que a atual.")
print("------------------------")

baralho = Baralho()
NCARDS = 8

while True:
    
    baralho.dealCards()
    baralho.embaralhar()

    jogador = Jogador()

    carta_atual = baralho.getCard()

    for i in range(0,NCARDS):
        print("Score: {}".format(jogador.score))
        resposta_do_jogador = input("A próxima carta será maior ou menor que {} ({}) [h/l]?\nR>".format(carta_atual.show(),carta_atual.valor))

        resposta_do_jogador = resposta_do_jogador.casefold()

        proxima_carta = baralho.getCard()
        
        print("Carta puxada é {} ({})".format(proxima_carta.show(),proxima_carta.valor))

        if proxima_carta.valor == carta_atual.valor:
            print("Nem maior nem menor!\nEmpate: você nem perde nem ganha pontos")
        else:

            if resposta_do_jogador == 'h':
                if proxima_carta.valor > carta_atual.valor :
                    jogador.win()
                else:
                    jogador.lose()
            elif resposta_do_jogador == 'l':
                if proxima_carta.valor < carta_atual.valor :
                    jogador.win()
                else:
                    jogador.lose()      

    

        carta_atual = baralho.getCard()
    print("Score: {}".format(jogador.score))
    goAgain = int(input("Quer continuar? [1/0]"))

    
    if not(goAgain):
        break
    print()






    










