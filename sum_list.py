def sum_(list):
    somma=0
    if list==[]:
        return None
    for item in list:
        somma=somma+item
    return somma
    
list=[1,2,3,4]
somma=sum(list)
print(somma)
