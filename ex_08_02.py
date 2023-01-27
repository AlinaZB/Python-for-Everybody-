fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

data=[]
for line in fh:
    if line.startswith("From") and len(line.split())>2:
        tem=line.split()
        data.append(tem[1])
for line in data:
    print(line)

print("There were", count, "lines in the file with From as the first word")
