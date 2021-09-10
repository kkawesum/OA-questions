
class Solution:
    def increment(self, arr, N):
        arr[N-1]+=1
        carry=0
        arr[N-1]=arr[N-1]%10
        print('initially',carry)
        for i in range(N-2,-1,-1):
            if carry==1:
                arr[i]+=1
                carry=arr[i]/10
                arr[i]=arr[i]%10
        if carry==1:
            arr.insert(0,1)
        return arr
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = 1
    for _ in range (t):
        N=3
        arr=[1, 2, 4]
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends