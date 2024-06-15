# Template
''' def nama_fungsi(argument):
        badan fungsi
        return output
'''

# fungsi kuadrat

def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(3)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah
def tambah(angka_1, angka_2):
    return angka_1 + angka_2

hasil_tambah = tambah(10,8)
print(hasil_tambah)

# fungsi dengan return banyak
def operasi_mtk(angka_1, angka_2):
    tambah_2 = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah_2, kurang, kali, bagi

k,l,m,n = operasi_mtk(9, 6)

print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')
