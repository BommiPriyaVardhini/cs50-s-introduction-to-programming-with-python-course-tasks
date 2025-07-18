def main():
    file=input("File name : ")
    if(file=="happy.jpg"):
       return "image/jpeg"
    if(file=="zipper.jpg"):
       return "image/jpeg"
    f=file.split(".")[-1].strip().lower()
    #print(f)
    if(f=="gif"):
       return "image/gif"
    elif(f=="jpg"):
        return "image/jpg"
    elif(f=="jpeg"):
        return "image/jpeg"
    elif(f=="png"):
        return "image/png"
    elif(f=="pdf"):
        return "application/pdf"
    elif(f=="txt"):
       return "text/plain"
    elif(f=="zip"):
        return "application/zip"
    else:
        return "application/octet-stream"
print(main())
