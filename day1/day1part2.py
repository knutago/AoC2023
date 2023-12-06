import regex as re

f = open('day1input.txt','r')
lines = f.readlines()

sum = 0
num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
numlist = list(num_dict.keys())
for line in lines:
    numbers = re.findall(r'(?:\d|'+'|'.join(numlist)+')', line, overlapped = True)
    for el,ind in zip(numbers,range(len(numbers))):
        try:
            numbers[ind] = num_dict[el]
        except:
            pass
    numints = ''.join(numbers)

    digit1 = numints[0]
    digit2 = numints[-1]

    sum1 = int(digit1+digit2)
    print(line,numints,digit1,digit2,sum1)
    sum += sum1
    
print(sum)
