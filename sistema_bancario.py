menu = """

  [1] Depósito
  [2] Saque
  [3] Extrato
  [0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Deposito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Insira um valor válido")

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar:"))
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite
    
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor informado excede o limite por saque (R$500.00)")

        elif excedeu_saques:
            print("Falha na operação! Número de saques diário foi excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${saldo:.2f}")
            print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")

        else:
            print("Falha na operação! O valor inforamdo é inválido")

    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "0":
        confirmacao = input("Tem certeza de que deseja sair? (s/n):")
        if confirmacao.lower() == "s":
            print("Obrigado po usar nosso sistema bancário! Até a próxima.")
            break
        else: 
            continue
    
    else:
        print("Operação inválida, por favor selecione uma opção")




    