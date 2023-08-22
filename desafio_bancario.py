# Definindo o saldo inicial e os limites de transação
saldo = 0.00
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500.00

# Listas para armazenar depósitos e saques
depositos = []
saques = []

# Função para formatar o valor como moeda
def formatar_moeda(valor):
    return "R$ {:0.2f}".format(valor)

# Função para exibir as opções do menu
def exibir_menu():
    print("\n[1] DEPÓSITO")
    print("[2] SAQUE")
    print("[3] EXTRATO")
    print("[4] SAIR")

# Função para realizar um depósito
def realizar_deposito():
    valor = input("Digite o valor do depósito: ")
    
    if valor.isdigit():  # Verifica se o valor é um número
        valor = float(valor)
        if valor > 0:
            depositos.append(valor)
            global saldo
            saldo += valor
            print("\nDepósito de {} realizado com sucesso.".format(formatar_moeda(valor)))
        else:
            print("Valor inválido.")
    else:
        print("Valor inválido. Digite um valor!.")

# Função para realizar um saque
def realizar_saque():
    global saldo
    global saques_diarios
    
    if saques_diarios < limite_saques_diarios:
        valor = input("Digite o valor do saque: ")
        
        if valor.isdigit():  # Verifica se o valor é um número
            valor = float(valor)
            if valor > 0 and valor <= limite_saque:
                if saldo >= valor:
                    saques.append(valor)
                    saldo -= valor
                    saques_diarios += 1
                    print("\nSaque de {} realizado com sucesso.".format(formatar_moeda(valor)))
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor acima do limite de saque, consulte o gerente!.")
        else:
            print("Valor inválido. Digite um número.")
    else:
        print("Limite diário de saques atingido.")

# Função para exibir o extrato com o histórico de transações e saldo atual
def exibir_extrato():
    print("============ EXTRATO ============")
    print("DEPÓSITOS:")
    if len(depositos) > 0:
        for deposito in depositos:
            print(formatar_moeda(deposito))
    else:
        print("SEM MOVIMENTAÇÃO")
    
    print("\nSAQUES:")
    if len(saques) > 0:
        for saque in saques:
            print(formatar_moeda(saque))
    else:
        print("SEM MOVIMENTAÇÃO")
        
    print("\nSALDO ATUAL: {}".format(formatar_moeda(saldo)))
    print("============= FIM =============")


# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao.isdigit():  # Verifica se o valor é um número
        opcao = int(opcao)
        if opcao == 1:
            realizar_deposito()
        elif opcao == 2:
            realizar_saque()
        elif opcao == 3:
            exibir_extrato()
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida. Digite um número.")
