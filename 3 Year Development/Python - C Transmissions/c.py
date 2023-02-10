import sys

class Pippo:
    def __init__(self):
        print("Ciao")

    def __del__(self):
        print("Reference")

def function():
    a = 0
    b = 1
    c = 2
    print(locals())
    print(globals())

p0 = Pippo()
p1 = p0
p2 = p1
p4 = p0

print(globals())
print(locals())
function()

p0 = None
p1 = None
p2 = None
lista = [p4]
p4 = None

print("End")
sys.pippo = ["Test"]
print(sys.__dict__)