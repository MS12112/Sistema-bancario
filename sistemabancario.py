menu = """

=========MENU==========

    [1] Depoisitar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("======Deposito======\n")
        deposito = float(input("Informe o valor desejado: "))
        
        if deposito > 0:
            saldo += deposito
            
        else:
            print("Operação falhou! Valor inválido")
        
        
    elif opcao == "2":
        print("======Saque======\n")
        saque = float(input("Informe o valor desejado: "))
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação Falhou! Valor do saque excedeu.")
            
        elif excedeu_saques:
            print("Operação Falhou! Número excedido de saques.")
            
        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            
        else: 
            print("Operação Falhou! Valor Inválido.")
            
        
    elif opcao == "3":
        print("======Extrato======")
        print(f"Saldo: {saldo:.2f}")
        
    
    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")