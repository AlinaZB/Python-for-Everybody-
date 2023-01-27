score = input("Enter Score:")
sc=float(score)
if sc>1.0:
    print("Error, score is out of range")
    quit()
if sc<0.0:
    print("Error, score is out of range")
    quit()
if sc>=0.9:
    print("A")
    quit()
elif sc>=0.8:
    print("B")
    quit()
if sc>=0.7:
    print("C")
    quit()
if sc>=0.6:
    print("D")
    quit()
if sc<0.6:
    print("F")
    quit()
