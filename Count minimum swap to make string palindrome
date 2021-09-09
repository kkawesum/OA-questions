def countswaps(s,n):
    # s is string ,n is length
    s=list(s)
    swaps=0
    ans=True #boolean ans denotes whether s can be converted into a palindrome
    
    for i in range(n//2):
        left=i
        right=n-left-1
        
        while(left<right):
            
            if s[left]==s[right]:
                break
            else:
                right-=1
                
        if left==right:
            ans=False
            break
        else:
            #swap the middle adj elements
            for j in range(right,n-left-1):
                s[j],s[j+1]=s[j+1],s[j]
                swaps+=1
    if ans:
        return swaps
    else:
        return -1
        
s='aabb'
n=len(s)
print(countswaps(s,n))
    
