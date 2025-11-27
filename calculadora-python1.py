# Calculadora simples em Python

# Lê o primeiro número informado pelo usuário
nmr1 = float(input("Qual o primeiro número? "))

# Lê o segundo número informado pelo usuário
nmr2 = float(input("Qual o segundo número? "))

# Lê a operação desejada (+, -, * ou /)
opc = input("Qual a operação? (+, -, * ou /) ")

# Verifica qual operação foi escolhida
if opc == "+":
    # Soma os dois números
    print(f"A soma é: {nmr1 + nmr2}")

elif opc == "-":
    # Subtrai o segundo número do primeiro
    print(f"A subtração é: {nmr1 - nmr2}")

elif opc == "/":
    # Verifica se o segundo número é zero antes de dividir
    if nmr2 == 0:
        print("Não é possível dividir por zero!")
    else:
        # Realiza a divisão normalmente
        print(f"A divisão é: {nmr1 / nmr2}")

elif opc == "*":
    # Multiplica os dois números
    print(f"A multiplicação é: {nmr1 * nmr2}")

# Caso a operação digitada não seja nenhuma das previstas
else:
    print("Operação inválida!")
