menu = f"menu principal".upper().center(60)+"""

Seja bem vinda(o) ao nosso gerenciador!

O nosso sistema tem todas as opção para gerar sua conta

                     uuuuuh
                     😊
Vamos começar:

# Escolhe o numero da ação desejada:
[1] depositar 
[2] Saque
[3] Extrato
[4] Sair

==> """

Saldo = 0
Limite = 500
Extrato = ""
Qtde_Saque = 0
Limite_Saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print(" Operação não identificado! Volte ao menu anterior.")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > Saldo

        excedeu_limite = valor > Limite

        excedeu_saques = Qtde_Saque >= Limite_Saque

        if excedeu_saldo:
            print("Você não tem saldo suficiente para realizar esta operação.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            Qtde_Saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n= EXTRATO =")
        print("Não foram realizadas movimentações." 
    if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("")

    elif opcao == "4":
        print("Obrigada por utilizar o nosso sistema de gerenciador !")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
    