def knapSack(W, wt, val, n): 
  
    if n == 0 or W == 0 : 
        return 0
  
     
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
   
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1))
      
///////////////////////////////////////////////////////////////////
val = [1,2,5,6] 
wt = [2,3,4,5] 
W = 8
n = len(val) 
print(knapSack(W, wt, val, n))
