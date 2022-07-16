winers = ["soha","basant","noha"]
index=0
for winer in winers :
    index +=1
    print ( index, winer)
#-------------------------------------
winers = ("soha","basant","noha",(1,2,3))

for winer in winers :
    
    print ( winers.index(winer)+1, winer)
print ("=======================================")
#-------------------------------------------
for index,winer in enumerate(winers,start=1):
    #  print ( index+1, winer) # when we use enumerate(winers)
    print ( index, winer)