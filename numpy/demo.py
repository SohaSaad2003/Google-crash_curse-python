class find_pair:
    def __init__(self ,arr,target):
        self.arr = arr
        self.target = target 
    def pair_num(self):
        for i in range (0,len(self.arr)-1):
            for j in range (i+1,len(self.arr)):
                if self.arr[i]+self.arr[j]==self.target:
                    print (f"the Output {i} and {j}")
  
arr=[10,20,10,40,50,60,70]
target = 50
pair1=find_pair(arr,target)
pair1.pair_num()

       
            