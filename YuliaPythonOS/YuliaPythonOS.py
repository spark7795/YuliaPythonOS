import random
import math
############################# Введём количество строк и столбцов
rows=int(input('Num of rows: '))
cols=int(input('Num of cols: '))
max_el=int(input('What matix i will generate? From 1 to: '))
############################# Сгенерируем массив заданного размера
#r=int(input())

mas = []
for i in range(rows):
    mas.append([])
    for j in range(cols):
        r = random.randint(1,max_el)  
        mas[i].append(r)
       
       #mas[i].append(int(input()))
max=0; max_x=0; max_y=0;
min=max_el; min_x=0; min_y=0;
for i in range(rows): 
    for j in range(cols):
        if mas[i][j]>max:
            max=mas[i][j]
            max_x=j
            max_y=i
for i in range(rows): 
    for j in range(cols):
        if mas[i][j]<min:
            min=mas[i][j]
            min_x=j
            min_y=i
############################# Выведем сгенерированный массив
for i in range(rows):
    print(mas[i], "\n")
print("Min num: ", min, "; X: ", min_x, "; Y: ", min_y)
print("Max num: ", max, "; X: ", max_x, "; Y: ", max_y)
print("distance between max&min elems by X:",math.fabs(max_x-min_x), "; By Y: ", math.fabs(max_y-min_y))