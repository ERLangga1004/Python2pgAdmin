# Penggunaan type Hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''fungsi dengan hints'''
    output = 10 ** argument
    return output

hasil = sepuluh_pangkat(2)
print(hasil)

def display(argument:string):
    print(argument)

display("Miku")