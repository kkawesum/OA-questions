
class Solution:
    def pushZerosToEnd(self,arr, n):
        count=0#count of non 0's
        
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[count]=arr[count],arr[i]
                count+=1
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = 5
        arr = [3, 5, 0, 0, 4]
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends