saldo = 0.00
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500.00

depositos = []
saques = []
extrato = []

usuarios = []
contas = []
proximo_numero_conta = 1

def formatar_moeda(valor):
    return "R$ {:0.2f}".format(valor)

def exibir_menu():
    print("\n[1] \tDEPÓSITO")
    print("[2] \tSAQUE")
    print("[3] \tEXTRATO")
    print("[4] \tCADASTRAR USUÁRIO")
    print("[5] \tCADASTRAR CONTA")
    print("[6] \tLISTAR CONTAS")
    print("[7] \tSAIR")

def validar_data_nascimento(data_nascimento):
    if not data_nascimento.replace("/", "").isdigit():
        return False

    partes = data_nascimento.split("/")
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        if not 1 <= dia <= 31:
            return False
        if not 1 <= mes <= 12:
            return False
        if not 1900 <= ano <= 2100:
            return False
    except:
        return False

    return True

def validar_nome(nome):
    for char in nome:
        if not char.isalpha() and char != ' ':
            return False
    return True

def exibir_saldo():
    print("Saldo disponível: {}".format(formatar_moeda(saldo)))

def realizar_deposito(valor_deposito):
    global saldo
    saldo += valor_deposito
    deposito = {
        "valor": valor_deposito,
        "saldo_anterior": saldo - valor_deposito,
        "saldo_atual": saldo
    }
    depositos.append(deposito)
    print("Depósito realizado com sucesso.")
    exibir_saldo()

def realizar_saque(valor_saque):
    global saldo, saques_diarios
    if saques_diarios >= limite_saques_diarios:
        print("Limite diário de saques atingido.")
        return
    if valor_saque > limite_saque:
        print("O valor do saque excede o limite permitido.")
        return
    if saldo < valor_saque:
        print("Saldo insuficiente.")
        return
    saldo -= valor_saque
    saques_diarios += 1
    saque = {
        "valor": valor_saque,
        "saldo_anterior": saldo + valor_saque,
        "saldo_atual": saldo
    }
    saques.append(saque)
    extrato.append(saque)
    print("Saque realizado com sucesso.")
    exibir_saldo()

def exibir_extrato():
    print("======= EXTRATO =======")
    for movimento in extrato:
        if movimento in depositos:
            print("DEPÓSITO:")
            print("Valor: {}".format(formatar_moeda(movimento["valor"])))
            print("Saldo anterior: {}".format(formatar_moeda(movimento["saldo_anterior"])))
            print("Saldo atual: {}".format(formatar_moeda(movimento["saldo_atual"])))
        elif movimento in saques:
            print("SAQUE:")
            print("Valor: {}".format(formatar_moeda(movimento["valor"])))
            print("Saldo anterior: {}".format(formatar_moeda(movimento["saldo_anterior"])))
            print("Saldo atual: {}".format(formatar_moeda(movimento["saldo_atual"])))
        print("----------------------")
    exibir_saldo()
    print("======================")

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    while not validar_nome(nome):
        print("Nome inválido. Digite apenas letras.")
        nome = input("Digite o nome: ")
    
    while True:
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        if validar_data_nascimento(data_nascimento):
            break
        else:
            print("Formato inválido. Digite a data no formato dd/mm/aaaa.")
    
    while True:
        cpf = input("Digite o CPF: ")
        if cpf.isdigit():
            break
        else:
            print("Formato inválido. Digite apenas números.")
    
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/UF): ")
    
    cpf_existente = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            cpf_existente = True
            break
    
    if not cpf_existente:
        usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        usuarios.append(usuario)
        print("\n --- Usuário cadastrado com sucesso. ---")
    else:
        print("CPF já cadastrado.")
        
