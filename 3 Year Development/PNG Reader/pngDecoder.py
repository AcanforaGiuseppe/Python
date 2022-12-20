import struct
import zlib


class PngDecoder:
    def decode(self, filepath):
        file = open(filepath, 'rb')
        png_signature = b'\x89PNG\r\n\x1a\n'
        if (file.read(len(png_signature)) != png_signature):
            raise PngDecoder.InvalidSignatureException(png_signature)

        chunks = []
        while True:
            chunk_type, chunk_data = self.__read_chunk(file)
            chunks.append((chunk_type, chunk_data))

            if chunk_type == b'IEND':
                break

        self.__process_chunks(chunks)
        return (bytes(self.reconstructed_data), self.width, self.height)

    def __read_chunk(self, file):
        chunk_length, chunk_type = struct.unpack('>I4s', file.read(8))
        chunk_data = file.read(chunk_length)
        checksum = zlib.crc32(chunk_data, zlib.crc32(
            struct.pack('>4s', chunk_type)))
        chunk_crc, = struct.unpack('>I', file.read(4))
        if chunk_crc != checksum:
            raise PngDecoder.ChecksumFailedException(chunk_crc, checksum)
        return (chunk_type, chunk_data)

    def __process_chunks(self, chunks: list):
        _, IHDR_data = chunks[0]
        self.width, self.height, bit_depth, color_type, compression_m, filter_m, interlace_m = struct.unpack('>IIBBBBB', IHDR_data)

        if compression_m != 0:
            raise PngDecoder.InvalidCompressionException

        if filter_m != 0:
            raise PngDecoder.InvalidFilterException

        if color_type != 6:
            raise PngDecoder.InvalidColorTypeException(color_type)

        if bit_depth != 8:
            raise PngDecoder.InvalidBitDepthException

        if interlace_m != 0:
            raise PngDecoder.InvalidInterlaceMethodException

        IDAT_data = b''.join(chunk_data for chunk_type, chunk_data in chunks if chunk_type == b'IDAT')
        IDAT_data = zlib.decompress(IDAT_data)
        self.__build_data(IDAT_data)

    def __build_data(self, IDAT_data):
        self.reconstructed_data = []
        self.bytes_per_pixel = 4
        self.stride = self.width * self.bytes_per_pixel
        i = 0

        for r in range(self.height):
            filter_type = IDAT_data[i]
            i += 1
            for c in range(self.stride):
                filter_x = IDAT_data[i]
                i += 1
                if filter_type == 0:    # None
                    reconstructed_x = filter_x
                elif filter_type == 1:  # Sub
                    reconstructed_x = filter_x + self.__reconstruct_a(r, c)
                elif filter_type == 2:  # Up
                    reconstructed_x = filter_x + self.__reconstruct_b(r, c)
                elif filter_type == 3:  # Average
                    reconstructed_x = filter_x + \
                        (self.__reconstruct_a(r, c) +
                         self.__reconstruct_b(r, c)) // 2
                elif filter_type == 4:  # Filters
                    reconstructed_x = filter_x + self.__choose_filter(self.__reconstruct_a(r, c), self.__reconstruct_b(r, c), self.__reconstruct_c(r, c))
                else:
                    raise PngDecoder.InvalidFilterException('unknown filter type: ' + str(filter_type))
                self.reconstructed_data.append(reconstructed_x & 0xff)

    def __choose_filter(self, a, b, c):
        p = a + b - c
        pa = abs(p-a)
        pb = abs(p-b)
        pc = abs(p-c)
        if pa <= pb and pa <= pc:
            pres = a
        elif pb <= pc:
            pres = b
        else:
            pres = c
        return pres

    def __reconstruct_a(self, r, c):
        return self.reconstructed_data[r * self.stride + c - self.bytes_per_pixel] if c >= self.bytes_per_pixel else 0

    def __reconstruct_b(self, r, c):
        return self.reconstructed_data[(r-1) * self.stride + c] if r > 0 else 0

    def __reconstruct_c(self, r, c):
        return self.reconstructed_data[(r-1)*self.stride + c - self.bytes_per_pixel] if r > 0 and c >= self.bytes_per_pixel else 0

    class PngDecoderException(Exception):
        def __init__(self, message):
            self.message = message

    class InvalidSignatureException(PngDecoderException):
        def __init__(self, signature, message='Invalid PNG signature'):
            self.message = message
            print(f'File signature is: {signature}')

    class ChecksumFailedException(PngDecoderException):
        def __init__(self, crc, checksum):
            self.message = f"Chunk checksum failed {crc} != {checksum}"

    class InvalidCompressionException(PngDecoderException):
        def __init__(self):
            self.message = 'Invalid compression method'

    class InvalidFilterException(PngDecoderException):
        def __init__(self, message='Invalid filtering method'):
            self.message = message

    class InvalidColorTypeException(PngDecoderException):
        def __init__(self, color_type):
            self.message = f'Color type {color_type} is not supported'

    class InvalidBitDepthException(PngDecoderException):
        def __init__(self):
            self.message = 'Only a bit depth of 8 is supported'

    class InvalidInterlaceMethodException(PngDecoderException):
        def __init__(self):
            self.message = 'There is no interlacing support'
