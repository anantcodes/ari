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

# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
#first lab toy problem
