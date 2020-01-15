import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == '__main__':

   
    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##

    curkey = None
    total = 0
    prom = 0
    suma = 0

    for line in sys.stdin:
       key = line.split("\t")[0]
       value = line.split("\t")[1]
       value = int(value)
       cant = line.split("\t")[2]
       cant = int(cant)

       if key == curkey:
          suma += value
          total += cant
          prom = suma/total

       else:

            if curkey is not None:
              # prom = (suma/total)
               sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))
            total = cant
            suma = value
            curkey = key

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))       
