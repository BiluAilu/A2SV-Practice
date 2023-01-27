class Solution:

    # def flip(self, a:List[int])->List[int]:
    #     return a.reverse()
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # '''
        # [3,2,4,1]
        # [4,2,3,1]
        # [1,3,2,4]

        # [1,4,2,3]
        
        # '''
        # k=[]
        # m=len(arr)
        # i=0
        # arr1=arr
        # while sorted(arr[0:m])==arr[0:m] and i<10*len(arr):
        #    if(arr.index(max(arr[0:m]))==0):
        #        k.append(len(arr))
        #     else:
        #         k.append(arr.index(max(arr)))
        #    x=flip(arr[:k])
        #    for i in range(len(x)):
        #        arr[i]=x[i]
            
        #     if 
            
                


        #    i+=1
        # return arr
        l=len(arr)
        k=[]
        for i in range(l):
            maxI=max(arr[:l-i])
            max_index=arr.index(maxI)+1
            arr[:max_index]=reversed(arr[:max_index])
            k.append(max_index)
            
            arr[:l-i]=reversed(arr[:l-i])
            k.append(l-i)
        return k
         