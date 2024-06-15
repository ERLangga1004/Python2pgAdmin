import datetime

mahasiswa1 = {
    'nama':'Ucup Surucup',
    'nim':'i.2410161',
    'sksLulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2005, 4, 10)
}

mahasiswa2 = {
    'nama':'Otong Surotong',
    'nim':'i.2210191',
    'sksLulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2001, 1, 1)
}

mahasiswa3 = {
    'nama':'Asep',
    'nim':'i.2310431',
    'sksLulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(1999, 9, 9)
}

dataMahasiswa = {
    'MHS001':mahasiswa1,
    'MHS002':mahasiswa2,
    'MHS003':mahasiswa3
}

print(f'{'KEY':<6} {'Nama':<17} {'nim':<10} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}')
print('-' *  50)

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa

    NAMA = dataMahasiswa[KEY]['nama']
    NIM = dataMahasiswa[KEY]['nim']
    SKS = dataMahasiswa[KEY]['sksLulus']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime('%x')

    print(f'{KEY:<6} {NAMA:<17} {NIM:<10} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}')