fname = input("Enter file name: ") #The first line prompts the user to enter a file name and stores it in a variable called "fname".
fh = open(fname) # The second line opens the file specified by the "fname" variable and assigns the file handle to the variable "fh".
data=[] # The third line creates an empty list called "data".
for each in fh: # The next lines make up a for loop that iterates over each line in the file specified by the "fh" variable.
    words=each.split() # Inside the for loop, each line is split into a list of words using the .split() method.
    for word in words: # This is followed by another for loop that iterates over the list of words
        if word not in data: # Inside the second for loop, a check is made to see if the current word is already present in the "data" list.
            data.append(word) # If the word is not in the "data" list, it is added to the list using the append() method.
print(sorted(data)) # Finally, the sorted() function is used to sort the "data" list and it is printed.
