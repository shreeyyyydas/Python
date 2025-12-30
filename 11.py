# Make sure sample.txt exists in the same directory or provide full path
with open ("texts.txt","w") as file:
    file.write("Who are you?\n")
    file.write("I am a carbon based organism")
# Using read()
with open("texts.txt", "r") as file:
    print("Using read():")
    print(file.read())
    
# Using readline()
with open("texts.txt", "r") as file:
    print("\nUsing readline():")
    print(file.readline())
    
# Using readlines()
with open("texts.txt", "r") as file:
    print("Using readlines():")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
