import struct
import sys

with open(sys.argv[1], 'rb') as handle:
    data = handle.read()

offset = 0

while offset < len(data):
    header = data[offset:offset+512]
    offset += 512
    print(header[124:124+11])
    size = int(header[124:124+11], 8)
    aligned_size = (size // 512) * 512 
    if size % 512 != 0:
        aligned_size += 512
    content = data[offset:offset+size]
    print(content)
    offset += aligned_size
