from math import radians, sin, cos, tan

ang = float(input('Qual o valor do angulo: '))
seno = sin(radians(ang))
print('O angulo {} tem o SENO de {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print ('O angulo {} tem o cosseno de {:.2f}'.format(ang, coss))
tang = tan(radians(ang))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(ang, tang))