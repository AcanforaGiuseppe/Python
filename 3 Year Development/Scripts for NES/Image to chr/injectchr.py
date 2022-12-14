import sys

with open(sys.argv[1], 'rb') as handle:
    data = bytearray(handle.read())

with open(sys.argv[2], 'rb') as handle:
    chr_data = handle.read()

if data[0:4] != b'NES\x1A':
    raise Exception('Invalid cartridge')

prg_num = data[4]
chr_num = data[5]

index = int(sys.argv[3])

offset = 16 + (prg_num * 0x4000) + (index * 0x1000)

data[offset:offset+0x1000] = chr_data

with open(sys.argv[1], 'wb') as handle:
    handle.write(data)