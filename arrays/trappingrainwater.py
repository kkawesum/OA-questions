


class Solution:
    def trappingWater(self, arr,n):
        res=0
        lmax=[]
        lmax.append(arr[0])
        
        for i in range(1,n):
            lmax.append(max(arr[i],lmax[i-1]))
        
        rmax=[0]*n
        
        rmax[n-1]=arr[n-1]
        
        for i in range(n-2,-1,-1):
            rmax[i]=max(arr[i],rmax[i+1])
        print('lmax',lmax)
        print('rmax',rmax)    
        for i in range(1,n-1):
            res+=min(lmax[i],rmax[i])-arr[i]
            
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=1
        while(T>0):
            
            n=6
            
            arr=[3,0,0,2,0,4]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends