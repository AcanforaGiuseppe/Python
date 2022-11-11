# Dichiarazione di una classe
class Vector(list):

    # Metodo repr che ritorna il vettore passato con la scritta 'Vector("VETTORE PASSATO")'
    def __repr__(self):
        # super() sta ad indicare la classe base
        return 'Vector(' + super().__repr__() + ')'

    def __add__(self, other):
        # Ricerca il tipo dell'item passato
        self.__check_type(other)

        # for x in self:
        #     print(x)
        # for i in range(len(self)):
        #     print(f'{i}: {self[i]} - {other[i]}')
        # for self1, other1 in zip(self, other):
        #     print(self1, '-', other1)

        # Unisce insieme x1 e x1, x2 e x2 grazie alla funzione "zip", unendo i due valori che gli passiamo e ritornando un vettore
        return Vector(x1 + x2 for x1, x2 in zip(self, other))

    # Stessa cosa della funzione di sopra, ma somma anche i valori passati
    def __mul__(self, other):
        self.__check_type(other)
        return sum(x1 * x2 for x1, x2 in zip(self, other))

    def __check_type(self, other):
        # Se la lunghezza del primo oggetto che gli passiamo è diversa dalla seconda del secondo oggetto:
        if len(self) != len(other):
            # Innalza eccezzione
            raise TypeError('Vector can only be added to sequences of the same lenght')


my_vector = Vector([1.5, 2, 3])
print(repr(my_vector))

other_vector = Vector([5, 9, 11.2])

list_from_vector = [1.5, 2, 3]

# Vettore creato per creare una classe con i valori che abbiamo passato
vector = Vector([1.5, 2, 3])
