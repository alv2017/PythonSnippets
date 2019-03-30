import win32crypt

# path to file
fpath = "workbench_user_data.dat"
#open file and read data as binary
with open(fpath, 'rb') as f:
    data = f.read()
#decrypt data
decrypt = win32crypt.CryptUnprotectData( data )

print(decrypt)
