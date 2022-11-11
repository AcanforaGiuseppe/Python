# La dichiarazione del tipo della variabile non è necessaria
my_var = 1

# Le parentesi risultano inutili in questo linguaggio
# if
if my_var == 1:
    # print(thing to print)
    print(1)
# Nuovo costrutto else + if
elif my_var == 2:
    print(2)
else:
    print("something else")

print("hello")

# while
# "and", "or", "not" sono operatori logici che si scrivono così come sono, come "True" e "False"
while my_var < 10 and True or False:
    print(my_var)
    my_var += 1
    # Tutto quello indentato con 4 spazi davanti fa parte del costrutto


while not my_var == 10:
    print(my_var)
    my_var += 1

# is
print(my_var is my_var)

# Importazione libreria (di solito ad inizio file)
import math

print(math.pi)
print(math.sin(math.pi / 2))

# Importare solo il necessario dalla libreria
from math import sin
# Rinominazione di una cosa importata dalla libreria math grazie ad "as"
from math import pi as PI

print(PI)
print(sin(PI / 2))

# Definizione metodi
#  def my_func(x: int, y: int) -> int:
def my_func(x=1, y=2):
    print(x, y)
    return x + y


print(my_func(1, 2))


def my_func_without_return():
    print("hello")


print(my_func_without_return())  # Ritorna none
print(my_func(1, 2))
print(my_func())
print(my_func(2))
print(my_func(y=3, x=4))  # 7


# Nuova classe "MyCustomException", classe figlia di Exception
class MyCustomException(Exception):
    # "pass" non fa nulla
    pass

# Chiamata ad un'eccezione con un messaggio
# raise MyCustomException("This is a custom exception")


x = 1
# "assert" viene utilizzato in fase di testing
assert x == 1, "x is not 1"

# Eliminazione variabile con "del"
del x

# "try" "except" come prova di risoluzione di un codice
try:
    print(x)
except Exception as e:
    print(e)

# lambda
my_lambda_func = lambda x, y: x + y + 1


def my_func(x, y):
    return x + y + 1


my_return = my_lambda_func(1, 2)
print(my_return)


def my_func(x, y):
    z = 10

    def my_second_func():
        # Definizione di una nuova variabile all'interno di un metodo, inclusa solo in quel metodo
        nonlocal z
        z = 16
        return z

    my_second_func()
    return x + y + 1


my_string = "ciao"
my_list = [1, 2, 3, 3, 4]

# Lunghezza di variabili
len(my_string)
len(my_list)


# my_string[0] = "d"
my_string = "d" + my_string[1:]  # "iao"
print(my_string)
# Operazioni con una lista
my_list = list(my_string)  # ['c', 'i', 'a', 'o']
my_list.pop(0)  # 'c' |      'i' | 'a' | 'o'  O(n)  O(1)
my_list[0] = "d"
my_list[1] = "a"
my_string = ",".join(my_list)  # "d, a, a, o"
my_string = "".join(my_list)  # "daao"
del my_list[1]

# Tuple
my_tuple = (0, )
my_tuple = 0, 
my_tuple = (0)  # This is not a tuple, only a 0


def my_function():
    return (1, 2)


my_tuple = my_function()
x, y = my_function()

# in
if 1 in my_tuple:
    print("1 is in my_tuple")
else:
    print("1 is not in my_tuple")

# Altre operazioni con la lista
my_unsorted_list = [10, 340, 324, 21, 34, 1, 54, 33, 923]
my_unsorted_list.sort()
print(my_unsorted_list)
my_unsorted_list.reverse()
print(my_unsorted_list)
my_sorted_list = sorted(my_unsorted_list)
my_reversed_list = reversed(my_unsorted_list)

# range
range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(2, 10)  # [2, 3, 4, 5, 6, 7, 8, 9]
range(2, 10, 2)  # [2, 4, 6, 8]

# Utilizzo del for
for i in range(10):
    print(i)

for i in range(len(my_unsorted_list)):
    print(i)

for element in my_sorted_list:
    print(element)

for i, element in enumerate(my_sorted_list):
    print(i, element)

for i, element in enumerate(my_sorted_list, 5):
    print(i, element)


from collections import defaultdict

# Dictionary
my_dict = {"ciao": []}
my_dict["ciao"].append(1)

my_dict["cane"] = []
my_dict["cane"].append(10)

my_new_dict = defaultdict(list)
my_new_dict["nuova"].append(11)

my_dict_of_ints = defaultdict(int)
my_dict_of_ints["cane"] += 1
