lista = []
with open('in.txt') as file:
    lista = [int(x) for x in file]

dic_freq = set([0])


i = 0
soma = 0
while(True):
    if( i ==  len(lista)):
            i=0
    soma += lista[i]

    if ( soma in dic_freq ):
        print(soma)
        break
    else:
        i+=1
        dic_freq.add(soma)


