import time


class Cliente:
    def __init__(self, saldo=10000):
        self.saldo = saldo

    def depositar(self):
        while True:
            valor = input('What amount do you want to deposit?')
            try:
                valor = int(valor)
                self.saldo += valor

                print('Making deposit...')
                time.sleep(1)
                print(f'{valor:.2f}R$ is deposited in your account.')
                break
            except:
                print('Enter only valid numbers.')
                continue
