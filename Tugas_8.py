from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# input batas
batas = int(input("Masukkan batas : "))

# Inisialisasi fungsi
def cetak(i):
    a = i + 1
    if a % 2 == 1:
       print(a, "Ganjil - ID proses", getpid())
    else:
       print(a, "Genap - ID proses", getpid())
    sleep(1)

# 1. Pemrosesan Sekuensial
print("- Pemrosesan Sekuensial -")

# Untuk mendapatkan waktu sebelum eksekusi
sekuensial_awal = time()

# Proses berlangsung
for i in range(batas):
    cetak(i)

# Untuk mendapatkan waktu setelah eksekusi
sekuensial_akhir = time()
print("")

# 2. Multiprocessing dengan kelas Process
print("- Multiprocessing dengan kelas Process -")

# Untuk menampung proses-proses
kumpulan_proses = []

# Untuk mendapatkan waktu sebelum eksekusi
process_awal = time()

# Proses berlangsung
for i in range(batas):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

# Untuk menggabungkan proses-proses agar tidak loncat ke proses sebelumnya
for i in kumpulan_proses:
    p.join()

# Untuk mendapatkan waktu setelah eksekusi
process_akhir = time()
print("")

# 3. Multiprocessing dengan kelas Pool:
print("- Multiprocessing dengan kelas Pool -")

# Untuk mendapatkan waktu sebelum eksekusi
pool_awal = time()

# Proses berlangsung
pool = Pool()
pool.map(cetak, range(batas))
pool.close()

# Untuk mendapatkan waktu sebelum eksekusi
pool_akhir = time()
print("")
print("-"*50)

# Bandingkan waktu eksekusi
print("Perbandingan waktu eksekusi")
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool:", pool_akhir - pool_awal, "detik")
