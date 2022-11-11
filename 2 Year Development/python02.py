# Definizione di un metodo che ogni nuovo esercizio, a funzione richiamata, scrive "Exercise (n esercizio)"
def ex(number):
    print('Exercise ' + str(number))


# 1
ex(1)

my_string = 'The quick brown fox jumps over the lazy dog'

# Divide la stringa per ogni parola
words = my_string.split()

my_list = []
for word in words:
    # Se la lunghezza delle singole parole è < 5
    if len(word) < 5:
        # Prendi quella parola
        my_list.append(word)

print(my_list)

# Stessa cosa ma in una riga
words = [word for word in my_string.split() if len(word) < 5]

print(words)


# 2
ex(2)

another_string = 'Ciao come va la vita ALLORA'

# Controlla lettera per lettere nella stringa se ci sono vocali e le trasforma in carattere grande
vowels = [char for char in another_string.upper() if char in 'AEIOU']

print(vowels)


# 3
ex(3)

another_one_string = 'Tutto bene grazie tu invece che mi racconti'

# Conta la lunghezza di ogni parola presente nella frase
word_count = {word: len(word) for word in another_one_string.split()}

print(word_count)


# 4
ex(4)

my_list_of_list = [[1, 3], [7, 9, 4, 6, 8, 9], [15, 2, 89, 4, 0, -9]]

# Somma la lista dei numeri per le liste che sono presenti che contengono più di cinque valori nella lista
list_of_sum_of_list = [sum(list_of_number)
                       for list_of_number in my_list_of_list
                       if len(list_of_number) > 5]

print(list_of_sum_of_list)


# 5
ex(5)

my_dictionary = {'suv': 2000, 'van': 5000, 'bicicletta': 20, 'moto': 10000}

# Nome in grande
vehicles = [name.upper()
            # Per gli oggetti presenti nel mio dizionario (passandogli nome e peso), di cui il peso è < di 5000
            for name, weigth in my_dictionary.items() if weigth < 5000]

print(vehicles)


# 6
ex(6)


# Ritorna il risultato del metodo, passandogli tutti gli argomenti che vogliamo
def my_sum(*args):
    return sum(args)


print(my_sum(1, 2))
print(my_sum(1, 2, 3))


# 7
ex(7)


# Ritorna chiave valore di quello che inseriamo nel print
def my_print(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


my_print(a=3, b=2, c='cane', d='valore')
