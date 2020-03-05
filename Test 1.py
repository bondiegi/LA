#10

integer_one = int(input("Enter the first integer: " ))
integer_two = int(input("Enter the second integer: " ))

if integer_one % integer_two == 0:
    print ("It is a multiple")
else:
    print ("It is not a multiple")

#11

count = 1
total = 0

while count <= 5:
    user_input = float(input("Enter number: "))
    total += user_input
    count += 1

print (total)

#12

#range starts from 0 unless a lower limit is placed
#the second number is an upper limit
#range(1,5)=4 numbers not 5

total = 0

for x in range(1,6):
    user_input = float(input("Enter number: "))
    total += user_input

print (total)

#13

count = 0
total = 0

user_input = int(input("Enter integer to be added, Enter -999 to quit: "))

while user_input != -999:
    total += user_input
    count += 1
    user_input = int(input("Enter integer to be added, Enter -999 to quit: "))

print ("The total is :",total)
print ("Number of integers entered :",count)

#14

#15 (while loop)

count = 1
total = 1

print (total)

while count <= 7:
    total += 3
    print (total)
    count += 1

#15 (for loop)
    for x in range (1,23, 3):
    print (x)

#16

#17
total = 0
commission = 0

user_input = float(input("Enter amount of sales,when finished enter -99: "))

while user_input != -99: 
    total += user_input
    commission = total * .10
    print (total)
    print (commission)
    user_input = float(input("Enter amount of sales,when finished enter -99: "))

#18a

x = 2.2567
y = 4
z = 6

print ('The value of x is',(format(x,'.2f')))

#18b

x = 2.2567
y = 4
z = 6

xxx = y + z

print ('The sum of y + z is',xxx)

#18c

x = 2.2567
y = 4
z = 6

xxx = y + z

print (format(x,'.3f'))
print(y)
print(z)

#18d

x = 2.2567
y = 4
z = 6

xxx = y + z

print (format(x,'.3f'),y,z,sep='..')

#19

def stocks ():
    name_of_stock = str(input("Enter the name of the stock: "))
    value_of_stock = float(input("Enter the value of the stock: "))
    number_of_shares = float(input("Enter the number of shares: "))

    total_value = number_of_shares * value_of_stock

    return name_of_stock, total_value
   

def main():
    answer = stocks()
    print (answer)
    
main()

#20

def tax(tax_percentage, dollar_value):
    tax = tax_percentage * dollar_value
    return tax

tax = tax(.10, 100)

print (tax)

#24

def square(integer):
    value = integer ** 2
    return value

square = square(5)
print (square)

#25,26,27

def openFile():
    outfile = open("tuition.txt", 'w')
    name = input("Enter student's name or enter 'exit' to quit: ")
    
    while name != 'exit' :
        outfile.write (name + '\n')
        credit_hours = input("Enter credit hours: ")
        outfile.write (credit_hours + '\n')
        student_type = input("Enter type of student: ")
        outfile.write (student_type + '\n')

        name = input("Enter student's name or enter 'exit' to quit: ")


def readFile():
    infile = open("tuition.txt",'r')
    name = infile.readline().rstrip()
    while name != '':
        credit_hours = infile.readline().rstrip()
        student_type = infile.readline().rstrip()

        if student_type == 'international':
            print ('Name:',name)
            print ('Credit Hours:',credit_hours)
            print ('Student Type:',student_type)
            print ('Tuition:', int(credit_hours) * 47.50)
        else:
            print ('Name:',name)
            print ('Credit Hours:',credit_hours)
            print ('Student Type:',student_type)
            print ('Tuition:', int(credit_hours) * 50)

        name = infile.readline().rstrip()


    infile.close()

def main():
    openFile()
    readFile()

        
main()
