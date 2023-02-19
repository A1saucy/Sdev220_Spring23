import unittest

num1=int(2)
num2 = int(4)
num3 = int(6)
num4 = int(1)
num5 = int(2)
num6 = int(3)

list1 = [num1,num2,num3]
list2 = [num3,num4,num5]

x=0 
total =0

while (x<len(list1)):
    total += list1[x]
    x+=1

while (x<len(list2)):
    total += list1[x]
    x+=1

class testSums(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sum([num1,num2,num3]),12,"ERROR,should be 12")





if __name__== "__main__":
    unittest.main()


