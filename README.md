# Desafio Sistema Bancário 


**O desafio foi criar uma versão inovadora do sistema bancário, com operações de `depósito`, `saque` e `extrato`. Nesse sistema, apenas valores positivos e números são permitidos, garantindo a precisão das transações. Limitamos o número de saques a 3 por dia, com valor máximo de R$500, promovendo o controle financeiro. Se o saldo for insuficiente, uma mensagem é exibida. O extrato lista todas as operações, incluindo depósitos e saques, com o saldo atual no final. Essa versão prioriza a segurança, facilidade de uso e transparência. Transforme sua vida financeira com essa inovação!**

# 🔧 Apresentação do código

Declaração de classes e enumerações

Definindo o saldo inicial e os limites de transação
```
saldo = 0.00
saques_diarios = 0
limite_saques_diarios = 3
limite_saque = 500.00
```
Nessa parte, são definidas as variáveis que controlam o `saldo atual`, o número de `saques diário`s permitidos e o limite de saque por transação. Esses valores podem ser ajustados de acordo com as necessidades do sistema.

Listas para armazenar depósitos e saques
```
depositos = []
saques = []
```
Essas listas são usadas para armazenar os valores de `depósitos` e `saques` realizados pelo usuário.

Função para formatar o valor como moeda
```
def formatar_moeda(valor):
    return "R$ {:0.2f}".format(valor)
```
Essa função recebe um valor numérico como argumento e retorna uma string formatada como uma `quantidade monetária`. Por exemplo, se o valor é 10.5, a função retorna R$ 10.50.

Função para exibir as opções do menu
```
def exibir_menu():
    print("\n[1] DEPÓSITO")
    print("[2] SAQUE")
    print("[3] EXTRATO")
    print("[4] SAIR")
```
Essa função simplesmente imprime as opções disponíveis no menu para o usuário.

Função para realizar um depósito
```
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
```
Essa função solicita ao usuário o valor do depósito, verifica se é um valor válido e, em caso afirmativo, adiciona o valor à lista de depósitos e atualiza o saldo. Caso contrário, exibe uma mensagem de erro.

Função para realizar um saque
```
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
```
Essa função permite ao usuário realizar um saque. O número máximo de saques diários é controlado pela variável limite_saques_diarios. A função valida se o valor é um número e se está dentro do limite permitido. Se o saldo for suficiente, o valor do saque é deduzido do saldo atual e o saque é registrado na lista de saques. Caso contrário, é exibida uma mensagem de erro.

Função para exibir o extrato com o histórico de transações e saldo atual
```
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
```
Essa função exibe o extrato das transações, mostrando todos os depósitos e saques realizados pelo usuário, bem como o saldo atual. Caso não haja nenhuma transação registrada, é exibida uma mensagem informando que não há movimentação.

Loop principal do programa
```
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
```
Esse é o loop principal do programa, onde o usuário é apresentado ao menu, escolhe uma opção e a função correspondente é chamada de acordo com a opção selecionada. O loop continua até o usuário escolher a opção de sair (4).

## 📦 Implementação

**# Dica:** Utilizando classes e métodos estáticos.

**# Dica:** Utilizando funções dentro de um módulo separado.

**# Dica:** Utilizando funções dentro de um único arquivo de script.

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Visual Studio Code](https://code.visualstudio.com/) - Code Editing


## ✒️ Autores


* **Rodrigo Neris** -  [*Trabalho Inicial*](https://github.com/rodrigonerisalves)
---
⌨️ com ❤️ por [Rodrigo Neris](www.linkedin.com/in/rodrigo-neris) 😊