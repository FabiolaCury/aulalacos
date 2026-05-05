   
print("Início da aula")

#1exercicio : Código de faixas etárias

idade = int(input("Qual sua idade?"))

if idade <= 12 :
    print("Você é criança.")
elif idade < 18 :
    print("Você é adolescente.")
elif idade < 65 :
    print("Você é adulto.")
else:
    print("Você é idoso.")

#2exercicio: booleano
    # print (10 < 5)
# print(10 > 5)
# print(10 >= 10)
# print(10 <= 10)
# print(10 != 5)
# print(10 != 10)
# print(10 == 10)

#3exercicio: and
idade = int(input("Digite a sua idade:"))

cnh = input("Possui habilitação?(sim/não):")

if idade >= 18 and cnh == "sim":
    print("Você tem permissão para dirigir.")
else :
    print("Você não tem permissão para dirigir.")


#alteracao 3 exercicio: and
idade = int(input("Digite a sua idade:"))

cnh = input("Possui habilitação?(sim/não):")

toxicológico = input("Exame toxicológico (positivo/negativo):")

if idade >= 18 and cnh == "sim" and toxicológico == "negativo" :
    print("Você tem permissão para dirigir.")
else :
    print("Você não tem permissão para dirigir.")

#4exercicio: or

estudante = input("Você é estudante? (sim/não):")
idoso = input("Você é idoso? (sim/não): ")

if estudante == "sim" or idoso == "sim" :
    print("Você ganhou desconto!")
else :
    print("Você não tem direito a desconto.") 


#5exercício
condicao_fisica = input("Condição física é boa?(sim/não) :  ")
atestado_medico = input("Tem atestado médico?(sim/não) : ")
idade = int(input("Qual sua idade?"))

if idade >= 18 and (condicao_fisica or atestado_medico == "sim"):
    print("Você está aprovado!")
else :
    print("Você está reprovado.")
