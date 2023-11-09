#Basic - Print all integers from 0 to 150.
for ruben in range(0, 151, 1):
    print(ruben)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for rdo in range(0, 1005, 5):
    print(rdo)

#Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for tdw in range(101):
    if tdw % 5 == 0:
        print("Coding")
    elif tdw % 10 == 0:
        print("Coding Dojo")
    else:
        print(tdw)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for num in range(1, 500000, 2):
    sum += num
print("The sum of odd integers from 0 to is: ", sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
num = 2018
for n in range(num, 0, -4):
    print(n)

#Flexible Counter - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum, mult):
    if i % mult == 0:
        print(i)
