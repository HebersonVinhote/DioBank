from datetime import datetime


menu = '''
=====####===== Bem Vindo ao DioBank!! =====####=====
==== Escolha uma das opções para continuar. ====
[1] - Saldo
[2] - Extrato 
[3] - Saque
[4] - Depósito
[5] - Nova Usuario
[6] - Nova Conta
[7] - Sair
'''
usuario = {}
saldo = 0
extrato = {}
limite = 500
LIMITE_SAQUE = 3
agencia = '0001'
contas = []
usuarios = []

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")



while True:
    try:
        print(menu)
        opcao = int(input('Opção:\t'))

        if opcao == 1:
            saldo_formatado = '{:.2f}'.format(saldo)
            print('Seu Saldo é de R$:', saldo_formatado)

        elif opcao == 2:
            print("=====##===== Extrato =====##=====")
            for data, lista_acao in extrato.items():
                print("{}:".format(data))
                for acao in lista_acao:
                    print("- {}".format(acao))
            print('''
=====####=====####=====####=====
Seu saldo atual é de R$:''', saldo)
            print("=====####=====####=====####=====")
        elif opcao == 3:
            try:
                saque = float(input('digite o valor do saque: '))
                excedeu_limite = saque > limite
                excedeu_saque = LIMITE_SAQUE == 0
                excedeu_saldo = saque > saldo

                if excedeu_limite:
                    print("Valor excede o limite por saque")
                elif excedeu_saque:
                    print("Limite de saques diarios excedido")
                elif excedeu_saldo:
                    print("Saldo insuficiente")
                elif saque <= saldo:
                    saldo -= saque
                    LIMITE_SAQUE -= 1
                    data_saque = datetime.now().strftime('%d/%m/%y %H:%M:%S')
                    extrato[data_saque] = []
                    extrato[data_saque].append("Saque no valor de R$: {}".format(saque))
                    print('Saque feito com sucesso!')
            except ValueError:
                print('Valor inválido. Por favor, insira um número válido.')
        elif opcao == 4:
            try:
                deposito = float(input('digite o valor do deposito: '))
                if deposito > 0:
                    saldo += deposito
                    data_deposito = datetime.now().strftime('%d/%m/%y %H:%M:%S')
                    extrato[data_deposito] = []
                    extrato[data_deposito].append("Deposito no valor de R$: {}".format(deposito))

                    print('Deposito feito com sucesso!')
                elif deposito <= 0:
                    print("Valor inválido. Digite um valor acima de R$: 0.00")

            except ValueError:
                print('Valor inválido. Por favor, insira um número válido.')
        elif opcao == 5:
            criar_usuario(usuarios)
        elif opcao == 6:
            contas = len(contas) + 1
            conta = criar_conta(agencia, contas, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 7:
            print('''
            =====####===== 
            == Até logo ==
            =====####=====
            ''')
            break
    except ValueError:
        print('Opção inválida.')
