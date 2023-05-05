from cliente import Client
from carrinho import CarrinhoDeCompras
import time
import os

user = input('Type your user: ')
senha = input('Type your password: ')


with open('data_user.txt', 'a+') as f:
    f.seek(0)

    msg = 'We are checking your register'
    for i in range(3):
        msg += '.'
        print(msg)
        time.sleep(1)

    if ('User: ' + user + ', ' + 'Senha: ' + senha + '\n') in f.readlines():
        print('Login done successfully.')
        print('Loading store...')
        print()
        # print()
        time.sleep(2)
        f.close()
    else:
        f.read()
        print('We do not accept your cadastro, do you want to raise one with the information given?')
        print('Type "yes" if you want, or "não" to end the program.')
        s_n = input()
        if s_n.lower() == 'não' or s_n.lower() == 'nao':
            exit()
        else:
            f.write('User: ' + user)
            f.write(', ')
            f.write('Senha: ' + senha + '\n')
            print('Seu cadastro foi realizado.')
            print('Carregando a loja...')
            print()
            # print()
            time.sleep(2)
            f.close()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()

# navegar pelos itens(1), depositar dinheiro, ir para o carrinho e sair.
itens = {
    'IPHONE X': 5000,
    'NOTEBOOK DELL': 4200,
    'POLVOIDE': 30,
    'CAMISA SUPERBAD': 80,
}

cliente_1 = Cliente()


def compra():
    # "INTERFACE" of purchases, it will show the items to the user, where he can
    # add item, remove item, or checkout
    # If the value of the car is greater than the user's balance, no date of purchase.

    # for key, value in items.items(): # list the items
    #     print(f'{key} custa {value:.2f}R$')
    # print()
    carrinho = CarrinhoDeCompras(user)

    while True:
        print('Type which item you want to buy, if you don't want to buy now, press ENTER.')
        item = input()

        if item.upper() in itens.keys():
            print()
            carrinho.add_item(item, itens[item.upper()])

        print('To continue shopping --> [1]')
        print('To remove any item --> [2]')
        print('To finalize purchase --> [3]')
        print('to see carrinho --> [4]')
        print('to go out --> [5]')
        decisao = input()
        print()

        if decisao == '1':
            for key, value in itens.items():  # lista os itens
                print(f'{key} custa {value:.2f}R$')
            print()
            continue
        elif decisao == '2':
            if len(carrinho.compras) == 0:
                print('Você não possui itens no momento.')
                break

            print('Seus itens no momento são: ')
            for key in carrinho.compras.keys():
                print('-' + key)
            print('Digite o nome do item que você quer remover.')
            i_remov = input()
            carrinho.remov_item(i_remov)
            continue
        elif decisao == '3':
            if cliente_1.saldo < carrinho.total:
                print('Saldo insuficiente. Remova algum item ou deposite dinheiro.')
                continue

            cliente_1.saldo -= carrinho.total
            carrinho.finalizar_compra()
            # tem que ver como eu vou fazer pro cliente pagar
            print(f'Obrigado por comprar conosco, {user}!')
            break

        elif decisao == '4':
            for key, value in carrinho.compras.items():  # lista os itens
                print(f'{key}, {value:.2f}R$')
            print()
            continue
        else:
            break


# cliente_1 = Cliente()

while True:
    print(
        f"""
Saudações {user}! Bem-vindo à loja, selecione o que você quer fazer:
Seu saldo é de: {cliente_1.saldo:.2f}R$
    """
    )

    print('Começar a comprar --> [1]')
    print('Depositar dinheiro --> [2]')
    print('Sair --> [3]')
    choice = input()
    print()

    if choice == '1':
        for key, value in itens.items():  # lista os itens
            print(f'{key} custa {value:.2f}R$')
        print()
        compra()
        continue

    elif choice == '2':
        cliente_1.depositar()
        continue

    elif choice == '3':
        print('Obrigado por visitar nossa loja!')
        exit()
