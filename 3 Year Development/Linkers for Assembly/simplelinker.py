from pelinker import Executable
import sys

exe = Executable(image_base=0x500000)

text = exe.add_section('.text', 'rx')
text.content = open(sys.argv[1], 'rb').read()

data = exe.add_section('.data', 'rw')
data.content = b'ciao\0hello\0'

exe.export_symbol('helloworld', 0x1000)
exe.export_symbol('foobar', 0x1004)

exe.import_symbols('user32.dll', ['MessageBeep', 'MessageBoxA'])
exe.import_symbols('kernel32.dll', ['ExitProcess'])

exe.entry_point = text.rva

open(sys.argv[2], 'wb').write(exe.link())
