def dfs(image,sr,sc,newColor,prevC):
    if(sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]!=prevC or image[sr][sc]==newColor):
        return
        
    image[sr][sc]=newColor
    dfs(image,sr-1,sc,newColor,prevC)
    dfs(image,sr+1,sc,newColor,prevC)
    dfs(image,sr,sc-1,newColor,prevC)
    dfs(image,sr,sc+1,newColor,prevC)
        
    return image
    
    
def floodFill(image, sr, sc, newColor):
    prevC=image[sr][sc]
    dfs(image,sr,sc,newColor,prevC)
        
    return image
#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

    T=1
    for i in range(T):
        image=[[1,1,1],[1,1,0],[1,0,1]]
        sr, sc, newColor = 1,1,2
        ans = floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()
# } Driver Code Ends