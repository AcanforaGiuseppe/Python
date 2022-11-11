#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME

nome = "Giuseppe"
cognome = "Acanfora"

################################################################################

# ----------------------------------- EX. ------------------------------------ #
"""
Esercizio: 15 punti

Si scriva una funzione ex1(query, file_db, k) che prende in ingresso una
tupla query, file_db che punta ad un file di testo, mentre k e' un
intero. query e' una tupla (x, y) che indica le coordinate del punto di
query. Invece file_db contiene punti 2D su ogni riga. Ogni riga
contiene le coordinate intere x e y separate da uno spazio, come ad
esempio:

  -5 -5
  10 5

La funzione deve leggere il contenuto del file. Dato il punto query, si
deve cercare gli indici dei k punti piu vicini al punto query in file_db.
Per la distanza fra (x1, y1) e (x2, y2) si usi:
(x1-x2)² + (y1-y2)²

Ad esempio, se k=2 e query=(-5, -5) e file_db contiene:

  1 1
  -3 -5
  -5 -3
  20 10

gli indici e le distanze di file_db rispetto al punto query sono:

 | indice |  x |  y | dist |
 |      0 |  1 |  1 | 72   |
 |      1 | -3 | -5 | 4    |
 |      2 | -5 | -3 | 4    |
 |      3 | 20 | 10 | 850  |

I due vicini al punto query sono la lista [2, 1] in quanto hanno le k=2 distanze
minori.  In caso di parita' sulla distanza, come in questo caso, si
ritornano gli indici dal piu grande al piu piccolo.

Si ritorni la lista che contiene i k indici vicini come sudetto.
Se in ingresso abbiamo query=(-5, -5) e db_00.txt e k=2, si deve ritornare:

 [2, 1]

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""

# INSERISCI QUI IL TUO CODICE
def ex1(query, file_db, k):
  query = (-5, -5)
  firstNumber = query[0]
  secondNumber = query[1]
  file_db = open("db_00.txt")
  arr = file_db.readlines()
  for item in arr:
    if item.__contains__(' '):
      diction1 = item.split().index(0)
      diction2 = item.split().index(1)
    res = calculate(firstNumber, secondNumber, diction1, diction2)
    # Print them all
    print(f"indice: {item.index()}, | x: {diction1} | y: {diction2} | dist: {res}")
    minimum = min(res)
  print(f"Value near k{k}: [{minimum}]")
  file_db.close()


  def calculate(query1, query2, firstNumber, secondNumber):
    calc = (query1 - firstNumber)^2 + (query2 - secondNumber)^2
    return calc


###############################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
