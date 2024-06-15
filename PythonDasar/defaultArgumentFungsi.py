def sapa(nama, pesan = 'Apa Kabar?'):
    print(f'Hai {nama}, {pesan}')

sapa('Miku', 'Apa kabarrr?')
sapa('Miku')


# contoh 2
def htg_pangkat(angka, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(htg_pangkat(4))

hasil = htg_pangkat(pangkat = 3, angka = 5)
print(hasil)


# contoh 3

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3 = 10))