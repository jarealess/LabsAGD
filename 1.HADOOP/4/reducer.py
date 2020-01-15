import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from operator import itemgetter
import time, datetime

if __name__ == '__main__':

    tup = []

    for line in sys.stdin:
        letter = line.split("\t")[0]
        fecha = line.split("\t")[1]
        fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime('%Y-%m-%d')
        value = line.split("\t")[2]
        tup.append((letter, fecha, value))

tup2 = sorted([row for row in tup], key = itemgetter(1))  

for row in tup2:
      key, date, value = row[0], row[1], row[2]     
      sys.stdout.write("{}\t{}\t{}\n".format(key, date, value))
