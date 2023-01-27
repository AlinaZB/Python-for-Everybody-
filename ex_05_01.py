largest = None
smallest = None

while True:
    numb = input("Enter a number: ")
    if numb == "done":
    	break
    try:
    	num = int(numb)
    except:
    	print("Invalid input")
    	continue
    if smallest is None:
    	smallest = num
    if largest is None:
    	largest = num
    if num > largest:
    	largest = num
    elif num < smallest:
    	smallest = num


print("Maximum is", largest)
print("Minimum is", int(smallest))
