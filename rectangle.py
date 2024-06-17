def perimeter(l,b):
    p=2*(l+b)
    return p

#print(perimeter(3,4))

def area(l,b):
    a=l*b
    return a
    
l=input("enter length: ")
b=input("enter breadth: ")

print(perimeter(l,b))
print(area(l,b))