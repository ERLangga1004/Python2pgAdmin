# Ltihan Fungsi

import os

# Pogram untuk menghitung luas dan keliling persegi panjang

# membuat header program
# os.system('cls')
# print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
# print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
# print(f'{'-'*40:^40}')

# # Mengambil input User
# LEBAR = int(input('Masukan nilai lebar: '))
# PANJANG = int(input('Masukan nilai panjang: '))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # Tampilkan Hasil
# print(f'Hasil perhitungan luas = {LUAS}')
# print(f'Hasil perhitungan keliling = {KELILING}')

def header():
    # Header
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    LEBAR = int(input("Masukan nilai lebar: "))
    PANJANG = int(input("Masukan nilai panjang: "))
    return LEBAR, PANJANG

def hitung_luas(LEBAR, PANJANG):
    '''fungsi luas'''
    return LEBAR*PANJANG

def hitung_keliling(LEBAR, PANJANG):
    '''fungsi keliling'''
    return 2*(LEBAR+PANJANG)

def display(message, value):
    '''fungsi display'''
    print(f"{message}, {value}")

while True:
    header()

    print("=== Menghitung ===")
    print("[1] Hitung Luas")
    print("[2] Hitung Keliling")
    opsi = input("Piluh Menu> ")
    
    LEBAR, PANJANG = input_user()

    if opsi == '1':
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)
    elif opsi == '2':
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)
   
    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == 'n':
        break

print("Program Selesai, Terima kasih!")