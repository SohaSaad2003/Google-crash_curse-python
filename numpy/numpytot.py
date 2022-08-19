#2- Write a Python program to check whether a given string contains a capital
# letter, a lower case letter, a number and a minimum length (8).
def check(string):
    x=[]
    
    if not any (i.isupper()for i in string ) :
        x.append("String must have 1 upper case character.")
    if not any (i.islower()for i in string ):
        x.append("String must have 1 lower case character.")
    if not any (i.isdigit()for i in string ):
        x.append("String must have 1 number.")
    if len(string)<8:
        x.append("String length should be atleast 8.")
    if not  x:
        x.append('Valid string.')
    return x
print(check("Myageis18yearsold"))