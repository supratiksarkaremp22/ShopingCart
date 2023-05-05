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
            f'{list(self.compras.keys())[-1]} foi adicionado ao seu carrinho.')
        print(f'Seu total agora é de: {self.total:.2f}R$')
        print()

    def remov_item(self, item):
        print(f'{list(self.compras.keys())[-1]} foi removido do seu carrinho.')
        print()
        self.total -= self.compras[item]
        del self.compras[item]

    def finalizar_compra(self):
        print('Finalizando compra...')  # dps add sleep
        time.sleep(1)

        print(f'Valor total da compra: {self.total:.2f}R$')
        pagamento = str(self.total) + 'R$'

        with open('data_compra.txt', 'a+') as f:
            f.write(f'Compra do usuario {self.user}, ' + str(pagamento) + '\n')

        return pagamento
