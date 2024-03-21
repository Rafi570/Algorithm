import sys
n = 4
distan = [
          [0, 22, 26, 30], # A 
          [30, 0, 45, 35], # B
          [25, 45, 0, 60], # C
          [30, 35, 40, 0]  # D
        ] 

# 2^4 - 1 = 15 = binary 1111
allVisitedMask = (1 << n) - 1  

# 2D Array dp
DP = [[-1 for _ in range(n)] for _ in range(2 ** n)]

# TSP function
def TSP(visitedMask, position):
    # base case: All cities have been visited
    if visitedMask == allVisitedMask:
        return distan[position][0]
    
    #  If the result is already calculated, return it
    if DP[visitedMask][position] != -1:
   
        return DP[visitedMask][position]
    
    # Initialize the minimum distance to sys.maxsize
    minDistance = sys.maxsize 

    # Try visiting every unvisited city
    for city in range(n):
     
        if (visitedMask & (1 << city)) == 0:  # 0001 & 0010 = 0000 == 0
            # print(1<<city)
            #   Mark the next city as visited
            newVisitedMask = distan[position][city]  # position = 0, city = 1 , value = 22

            # Calculate the distance after visiting the next city
            newDistance = newVisitedMask  + TSP(visitedMask | (1 << city), city) # 0011 , 1
            # Update the minimum distance
            minDistance = min(minDistance, newDistance)

    # Store and return the minimum distance        
    DP[visitedMask][position] = minDistance
    return minDistance

# Create a dp table and initialize with -1
for i in range(1 << n):
    for j in range(n):
        DP[i][j] = -1
print("Minimum Distance Travelled ->", TSP(1, 0))
