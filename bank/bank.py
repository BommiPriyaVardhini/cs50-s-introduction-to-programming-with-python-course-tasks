def main():
    g=input("Greeting: ")
    g=g.strip()
    if(g.startswith("Hello")):
        print("$0")
    elif(g.startswith("H")):
        print("$20")
    else:
        print("$100")
main()
