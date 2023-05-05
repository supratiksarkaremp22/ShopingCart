import time


class CarrinhoDeCompras:
    def __init__(self, user):
        self.compras = {}
        self.total = 0
        self.user = user

    def add_item(self, item, valor):
        self.compras[item] = valor
        self.total += valor

        print(
            f'{list(self.compras.keys())[-1]} has been added to your cart.')
        print(f'Seu total agora é de: {self.total:.2f}R$')
        print()

    def remov_item(self, item):
        print(f'{list(self.compras.keys())[-1]} has been removed from your cart.')
        print()
        self.total -= self.compras[item]
        del self.compras[item]

    def finalizar_compra(self):
        print('Finalizing purchase...')  # dps add sleep
        time.sleep(1)

        print(f'Total purchase amount: {self.total:.2f}R$')
        pagamento = str(self.total) + 'R$'

        with open('data_compra.txt', 'a+') as f:
            f.write(f'User purchase {self.user}, ' + str(pagamento) + '\n')

        return pagamento
