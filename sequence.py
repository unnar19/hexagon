n = int(input("Enter the length of the sequence: ")) # Do not change this line
result = 1
tala1 = 1
tala2 = 2
tala3 = 3

for i in range(1,n+1):
    if result <= 3:
        print(result,end=', ')
        result += 1
    else:
        result = tala1 + tala2+ tala3
        tala1 = tala2
        tala2 = tala3
        tala3 = result
        print (result, end=', ')
