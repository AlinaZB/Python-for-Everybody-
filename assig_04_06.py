hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("enter rate:")
r = float(rate)

def computepay(h,r):
    if h<=40:
        pay=h*r
    elif h>40:
        pay=40*r + (h-40)*r*1.5
    return(pay)

p=computepay(h,r)
print('Pay',p)


n=5
while n>0:
    print(n)
    n=n-1
print("Blastoff")
print(n)
