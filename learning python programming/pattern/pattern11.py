for row in range(6):
    for col in range(7):
        if (row == 0 and col%3!=0) or(row==1 ) or (row==2) or (row-col==2) or (row*col==15) or (row*col==6) or (row*col==9) or (row*col==12) or (row*col==16) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
