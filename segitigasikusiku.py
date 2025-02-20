alas = int(input("Masukan alas segitiga siku-siku :"))
tinggi = int(input("Masukan tinggi segitiga siku-siku :"))

luas = 0.5*alas*tinggi
hipotenusa = (alas*2 + tinggi**2)**0.5
keliling = alas+tinggi+hipotenusa

print("luas segitiga adalah :,",luas)
print("keliling adalah :,", keliling)
