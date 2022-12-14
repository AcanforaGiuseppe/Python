import struct
import sys
import zlib

with open(sys.argv[1], 'rb') as handle:
    data = handle.read()

eocd_offset = data.rfind(b'PK\x05\x06')
print(eocd_offset, hex(eocd_offset))

records, = struct.unpack('<H', data[eocd_offset+8:eocd_offset+8+2])

print('records:', records)

cd_size, cd_offset = struct.unpack('<II', data[eocd_offset+12:eocd_offset+12+8])

print('central directory offset:', cd_offset, hex(cd_offset))
print('central directory size:', cd_size, hex(cd_size))

offset = cd_offset
for i in range(0, records):
    compressed_size, uncompressed_size = struct.unpack('<II', data[offset+20:offset+20+8])
    filename_len, extra_len, comment_len = struct.unpack('<HHH', data[offset+28:offset+28+6])
    # print(filename_len, extra_len, comment_len)
    data_offset, = struct.unpack('<I', data[offset+42:offset+42+4])
    local_filename_len, local_extra_len = struct.unpack('<HH', data[data_offset+26:data_offset+26+4])
    record_data_offset = data_offset + 30 + local_filename_len + local_extra_len
    compression, = struct.unpack('<H', data[data_offset+8:data_offset+8+2])
    clean_data = data[record_data_offset:record_data_offset+compressed_size]
    print(compression)
    if compression != 0:
        clean_data = zlib.decompress(clean_data, -15)
    print(data[offset+46:offset+46+filename_len], '@', hex(data_offset), compressed_size, uncompressed_size, clean_data)
    offset += 46 + filename_len + extra_len + comment_len
