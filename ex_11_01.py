import re # imports the regular expression library
hand=open('regex_sum_42.txt')
numlist=[]

for line in hand:
    line=line.rstrip()
    integers=re.findall('([0-9]+)',line)

    for number in integers:
        numlist.append(int(number))

print(sum(numlist))
