data_dict = {
    'cup':'Ucup Surucup',
    'tong':'Otong Surotong',
    'dung':'Dudung Surudung'
}

#panjang dictionary
lendict = len(data_dict)
print(f'Panjang Dictionary: {lendict}')

# mengecek key exist atau tidak
key = 'cup'
checkkey = key in data_dict
print(f'apakah {key} ada di data_dict: {checkkey}')

# mengakses value (read dengan get)
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis','key tidak ditemukan')) # cek key dengan message

# mengupdate data
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)
data_dict['sep'] = 'asep si kasep'
print(data_dict)

data_dict.update({'cup':'Ucup Surucup'})
print(data_dict)
data_dict.update({'faqih':'faqihza si kweren'}) # update / add jika data tidak ada
print(data_dict)

# mendelete data dari dictionary
del data_dict['faqih']
print(data_dict)