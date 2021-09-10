
class Solution:
    def reverse(self,arr,low,high):
        while(low<high):
            temp=arr[low]
            arr[low]=arr[high]
            arr[high]=temp
            
            low+=1
            high-=1
        return arr    
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        self.reverse(A,0,D-1)
        self.reverse(A,D,N-1)
        self.reverse(A,0,N-1)
        
        return A
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=1
    
    while(T>0):
        N=5
        D=2
        A=[1,2,3,4,5]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends