def sum_list(list):
    somma=0
    if list == []:
        return none
    for item in list:
        somma=somma+item
    return somma
list=[1,2,3,4]
somma=sum_list(list)
print(somma)
