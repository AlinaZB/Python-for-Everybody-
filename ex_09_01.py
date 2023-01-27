counts= dict()
names= ['alina', 'filip', 'boris', 'iva', 'elena', 'iva', 'elena']
for name in names:
    counts[name]= counts.get(name,0)+1
print(counts)
