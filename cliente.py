import time


class Cliente:
    def __init__(self, saldo=10000):
        self.saldo = saldo

    def depositar(self):
        while True:
            valor = input('Qual a quantia que você deseja depositar? ')
            try:
                valor = int(valor)
                self.saldo += valor

                print('Realizando depósito...')
                time.sleep(1)
                print(f'{valor:.2f}R$ foram depositados na sua conta.')
                break
            except:
                print('Digite apenas números válidos.')
                continue
