def sum_csv(my_file):
    list=[]
    my_file=open(my_file,'r')
    for line in my_file:
        elements=line.split(',')
        date=elements[0]
        value=elements[1]
        if date!='Date':
            list.append(float(value))
    if len(list)==0:
        return None
    s=sum(list)
    return s
shampoo_sales='shampoo_sales.csv'
print(sum_csv(shampoo_sales))
