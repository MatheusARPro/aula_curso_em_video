continua = True
while continua:
    numero = int(input('Digite um numero: '))
    if numero <= 1 and numero % 2 == 0:
        print('Este número não pode ser PRIMO.')
    else:
        primo = False
        for numero_indice in range(2, numero):
            if numero % numero_indice == 0:
                ...  # É a mesma coisa de "pass"
            else:
                primo = True
        if primo is True:
            print('Com certeza este número é primo.')
        else:
            print('Este número não é primo.')
    continuar = int(input("Quer continuar? Digite 0 para sim e 1 para não: "))
    if continuar == 1:
        continua = False
