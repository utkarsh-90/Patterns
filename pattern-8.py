'''p8.py'''

for i in range(5):
    for j in range(i):
        print(' ',end="")
    for j in range(5-i):
        print("*",end=" ")
    print()