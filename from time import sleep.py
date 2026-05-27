from time import sleep

# criando o fogao
class Fogao():
    # atributos de classe
    bocas = 5

    # metodo construtor
    def __init__(self, gas: bool = False, aceso: bool = False, quantidade: float = 0):
        # atributos de instancia
        self.gas = gas
        self.aceso = aceso
        self.quantidade = quantidade

    # metodos de instancia
    def acender(self):
        self.aceso = True

    def apagar(self):
        self.aceso = False

    def explodir(self):
        if self.gas:
            self.quantidade = float(input('Quantos KG de gas tem no seu bujão? '))

            if self.quantidade < 50:
                print("Você está seguro!")
            elif self.quantidade >= 50:
                print("Você está em Perigo!")

                for c in range(3, 0, -1):
                    print(c)
                    sleep(1)

                print('KABOOOOOOOOOOOOOMMMMMMMMMM!!!!!!!!!!!!!')
                
                sleep(0.5)

                print('EXPLODIU!!!!!!!!!!!!!!!!!!!!!')

    def ver_status_fogao(self):
        if self.aceso:
            print('Fogao está ligado!')
        else:
            print('Fogao está desligado!')

class Fogao_4_bocas(Fogao):
    def __init__(self, forno: bool = True):
        super().__init__(bocas)
        self.forno = forno

        def ver_forno(self):
            if self.forno:
                return "Seu fogao tem forno!"
            else:
                return "Seu fogao não tem forno!"

fogao = Fogao()
fogao_2 = Fogao_4_bocas()

fogao.ver_status_fogao()
fogao_2.ver_status_fogao()
fogao.acender()
fogao_2.acender()
fogao.ver_status_fogao()
fogao_2.ver_status_fogao()