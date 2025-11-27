nmr1 = float(input("Qual o primeiro número? ")) 
nmr2 = float(input("Qual o segundo número? ")) 
opc = str(input("Qual a operação? (+, -, * ou /)")) 

if opc == "+":
    print (f"A soma é: {nmr1 + nmr2}") 

elif opc == "-":
    print (f"A subtração é: {nmr1 - nmr2}") 

elif opc == "/":
    if nmr2 == 0: print("Não é possível dividir por zero!") 
    else:
        print(f"A divisão é: {nmr1 / nmr2}") 

elif opc == "*":  
    print (f"A multiplicação é: {nmr1 * nmr2}") 
    
else: print ("Operação inválida!")