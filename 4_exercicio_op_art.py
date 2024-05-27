op = ''

while(op!='exit'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Digite o símbolo da operação, ou exit para sair: ")

    if (op == "+"):
        fin = num1 + num2
        print(fin)
    elif (op == "-"):
        fin = num1 - num2
        print(fin)
    elif (op == "*"):
        fin = num1 * num2
        print(fin)
    elif (op == "/"):
        fin = num1 / num2
        print(fin)
    elif (op == "//"):
        fin = num1 // num2
        print(fin)
    elif (op == "%"):
        fin = num1 % num2
        print(fin)
    elif (op == "**"):
        fin = num1 ** num2
        print(fin)
    elif (op == "exit"):
        print("Obrigado por usar!")
    else:
        print("OPERAÇÃO INVALIDA!!")
        print("As operações possíveis são:")
        print("+ Adição\n- Subtração\n* Multiplicação\n/ Divisão\n// Divisão Inteira\n% Resto da divisão")