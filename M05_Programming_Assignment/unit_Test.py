import unittest


num1=int(2)
num2 = int(4)
num3 = int(6)
num4 = int(1)
num5 = int(2)
num6 = int(3)

#sum of first three nums
sum = num1 + num2 + num3

#print(sum)
#print("")

# first three nums inserted into a list
list1 = [num1, num2, num3]

# last three nums inserted into a list
list2 = [num4, num5, num6]

###############################################

#for loops to add the numbers in the list
x = 0
total = 0
#print(list1)
#print("")
while (x<len(list1)):
    total = total + list1[x]
    x+=1
#print(total)

while (x<len(list2)):
    total = total + list1[x]
    x+=1

#unit testing the lists
def sumTest():
    # the first test is to check if the sum is not 12 to throw an error
    assert(list1)!=12,"sum is 12"
    assert(list2)==12,"error, sum is 12"

#gaurd statement to print if the unit test came back good
if __name__ == "__main__":
    sumTest()
    print("I finally invented something that works")