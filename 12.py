
path="C:/Users/OM/Desktop/n1/paste.txt" 
with open(path,"w") as file:
    file.write(" Nile river\n")
    file.write(" Amazon forest")

with open(path, "a") as file:
    file.write(" Fine")
    file.write(" Do some water intake\n")

with open(path,"r") as file:
    print("write and append:")
    print(file.read())
