
#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH']='text.txt'

# Complete the isValid function below.
def isValid(s):
    from itertools import count
    import statistics as st

    lista_set=list(set(s))

    lista_count=[s.count(i) for i in lista_set]    

    if len(set(lista_count))>2:
        
        print('NO')
    else:
        
        try:
            moda=st.mode(lista_count)
            if sum(lista_count)/len(lista_count)==moda or (sum(lista_count)+1)/len(lista_count)==moda or (sum(lista_count)-1)/len(lista_count)==moda or (sum(lista_count)-1)/(len(lista_count)-1)==moda:
                print('YES')
                
            else:
                print('NO')
                
        except:
            print('NO')
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(str(result) )

    fptr.close()
