def main():
        x=input()
        y=convert(x)
        print(y)


def convert(t):
         t=t.replace(":)","🙂")
         t=t.replace(":(","🙁")
         return t
main()
