print("Início da aula")

#Código de faixas etárias

idade = int(input("Qual sua idade?"))

if idade <= 12 :
    print("Você é criança.")
elif idade < 18 :
    print("Você é adolescente.")
elif idade < 65 :
    print("Você é adulto.")
else:
    print("Você é idoso.")

    # print (10 < 5)
# print(10 > 5)
# print(10 >= 10)
# print(10 <= 10)
# print(10 != 5)
# print(10 != 10)
# print(10 == 10)


idade = int(input("Digite a sua idade:"))

cnh = input("Possui habilitação?(sim/não):")

if idade >= 18 and cnh == "sim":
    print("Você tem permissão para dirigir.")
else :
    print("Você não tem permissão para dirigir.")

    


