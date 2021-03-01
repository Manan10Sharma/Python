#Intersect two list
def inter(l1,l2):                   
    l3=[value for value in l1 if value in l2]
    return l3
l1=[4,9,5,8,6,7]
l2=[2,8,3,7,4,6]
print("intersection:-",inter(l1,l2))
