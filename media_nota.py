#Calculadora de Média Escolar, você tem duas provas, se a média das duas for maior ou igual a 7
# é aprovado por média, mas se o aluno tive média abaixo de 7 e maior ou igual a 3, ele vai para a final
# precisando tirar a diferença para dar 10, caso seja média menor de 3, ele reprova direto

av1 = float(input("AV1: "))
av2 = float(input("AV2: "))

media = float((av1+av2)/2)
media = round(media,2)
if media >= 7:
    print("Parabéns, foi aprovado com média: "+str(media))
elif media<7 and media >=3:
    result = 10 - media
    final = float(input(("Você foi para a Final, precisando de "+str(result)+" para ser aprovado, Digite sua nota da final: ")))
    if final >= result:
        print("Aprovado na final")
    else:
        print("Reprovado")
else:
    print("Reprovado")