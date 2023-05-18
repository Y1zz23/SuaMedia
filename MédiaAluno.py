nota1 = float(input("Digite a 1 nota: "))
nota2 = float(input("Digite a 2 nota: "))
media = (nota1 + nota2)/2
if media < 5:
    print("Infelizmente voce reprovou")
elif media >= 5 and media <=6.99:
    print("Recuperação")
else:
    print("Aprovado, Parabéns !!!")
print("Sua média foi {}".format(media))
    