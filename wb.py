# Working with MySQL Workbench

import win32crypt
from os import path

fname = "workbench_user_data.dat"

print(fname)

if path.exists:
    print('file exists')

#open file and read data as binary
with open(fname, 'rb') as f:
    data = f.read()

decrypt = win32crypt.CryptUnprotectData( data )

print(decrypt)
