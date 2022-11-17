def sum_csv():
    list=[]
    my_file=open('shampoo_sales.csv','r')
    def sum_list(list):
        somma=0
        if list==[]:
            return None
        for item in list:
            somma=somma+item
        return somma
    for line in my_file:
        elements=line.split(',')
        numbers=float(elements)
        date=elements[0]
        value=elements[1]
        list.append(float(value))
    s=sum_list(list)
    return s
print(sum_csv())
