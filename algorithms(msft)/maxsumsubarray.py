# also known as Kadane algorithm
#doesnt work when all values are negative

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        max_so_far=a[0]
        max_ending_here=0
        
        for i in a:
            max_ending_here+=i
            if max_ending_here>max_so_far:
                max_so_far=max_ending_here
                
            if max_ending_here<0:
                max_ending_here=0
        return max_so_far
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=1
        while(T>0):
            
            n=5
            
            arr=[1,2,3,-2,5]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends