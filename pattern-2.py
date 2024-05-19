'''
-The j loop has to add i+1 to use the i loop properly 
-Like in the first iteration i is 0 and j would be 1 so at 0th place one star will be printed. 
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()