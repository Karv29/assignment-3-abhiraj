#Difference between == and === operator
# 
'''== is used to compare the values of two variables but not its data type and  whereas, === compares the both values as well as data types but it is not available in python instead it contains is operator
a=10
b='10'
(a==b) it will retun true,
(a is b) it will return false'''
#if-Else........pass statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#elif b <a:
 # pass
else:
  print("a is greater than b")
#for loop.......
# range(start,end,stepsize) 
# start	(Optional). An integer number specifying at which position to start. Default is 0
# stop	(Required). An integer number specifying at which position to stop (not included).
# step	(Optional). An integer number specifying the incrementation. Default is 1

x = range(6)
for n in x:
  print(n)
  #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

x1 = range(3, 20, 2)
for n2 in x1:
  print(n2)


  #The break keyword is used to break out a for loop, or a while loop.
  i = 1
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1

  #The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

i1 = 0
while i1 < 9:
  i1 += 1
  if i1 == 3:
    continue
  print(i1)


