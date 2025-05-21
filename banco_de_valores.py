cont_saque = 0
LIMITE_SAQUE = 500
extrato = 0
opção = ""
lista_de_acontecimentos = []
saque = 0

while opção != "q":

    tabela = print("""
    ==========================
            BANCO           
    ==========================
       [s]Saque.            
       [d]Deposito.         
       [e]Extrato.          
       [q]Sair.             
        """)
    print("     ==========================")


    opção = str(input("Digite uma opção:")).lower()[0]

    if opção == "s":
        saque = float(input("Valor do saque: "))
        if saque > 500 or cont_saque == 3 or saque > extrato:
            if saque > 500:
                print("excedeu o valor do saque.")

            elif saque > extrato:
                print("excedeu o seu proprio dinheiro.")

            else:
                print("excedeu o numero de saques.")

        elif saque < 0:
            print("Não aceitamos numeros negativos.tente novamente.")

        else:
            cont_saque += 1
            extrato -= saque
            lista_de_acontecimentos.append(f"Saque: {saque:.2f}")

    elif opção == "d":
        deposito = float(input("Deposite o seu valor: "))

        if saque < 0:
            print("Não aceitamos numeros negativos.tente novamente.")

        else:
            extrato += deposito
            lista_de_acontecimentos.append(f"Deposito: {deposito:.2f}")

    elif opção == "e":
        print("==========EXTRATO==========")

        for item in lista_de_acontecimentos:
            print(item)

        print(f"Extrato: {extrato:.2f}")
            

        print("============================")
