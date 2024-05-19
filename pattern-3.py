'''
the real deal is range() it gives array like functionality but it's not array. it promptly gets needed data not like array which stores data in memory.
'''

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=" ")
    print()