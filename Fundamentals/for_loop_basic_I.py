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
    if tdw % 10 == 0:
        print("Coding Dojo")
    print(tdw)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
max = 500_000
for number in range(1, max + 1, 2):
    sum += number
print("The sum of odd integers from 0 to", max, "is:", sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
number = 2018
while number > 0:
    print(number)
    number -= 4

#Flexible Counter - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for number in range(lowNum, highNum + 1):
    if number % mult == 0:
        print(number)
