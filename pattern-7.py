'''have to add another j loop to make it work and print a *'''

for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("#",end=" ")
    print()