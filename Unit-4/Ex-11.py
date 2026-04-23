with open("FILE.txt","w") as file:
    file.write("MIT-ADT=MIT-Arts Design And Technology.\n")
    file.write("Yajat kapoot is going to Farm.\n")
    file.close()
with open("FILE.txt","r") as file:
    f=file.read()
    print(f)
    file.close()
with open("FILE.txt","a") as file:
    file.write("Again a new line.")
    file.close()