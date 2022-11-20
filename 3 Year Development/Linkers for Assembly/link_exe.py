from pelinker import Executable
import sys

exe = Executable(image_base=0x500000)

text = exe.add_section('.text', 'rx')
text.content = open(sys.argv[1], 'rb').read()

exe.import_symbols('aiv01.dll', ['boh'])

exe.entry_point = text.rva

open(sys.argv[2], 'wb').write(exe.link())