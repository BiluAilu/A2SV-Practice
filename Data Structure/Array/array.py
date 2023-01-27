class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.arr=arr
        self.capacity=4
        self.length=0
        # write your code here
   
    def insertEnd(self, value):
        if(self.length<self.capacity):
            self.arr[self.length]=value
            self.length+=1

        # write your code here
       
    def removeEnd(self):
        if self.length>0:
            self.arr[self.length]=0
            self.length-=1
        else:
            print("The array is already empty")
        # write your code here
   
    def insertMiddle(self, index, value):
        if self.length<self.capacity:
            
        # write your code here, you need to shift elements after insertion
       
    def removeMiddle(self, index):
        # write your code here, you need to shift elements after removal
   
    def printArr(self):
        print(self.arr)
        # write your code here
