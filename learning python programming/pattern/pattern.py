for row in range(5):
    for col in range(5):
        if (row == 0 )or(row-col==0)or(row == 1 and col ==4)or(row == 2 and col ==4)or(row == 3 and col ==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
