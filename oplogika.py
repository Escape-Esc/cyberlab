#operasi logika atau boolean
# ada , not, or, xor,

print("===NOT===")
a = True #jika ini true hasil data c akan false/kebalikannya
c = not a
print("data a =", a)
print("----------------- NOT")
print("data c =",c)

#OR jika salah satu true, maka hasilnya true
print("===OR===")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b,"=",c)
a = True
b = False
c = a or b
print(a,"OR",b," =",c)
a = True
b = True
c = a or b
print(a,"OR",b," =",c)

#AND jika salah satu False, maka hasilnya False. jika true and true hasilnya True
print("===AND===")
a = False
b = False
c =  a and  b
print(a,"AND",b,"=",c)
a = False
b = True
c =  a and  b
print(a,"AND",b,"=",c)
a = True
b = False
c = a and  b
print(a,"AND",b," =",c)
a = True
b = True
c = a and b
print(a,"AND",b," =",c)

#XOR akan true jika salah satu true, sisanya False, jika ada dua True akan False
print("===XOR===")
a = False
b = False
c =  a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c =  a ^ b
print(a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = True
c = a ^ b
print(a,"XOR",b," =",c)