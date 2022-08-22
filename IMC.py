altura = float(input("Qual é a sua altura em cm: "))
peso = float(input("Qual é o seu peso em kg: "))

IMC = peso / (altura / 100) ** 2
print(f"{IMC:.2f}")
if IMC < 18.5:
    print(f"seu IMC é de {IMC:.2f} e é classificado como magreza")

elif IMC >= 18.5 and IMC < 24.9:
    print(f"seu IMC é de {IMC:.2f} e é classificado como normal")

elif IMC >= 25 and IMC < 29.9:
    print(f"seu IMC é de {IMC:.2f} e é classificado como sobrepeso,mas bem pouco não se preocupe!")

elif IMC >= 30 and IMC < 39.9:
    print(f"seu IMC é de {IMC:.2f} e é classificado como Obesidade")

else:
    print("pode parar de comer! comece a malhar pois o negócio esta feio! Obesidade grave")
