# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = float(input("digite velocidade em Km/h: "))
if km > 60:
    print("a velocidade", km, " é maior que 60")
print(" voce levara multa R$" , km * 7)
else:
    print(" a velocidade" ,km, "é menor que 60")