for row in range(5):
    for col in range(5):
        if (row==4) or (col==0) or (row-col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")