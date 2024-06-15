# *args artinya argumen

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",120,120)

# Studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

hasil = tambah(10,5,15)
print(f'Hasil = {hasil}')