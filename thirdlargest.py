def thirdLargest(a, n):
    first=a[0]
    second=0
    third=0
        
    if n<3:
        return -1
            
    for i in range(1,len(a)):
        if a[i]>first:
            third=second
            second=first
            first=a[i]
            
        elif a[i]>second:
            third=second
            second=a[i]
            
        elif a[i]>third:
            third=a[i]
    return(third)
#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = 1
    for i in range(t):
        n = 5
        arr = [2,4,1,3,5]
        print(thirdLargest(arr, n))
# } Driver Code Ends