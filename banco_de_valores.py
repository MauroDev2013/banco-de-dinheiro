cont_saque = 0
LIMITE_SAQUE = 500
extrato = 0


tabela = print("""
==========================
|        BANCO           |
==========================
|   [s]Saque.            |
|   [d]Deposito.         |
|   [e]Extrato.          |
|   [q]Sair.             |
==========================
    """)


opção ========================== str(input("Digite uma opção:")).lower()[0]

while opção != "q":
    if opção = "s":
        saque = float(input("Valor do saque: "))
        if saque > 500 or cont_saque == 3:
            print("excedeu o valor do saque." if saque > 500 else "excedeu o numero de saques.")

