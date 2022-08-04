m = float(input('Digite o valor em metros(M): '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m * 0.1
hm = m * 0.01
km = m * 0.001
print('a conversão de {}m \nEm milímetros e igual a {:.0f}mm \nEm centímetros e igual a {:.0f}cm \nEm decímetros e igual a {:.0f}dm.'.format(m, mm, cm, dm))
print('Em decametros e igual a {}dam \nEm hectometros e igual a {}hm \nEm quilometros e igual a {}km'.format(dam, hm, km))