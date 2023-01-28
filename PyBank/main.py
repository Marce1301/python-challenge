import os
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")
pl = 0
lista=[]
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    rowcount  = 0
#iterating through the whole file
    for row in csvreader:
        lista.append(int(row[1]))
        rowcount+= 1
        pl = pl + eval(row[1])
        Promedio = int(pl/rowcount)

#getting greatest increase and decrease 
def mayor(lista):
    maximum = lista[0]
    for number in lista:
        if number > maximum:
            maximum = number
    return maximum

def menor(lista):
    minimun = lista[0]
    for number in lista:
        if number < minimun:
            minimun = number
    return minimun

#Calling the output .txt file
txtpath = os.path.join("PyBank","Analysis","output.txt")

#write the results in an output .txt file
with open(txtpath, "a") as f:
    f.write("\nFinancial Analysis")
    f.write("\n---------------------------------------------------------------------")
    f.write("\nTotal Months:" + str(rowcount))
    f.write("\nTotal:$"+ str(pl) )
    f.write("\nAverage change:$"+ str(Promedio))
    f.write("\nGreatest Increase in Profits" + str(mayor(lista)))
    f.write("\nGreatest Decrease in Profits" + str(menor(lista)))
 
 #printing the result
print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months:"+ str(rowcount))
print("Total:$"+ str(pl) )
print("Average change:$"+ str(Promedio))
print("Greatest Increase in Profits" + str(mayor(lista)))
print("Greatest Decrease in Profits"+ str(menor(lista)))




