for i in range(1,5):
    for j in range(1,5):
        if j<= 5-i:
            print(j,end=" ")
    print()

'''
for i in range(1,5):
    for j in range(1,5-i): #here j is not subtracting only 1 but its subtracting 5-i-1
        print(j,end=" ")
    print()

'''
