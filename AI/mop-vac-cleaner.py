row =int(input("Enter the size of row : "))
col=int(input("Enter the size of column : "))
room = [[0 for j in range(col)] for i in range(row)]
i=0
while i<row:
    print("Row",i+1,":")
    if i%2==0:
        for j in range(col):
            if room[i][j]==0:
              room[i][j]=1
              print(room[i])
    else:
        for j in range(-1,(col*-1)-1,-1):
            if room[i][j]==0:
                room[i][j]=1
                print(room[i])
    i+=1
    print()
print("After cleaning the room:")
print(room)
