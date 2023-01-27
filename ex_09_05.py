name=input("Enter file name:")  #promtp to file name
if len(name)<1: name="mbox-short.txt"  #with enter it will default to my file
text=open(name)

di=dict()

for line in text:
    line=line.rstrip()
    wds=line.split()
    for w in wds:
        #idiom:retrieve/create/update counter
        di[w]=di.get(w,0)+1

#now we want to find the most common word
largest=-1
theword=None

for k,v in di.items():
    if v>largest:
        largest=v
        theword=k #capture/remember the word that was the largest

print(theword,largest)
