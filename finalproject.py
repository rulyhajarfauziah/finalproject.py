

while True:
    print("\nPilih opsi")
    print("1. Hitung Luas Persegi Panjang")
    print("2. Hitung Luas Lingkaran")
    print("3. Hitung Fungsi X")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":

        p = float(input("Masukkan nilai panjang: "))
        l = float(input("Masukkan nilai lebar :"))

        hasil_luas = p*l
        print("Luas Persegi Panjangnya adalah :",hasil_luas)

    elif pilihan == "12":

        phi = 3.14
        r = int(input("Masukkan nilai jari-jari: "))
        hasil_luas_lingkaran = phi*r*r
        print("Luas lingkaran adalah :",hasil_luas_lingkaran)
        
    elif pilihan == "3":
        def fungsiku (x):
            return (2*x*x)+(3*x)-10

        x = int(input("Masukkan nilai x :"))

        hasil_fx = fungsiku(x)
        print ("Hasilnya F(x) adalah",hasil_fx)
    else:
        print("Anda hanya boleh memilih opsi 1, 2 atau 3")
        break
