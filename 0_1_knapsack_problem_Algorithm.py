def knapSack(Cap,wt,profit,n):
	K=[[0 for x in range(Cap+1)] for x in range(n+1)]
	for i in range(n+1):
		for w in range(Cap+1):
			if i==0 or w==0:
				K[i][w]=0
			elif wt[i-1]<=w:
				K[i][w]=max(profit[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
			else:
				K[i][w]=K[i-1][w]
	return K[n][w]
if __name__ == '__main__':
    profit = [4,3,6,5]
    weight = [3,2,5,4]
    W = 5
    n = len(profit)
    print(knapSack(W, weight, profit, n))
