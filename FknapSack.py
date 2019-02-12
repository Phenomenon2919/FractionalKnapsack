import operator
'''
* The declaration of variables that are going to hold the values of
* Profits, Weights and the calculated Densities for the objects
'''
profit = []
weight = []
density = {}

'''
* Taking the inputs in order,
* 1) The number of objects
* 2) The values of weight and profit corresbonding for each object
* 3) The values of densities of all objects are calculated from their corresponding profits and weights
* 4) The capacity of the Bag
'''
N = input("Enter the number of objects: ")
for i in range(N):
	weight.append(input("Enter the weight of object no. "+str(i+1)+": "))
	profit.append(input("Enter the profit of object no. "+str(i+1)+": "))
	density[i] = float(profit[i])/float(weight[i])
M = input("Enter the Capacity of Bag: ")

#Sorting the object number and their densities in descending order of their density values
density = sorted(density.items(), key=operator.itemgetter(1), reverse=True)

solution = {}		#Stores the fractions of the objects in the solution
capacity = M		#Stores the current capacity of the bag, reduces with inclusion of each item
final_profit = 0	#Stores the final profit of the solution
left = N 			#Stores the object number of the last object thet could not be include whyole in the solution

#loop to include the objects whose whole fraction can included in the bag
for i in range(len(density)):
	if weight[density[i][0]] > capacity:
		left = density[i][0]
		break
	else:
		solution[density[i][0]] = 1
		capacity -= weight[density[i][0]]
		final_profit += profit[density[i][0]]

#To include the fraction of the left object
if left < N:
	solution[left] = float(capacity)/float(weight[left])
	final_profit = final_profit + solution[left]*profit[left]

#printing the results
print "The fractions of objects included in the bag are: "
for x in solution.keys():
	print "For part ",x+1," fraction = ",solution[x]

print "The final profit produced = ",final_profit


