teman_teman = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dudung surudung',
    'sep':'asep si kasyep',
    'cuy':'ucuy surucuy'
}

friends = teman_teman.copy()

'''Jika tanpa copy makan value dari friends dan
teman_teman akan sama-sama berubah, 
jika memakai COPY maka hanya salah satu saja yang berubah/terupdate'''

teman_teman['cup']='ucup si kwerwn'
print(f'teman_teman: {teman_teman}\n')
print(f'friends: {friends}\n')

# pop dictionary (berdasarkan key)
dataAsep = friends.pop('sep')
print(f'data asep = {dataAsep}\n')
print(f'friends = {friends}\n')

# popitem dictionary (berdasarkan item terakhir)
dataTerakhir = friends.popitem()
print(f'data terakhir = {dataTerakhir}\n')
print(f'friends = {friends}\n')