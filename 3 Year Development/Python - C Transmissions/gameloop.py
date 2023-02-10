import pyaiv

print("Enter")

x = 0
y = 0

def tick():
    global x,y
    print("Tick")
    x += 1
    y += 1
    print(pyaiv.move(x,y))