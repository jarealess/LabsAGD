import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/env python3

if __name__ == "__main__":

   for line in sys.stdin:
       valor_columna = line.split(',')[2]
       sys.stdout.write("{}\t1\n".format(valor_columna))
