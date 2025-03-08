total_belanja = float(input("Masukan total belanja :"))

if (total_belanja > 100000):
    diskon = 0.10
elif (total_belanja > 50000):
    diskon = 0.05
else :
    diskon = 0

    total_belanja = total_belanja - (total_belanja * diskon)

    total_setelah_diskon = total_bayar
    print(f"Total yang harus dibayarkan setelah diskon : Rp {total_setelah_diskon: .2f}")