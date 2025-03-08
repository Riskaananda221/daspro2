tahun_kabisat = int(input("Masukan tahun :"))
if(tahun_kabisat % 4 == 0 and tahun_kabisat % 100 != 0) or (tahun_kabisat % 400 == 0):
    print(f"{tahun_kabisat} adalah tahun kabisat")
else:
    print(f"{tahun_kabisat} bukan tahun kabisat" )

