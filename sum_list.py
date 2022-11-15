def sum_list(list):
    somma=0
    if list==[]:
        return None
    for item in list:
        somma=somma+item
    return somma
    
list=[]
somma=sum_list(list)
print(somma)
