altura = float(input('Altura (m): '))
peso = float(input('Peso(Kg): '))


altura2 = altura * altura
imc = peso / altura2

print('%'*30)
print(f'IMC : {imc:.3f}')
if imc < 18.5:
    print('Status de IMC: Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Status de IMC: Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Status de IMC: Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Status de IMC: Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')
print('%'*30)
