import re

f = open('day1input.txt','r')
lines = f.readlines()

sum = 0
for line in lines:
    numbers = ''.join(re.findall(r'\d',line))
    digit1 = numbers[0]
    digit2 = numbers[-1]

    print(line,numbers,digit1,digit2)
    sum1 = int(digit1+digit2)
    sum += sum1
    
print(sum)
