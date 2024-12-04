# tuple with expId, weight, value
items = [(1, 8, 1500), (2, 7, 1600), (3, 6, 1700), (4, 5, 1800), (5, 4, 3000)]

# separate arrays for expId, weight, value
expId = [x[0] for x in items]
weight = [x[1] for x in items]
value = [x[2] for x in items]

weightLimit = 20    # weight limit
n = len(value)      # number of items (5)

totalWeight = weightLimit   # used to calc total weight in knapsack
selectedExp = []    # used to find selected experiences at the end

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
            # weight[i] > weightLimit
            else:   
                # case 2
                dp[i][j] = dp[i - 1][j]



def findSelectedExp():
    global totalWeight
    global selectedExp
    for i in range(n, 0, -1):   # start, stop, step (incremement backwards -> 5, 4, 3, 2, 1)
        # check if value at [i][totalWeight] != prev row -> means item is included
        if dp[i][totalWeight] != dp[i - 1][totalWeight]:
            selectedExp.append(expId[i - 1])  # include this item's experience ID
            totalWeight -= weight[i - 1]    # update the total weight (remove included item)

# call function to populate table
populateKnapsackTable() 
# call function to find selexted experiences
findSelectedExp()

# find & print max enjoyment points -> dp[5][20]
maxEnjPts = dp[n][weightLimit]
print("Maximum enjoyment points:", maxEnjPts)
# print total weight in the knapsack
print("Total weight:", weightLimit - totalWeight)
# print selected experiences
print("Chosen Experiences:", selectedExp)
