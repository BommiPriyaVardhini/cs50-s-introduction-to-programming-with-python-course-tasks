def main():
    a=input("Expression: ")
    x,y,z=a.split()
    x=int(x)
    z=int(z)
    if(y=="+"):
        return float(x+z)
    elif(y=="-"):
        return float(x-z)
    elif(y=="*"):
        return float(x*z)
    elif(y=="/" and z!=0):
        return float(x/z)
print(main())
