def perimeter_reactangle(l,b):
    p=2*(l+b)
    return p

#print(perimeter(3,4))

def area_reactangle(l,b):
    a=l*b
    return a
    
l=input("enter length: ")
b=input("enter breadth: ")

print(perimeter_reactangle(l,b))
print(area_reactangle(l,b))