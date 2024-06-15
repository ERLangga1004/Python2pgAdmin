# fungsi dengan argumen

def hello_wordl(nama): 
    # menerima input dari variable nama
    print(f'Selamat Datang di Dunia wahai {nama}')

hello_wordl('Miku')# bisa diisi apa saja!
hello_wordl('Ichika')

def tambah(angka_1, angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(99,1)
tambah(75,25)

def say_hi(list_peserta):
    # fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'Yang terhormat {peserta}')

anggota_boyband = ['Ucup', 'Otong', 'Dudung']
anggota_girlband = ['Miku', 'Nino', 'Itsuki']

say_hi(anggota_girlband)