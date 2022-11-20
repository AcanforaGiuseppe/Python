from pelinker import SharedLibrary
import sys

lib = SharedLibrary()

text = lib.add_section('.text', 'rx')
text.content = open(sys.argv[1], 'rb').read()

lib.export_symbol('boh', text.rva)

open(sys.argv[2], 'wb').write(lib.link())