def cadastrar_conta():
    global proximo_numero_conta
    
    while True:
        cpf_usuario = input("Digite o CPF do usuário vinculado à conta: ")
        if cpf_usuario.isdigit():
            break
        else:
            print("Formato inválido. Digite apenas números.")
    
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            usuario_encontrado = True
            break
    
    if usuario_encontrado:
        conta = {
            "agencia": "0001",
            "numero": proximo_numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        proximo_numero_conta += 1
        print("\nConta cadastrada com sucesso.")
    else:
        print("Usuário não encontrado.")

def listar_contas():
    print("\n============ CONTAS ============")
    if len(contas) == 0:
        print("")
    else:
        for conta in contas:
            print("Agência: {}".format(conta["agencia"]))
            print("C/C: {}".format(conta["numero"]))
            print("Titular: {}".format(conta["usuario"]["nome"]))
            print("================================")

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    while not validar_nome(nome):
        print("Nome inválido. Favor digite um nome!.")
        nome = input("Digite o nome: ")
    
    while True:
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        if validar_data_nascimento(data_nascimento):
            break
        else:
            print("Formato inválido. Digite a data no formato dd/mm/aaaa em números.")
    
    while True:
        cpf = input("Digite o CPF: ")
        if cpf.isdigit():
            break
        else:
            print("Formato inválido. Digite apenas números.")
    
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/UF): ")
    
    cpf_existente = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            cpf_existente = True
            break
    
    if not cpf_existente:
        usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso.")
    else:
        print("CPF já cadastrado.")
        
def cadastrar_conta():
    global proximo_numero_conta
    
    while True:
        cpf_usuario = input("Digite o CPF do usuário vinculado à conta: ")
        if cpf_usuario.isdigit():
            break
        else:
            print("Formato inválido. Digite apenas números.")
    
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            usuario_encontrado = True
            break
    
    if usuario_encontrado:
        conta = {
            "agencia": "0001",
            "numero": proximo_numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        proximo_numero_conta += 1
        print("Conta cadastrada com sucesso.")
    else:
        print("Usuário não encontrado.")

def listar_contas():
    print("============ CONTAS ============")
    for conta in contas:
        print("Agência: {}".format(conta["agencia"]))
        print("C/C: {}".format(conta["numero"]))
        print("Titular: {}".format(conta["usuario"]["nome"]))
        print("================================")

def realizar_deposito(valor):
    global saldo
    global depositos
    global extrato

    depositos.append(valor)
    saldo += valor
    extrato.append("Depósito de {}".format(formatar_moeda(valor)))
    print("\nDepósito de {} realizado com sucesso.".format(formatar_moeda(valor)))

def realizar_saque(valor):
    global saldo
    global saques_diarios
    global limite_saques_diarios
    global limite_saque
    global saques
    global extrato
    
    if saques_diarios < limite_saques_diarios:
        if valor > 0 and valor <= limite_saque:
            if saldo >= valor:
                saques.append(valor)
                saldo -= valor
                saques_diarios += 1
                extrato.append("Saque de {}".format(formatar_moeda(valor)))
                print("\nSaque de {} realizado com sucesso.".format(formatar_moeda(valor)))
            else:
                print("\nSaldo insuficiente.")
        else:
            print("\nValor acima do limite de saque, consulte o gerente!")
    else:
        print("\nLimite diário de saques atingido.")

def exibir_extrato():
    global saldo
    global depositos
    global saques
    global extrato
    
    print("\n============ EXTRATO ============")
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

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")
    
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            while True:
                valor_deposito = input("Digite o valor do depósito: ")
                if valor_deposito.isdigit():
                    break
                else:
                    print("Valor inválido. Por favor disite um valor válido.")
            realizar_deposito(float(valor_deposito))
        elif opcao == 2:
            while True:
                valor_saque = input("Digite o valor do saque: ")
                if valor_saque.isdigit():
                    break
                else:
                    print("Valor inválido. Por favor disite um valor válido.")
            realizar_saque(float(valor_saque))
        elif opcao == 3:
            exibir_extrato()
        elif opcao == 4:
            cadastrar_usuario()
        elif opcao == 5:
            cadastrar_conta()
        elif opcao == 6:
            listar_contas()
        elif opcao == 7:
            break
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida. Digite um número.")
