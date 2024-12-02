# tuple with expId, weight, value
items = [(1, 8, 1500), (2, 7, 1600), (3, 6, 1700), (4, 5, 1800), (5, 4, 3000)]

# separate arrays for expId, weight, value
expId = [x[0] for x in items]
weight = [x[1] for x in items]
value = [x[2] for x in items]

weightLimit = 20    # weight limit
n = len(value)      # number of items (5)

# knapsack table is 21 x 5 (dp starts as a bunch of 0's)
dp = [[0 for x in range(weightLimit + 1)]for x in range(n + 1)]

# function to populate the knapsack table
def populateKnapsackTable():
    # (1 - 6)
    for i in range(1, n + 1):
        # (1 - 21)
        for j in range(1, weightLimit + 1):
            # if weight[i] is <= weightLimit
            if weight[i - 1] <= j:  
                # case 1: k(i,j) is in optimal subset
                # case 2: k(i,j) is not in optimal subset
                # max(case 2, case 1)
                dp[i][j] = max(dp[i - 1][j], value[i - 1] + dp[i - 1][j - weight[i - 1]])
            else:
                # else case 1
                dp[i][j] = dp[i - 1][j]
 

# call function to populate table
populateKnapsackTable() 

# find & print max enjoyment points -> dp[5][20]
maxEnjPts = dp[n][weightLimit]
print("Maximum enjoyment points (value):", maxEnjPts)

