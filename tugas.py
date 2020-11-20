data = ['', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']


def terbilang(a):

    if a < 10:
        return data[a]
    elif a >= 1_000_000_000:
        return terbilang(a // 1_000_000_000) + ' billion ' + (terbilang(a % 1_000_000_000) if a % 1_000_000 != 0 else '')
    elif a >= 1_000_000:
        return terbilang(a // 1_000_000) + ' million ' + (terbilang(a % 1_000_000) if a % 1_000_000 != 0 else '')
    elif a >= 1_000:
        if a // 1_000 == 1:
            return " one thousand " + (terbilang(a % 1_000) if a % 1_000 != 0 else '')
        else:
            return terbilang(a // 1_000) + " thousand " + (terbilang(a % 1_000) if a % 1_000 != 0 else '')
    elif a >= 100:
        if a // 100 == 1:
            return ' one hundred ' + (terbilang(a % 100) if a % 100 != 0 else '')
        else:
            return terbilang(a // 100) + ' hundred ' + (terbilang(a % 100) if a % 100 != 0 else '')
    elif a >= 20:
        if a//10 == 2:
            return 'twenty ' + (terbilang(a % 10) if a % 10 != 0 else '')
        elif a//10 == 3:
            return 'thirty ' + (terbilang(a % 10) if a % 10 != 0 else '')
        elif a//10 == 5:
            return 'fifty ' + (terbilang(a % 10) if a % 10 != 0 else '')
        elif a//20 == 8:
            return 'eighty ' + (terbilang(a % 10) if a % 10 != 0 else '')
        else:
            return terbilang(a // 10) + ('ty' if (a // 10) != 8 else 'y') + terbilang(a % 10)
    else:
        if a == 10:
            return 'ten'
        elif a == 11:
            return 'eleven'
        elif a == 12:
            return 'twelve'
        elif a == 13:
            return 'thirteen'
        elif a == 15:
            return 'fifteen'
        elif a == 18:
            return 'eighteen'
        elif a == 19:
            return 'nineteen'

import os
while True:
    os.system('cls')
    try:
        a = int(input('masukkan angka = '))
        print(f'{a:,} = {terbilang(a)}')
    except:
        print('inputan anda salah')
    os.system('pause')