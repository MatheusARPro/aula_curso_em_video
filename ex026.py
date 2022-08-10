frase = str(input('Digite uma frase: ')).upper().strip()

print(f'''Total de letras "A" : {frase.count("A")}
Primeira letra "A" na posição : {frase.find("A")+1}
Ultima letra "A" na posiçao : {frase.rfind("A")+1}''')
