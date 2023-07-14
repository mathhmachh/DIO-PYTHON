menu = """"

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = (input(menu))

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! Informe um valor válido.")
    
    elif opcao =="2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
             print("Não há saldo suficiente para essa operação.")

        elif excedeu_limite:
            print("Limite por operacao ultrapassado.")

        elif excedeu_saques:
            print("Você exceudeu seu número de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "3":
        print ("\n==============EXTRATO==============") 
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")        

    elif opcao == "4":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")