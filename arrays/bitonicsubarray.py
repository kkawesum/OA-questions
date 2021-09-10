def maxbitonic(arr,n):
    inc=[1]*n
    dec=[1]*n


# filling up increasing array from left to right
    for i in range(1,n):
        if(arr[i]>=arr[i-1]):
            inc[i]=inc[i-1]+1
    print(inc)

# filling up dec array from right to left

    for i in range(n-2,-1,-1):
        if(arr[i]>=arr[i+1]):
            dec[i]=dec[i+1]+1
    print(dec) 

#max length bitonic subarray will be the max value of (inc[i]+dec[i]-1)

    biton=inc[0]+dec[0]-1
    for i in range(n):
        biton=max(biton,inc[i]+dec[i]-1)
    return biton



if __name__=="__main__":

    arr = [12, 4, 78, 90, 45, 23]
    n=6

    print(maxbitonic(arr,n))