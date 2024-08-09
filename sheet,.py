#Check if a string is a palindrome.
str = "ava"
dstr = str[::-1]
print(dstr)
if str == dstr:
    print("Yes")

#factorial
num = 5
res = 1
for i in range (num, 0, -1):
    res = res * i
print(res)
#or
num = 5
res = 1
for i in range (1, num+1):
    res = res * i
print(res)

#Find largest element
myList = [51,4,3,2,50,1,5,50]
largest = myList[0]
for i in myList:
    if largest < i:
        largest = i
print(largest)

#Frequency of elements
myList = [1,2,2,1,4,55,6,7,7]
frequency = {}

for n in myList:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1
print(frequency)

#Find if Prime
number = 8

def primeCheck(number):
 for i in range  (2, number):
    if number%i == 0:
        return True
        break
    else:
        pass
    
checker = primeCheck(number)
if checker == True:
    print("It is not a prime number")
else:
    print("It is a prime number")

#Find common elements
list1 = [1,2,3,4]
list2 = [1,7,3,5]

comEle = []
for i in list1:
    if i in list2:
        comEle.append(i)
        
print(comEle)

#Remove duplicates from list
myList = [1,1,2,3,4,5,5,6,7,7]
def dupRem(arr):
    uList = []
    for ele in arr:
        if ele not in uList:
            uList.append(ele)
    return uList

print(dupRem(myList))

#Remove duplicates from string
str = "aabcddfs"
new_str = ""

for i in str:
    if i not in new_str:
        new_str += i

print(new_str)
