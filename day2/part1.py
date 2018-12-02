import string
    
dois = 0
tres = 0
with open('in.txt') as file:
    for line in file: 
        dic_letras = {}
        for char in line:
            if (char in dic_letras):
                dic_letras[char]+=1
            else:
                dic_letras[char] = 1
        dois_usado = False
        tres_usado = False
        for key,value in dic_letras.items():
            if value == 2 and not dois_usado:
                dois+=1
                dois_usado = True
            if value == 3 and not tres_usado:
                tres+=1
                tres_usado = True

print(dois*tres)

