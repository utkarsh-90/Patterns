def item():
    for i in range(0,5):
        for j in range(0,5-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()

def rev_Item():
    for i in range(0,5):
        for j in range(i):
            print(" ",end="")
        for j in range(0,5-i):
            print("*",end=" ")
        print()


item()
rev_Item()