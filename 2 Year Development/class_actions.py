# Dichiarazione di una classe
class MyClass:

    # Inizializzazione di 3 variabili della classe
    def __init__(self, name, health):
        # self = "this"
        self.name = name
        self.health = health

    def __str__(self):
        # Per poter utilizzare i nomi delle variabili all'interno delle parentesi graffe, si inserisce "f" prima dell'inizio della stringa
        return f"{self.name} has {self.health} health"

    def __repr__(self):
        return f"MyClass('{self.name}', {self.health})"


my_class = MyClass('John', 100)
my_class_str = str(my_class)
print(my_class)
print(my_class_str)
print(repr(my_class))

MyClass('John', 100)


class List:

    def __init__(self, *args):
        self.items = list(args)

    def __bool__(self):
        return len(self.items) > 0
