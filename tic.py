# Write your code here :-)
a = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    print("|", end="")
    for j in range(3):
        print(a[i][j], end="|")
    print()

moves=[0,1,2,10,11,12,20,21,22]

for k in range(5):
    player_move = input("Choose the position in which you want to mark X: ")
    print()
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(a[i][j], end="|")
        print()



