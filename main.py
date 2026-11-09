#nama: syamsul rotab bahri
#nim: 2608342

#latihan 1 A
def fibonacci(n, a = 0, b = 1):
    if n == 0:
        print(a)
        return
    else:
        print(a)
        return fibonacci(n-1,b,a+b)

fibonacci(7)

# 0, 1, 1, 2, 3, 5, 8, 13

#latihan 1 B
def volTabung(r, t):
    phi = 3.14
    volume = phi * (r ** 2) * t 
    return volume

print(volTabung(7, 8))

#latihan 1 C
input_angka = []

def nilai_total(*angka):
    total = sum(angka)
    return total

def nilai_rata_rata(*angka):
    total = sum(angka)
    jumlah_angka = len(angka)
    rata_rata = total / jumlah_angka
    return rata_rata

jumlah_angka = int(input('Masukan jumlah angka nya: '))

for i in range(jumlah_angka):
    input_angka.append(int(input(f"Masukan Angka ke {i+1} : ")))
    
print(f"Total : {nilai_total(*input_angka)}")
print(f"Rata-rata : {nilai_rata_rata(*input_angka)}")

#latihan 2
def login():
    kesempatan = 3
    while True:
        password = "Latihan"
        usn = input("masukan usn: ")
        pw = input("masukan pw: ")
        if pw == "Latihan":
            print("anda berhasil login")
            return True
        else:
            kesempatan -= 1
            print(f"kesempatan anda sisa {kesempatan}")
        if kesempatan == 0:
            print("kesempatan sudah habis")
            break
login()


#latihan 3
def konversi_ke_detik(jam, menit, detik):
    return (jam * 3600) + (menit * 60) + detik


def selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_mulai = konversi_ke_detik(jam_mulai, menit_mulai, detik_mulai)
    total_selesai = konversi_ke_detik(jam_selesai, menit_selesai, detik_selesai)

    selisih = total_selesai - total_mulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60

    return jam, menit, detik


# Input dari user
print("=== Waktu Mulai ===")
jam_mulai = int(input("Jam   : "))
menit_mulai = int(input("Menit : "))
detik_mulai = int(input("Detik : "))

print("=== Waktu Selesai ===")
jam_selesai = int(input("Jam   : "))
menit_selesai = int(input("Menit : "))
detik_selesai = int(input("Detik : "))

hasil_jam, hasil_menit, hasil_detik = selisih_waktu(
    jam_mulai, menit_mulai, detik_mulai,
    jam_selesai, menit_selesai, detik_selesai
)
print(f"Selisihnya adalah {hasil_jam} jam - {hasil_menit} menit - {hasil_detik} detik")