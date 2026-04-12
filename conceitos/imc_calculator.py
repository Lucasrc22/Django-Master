peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = float(peso/(altura **2))
imc = round(imc,2)
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <=24.9:
    print("Peso normal")
elif imc >=25 and imc < 30:
    print("Você está Sobrepeso")
else:
    print("Você está obeso")

print("Seu IMC: "+str(imc))