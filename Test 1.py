def checkered():
    m = int(input("Enter the lenght of the checkerboard ="))
    n = int(input("Enter the width of the checkerboard ="))

    Table = []

    for i in range(m) :
        x = []
        y = []
        
        for j in range(n):
            x.append("#")
            x.append("*")
            y.append("*")
            y.append("#")

        Table.append(x)
        Table.append(y)
    
    for i in range(m):
        for j in range(n) :
            print(Table[i][j],end="")
        print()
checkered()