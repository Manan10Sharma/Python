#print symbol A by stars
for i in range(7):
    for j in range(5):
        if (j==0 or j==4) or (i==0 or i==3) and (j>0 and j<4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
print("program finished...  \n\nfor print A by stars(*)")
