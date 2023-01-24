import os
import csv
csvpath = os.path.join( "Resources", "budget_data.csv")

pl = 0
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #lista = list(csvreader)
    rowcount  = 0
#iterating through the whole file
    for row in csvreader:
        rowcount+= 1
#for row in csvreader:
        pl = pl + eval(row[1])
        Promedio = int(pl/rowcount)

numeros = []

#def min_max(numeros):
    #menor = numeros[0]
    #mayor = numeros[0]      

    #for n in numeros:
        #if n < menor:
 #           menor = n 
#
        #if n > mayor:
         #   mayor = n

""" lista = []
for row in lista:     
def mayor(lista):   
max = lista[0]
for x in lista:
if x > max:
    max = x
return max """

#def menor(lista):
    """ min = lista[0]
    for x in lista:
        if x < min:
            min = x
    return min """

txtpath = os.path.join("Analysis", "output.txt")

with open(txtpath, "a") as f:
    f.write("Financial Analysis")
    f.write("\n---------------------------------------------------------------------")
    f.write("\nTotal Months:" + str(rowcount))
    f.write("\nTotal:$"+ str(pl) )
    f.write("\nAverage change:$"+ str(Promedio))
    #f.write("\nGreatest Increase in Profits", mayor(lista))
    #f.write("\nGreatest Decrease in Profits", menor(lista))
    f.close ()


 #printing the result

print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months:"+ str(rowcount))
print("Total:$"+ str(pl) )
print("Average change:$"+ str(Promedio))
#print("Greatest Increase in Profits", mayor(lista))
#print("Greatest Decrease in Profits", menor(lista))
#print(min_max(numeros))



