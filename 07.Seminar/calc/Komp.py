def parse(data):

    data = data.replace(" ", "")
    for n, x in enumerate(data):
        if x == "+" or x == "-":
            data_real = data[:n]
        elif x == "i":
            data_complex = data[len(data_real)+1:len(data)-1]
    return float(data_real), float(data_complex)
            
def mult(data1, data2):
    list1 = parse(data1)
    list2 = parse(data2)

    real =  list1[0] * list2[0] - list1[1] * list2[1] 
    complex =  list1[0] * list2[1] + list2[0] * list1[1]

    return f'{real} + {complex} * i'

def sum(data1, data2):
    list1 = parse(data1)
    list2 = parse(data2)
    real =  list1[0] +  list2[0]
    complex =  list1[1] + list2[1]
    return f'{real} + {complex} * i'
   
def sub(data1, data2):
    list1 = parse(data1)
    list2 = parse(data2)
    real =  list1[0] -  list2[0]
    complex =  list1[1] - list2[1]
    return f'{real} + {complex} * i'

def div(data1, data2):
    list1 = parse(data1)
    list2 = parse(data2)
    real =  list1[0] +  list2[0]
    complex =  list1[1] + list2[1]
    return f'{real} + {complex} * i'

