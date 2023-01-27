name=input("Enter file name:")  #promtp to file name
if len(name)<1: name="mbox-short.txt"  #with enter it will default to my file
text=open(name)

author=dict()

for line in text:
    line.rstrip()
    if not line.startswith("From"): continue
    words=line.split()
    author[words[1]]=author.get(words[1],0)+1

largest=None
largest_author=None

for key in author:
    if largest is None:largest=author[key]

    if largest<author[key]:
        largest=author[key]
        largest_author=key

print(largest_author,largest)
