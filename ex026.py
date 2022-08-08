frase = input('Digite uma frase: ').upper()

print(f'''Total de letras "A" : {frase.count("A")}
Primeira letra "A" : {frase.find("A")}
Ultima letra "A" : {frase.rfind("A")}''')
