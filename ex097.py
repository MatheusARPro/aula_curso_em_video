#funções
def escreva(txt):
    tamanho_texto = len(txt) + 4
    print("-" * tamanho_texto)
    print(f'  {txt}  ')
    print("-" * tamanho_texto)


#codigos
escreva('ola,mundo!')
escreva('O gato roeu a roupa do rei de Roma!')
escreva('Em Roma a roupa do rei o gato roeu!')
escreva('CURSO EM VIDEO')