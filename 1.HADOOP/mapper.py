#! /usr/bin/env python

import sys
from operator import itemgetter

if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##

    tup = []
    for line in sys.stdin:
        value = line.split()[0]
        lista = line.split()[1]

        for letra in lista.split(','):
          tup.append((letra, value))

tup2 = sorted([row for row in tup], key = itemgetter(0))

for row in tup2:
    sys.stdout.write("{}\t{}\n".format(row[0], row[1]))
