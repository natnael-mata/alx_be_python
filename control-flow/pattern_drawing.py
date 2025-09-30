#pattern drawing
length = int(input("Enter the size of the pattern: "))
raw=0
while raw<length:
    for size in range(0,length):
        print("*", end="")
    print()
    raw+=1
