from prettytable import PrettyTable

def fractional_knapsack(value, weight, capacity):
   
    index = list(range(len(value)))
    
    ratio = [v/w for v, w in zip(value, weight)]
    
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value, fractions


def dynamic_prog(capacity, weight, value):
   z=len(value)
   item=[]
   lookup_table = [[0 for x in range(capacity+1)] 
                    for x in range(z+1)] 
  
     
   for i in range(z+1): 
        for w in range(capacity+1): 
            if i==0 or w==0: 
                lookup_table[i][w] = 0
            elif weight[i-1] <= w:
                lookup_table[i][w] = (max(value[i-1] + lookup_table[i-1][w-weight[i-1]], lookup_table[i-1][w]))
            else: 
                lookup_table[i][w] = (lookup_table[i-1][capacity])

   res=lookup_table[z][capacity]
   print("The maximum value of knapsack is:", res)

   x=capacity
   for i in range(z,0,-1):
       if res<=0:
           break
       if res==lookup_table[i-1][x]:
           continue
       else:
           z=i
           item.append(z)
           res = res - value[i - 1] 
           x = x - weight[i - 1]
   print("The items you can choose are")
   table_dynamic=PrettyTable(["Item"])
   for x in range(0,len(item)):
       table_dynamic.add_row([item[x]])
   print(table_dynamic)
       


print("WE CAN HELP YOU DECIDE WHAT TO CARRY IN YOUR BAGS")
print('**************************************************\n')

n = int(input('Enter number of items you wish to carry: '))
value = input('On a scale of 1-{} what are the items worth to you? (Write in order i.e, 1st(item) 2nd 3rd ...): '.format(n)).split()
value = [int(v) for v in value]
weight = input('Enter the weights of the {} item(s) (in order) (g): '.format(n)).split()
weight = [int(w) for w in weight]
weight_threshold = int(input('Enter maximum weight that your airlines can allow (g): '))
bag_wt=int(input('Enter weight of your bag (g): '))
capacity=weight_threshold - bag_wt

item_total=[]
for i in range(1,n+1):
    item_total.append(i)

print("\nYour entries are")
table_wt_val=PrettyTable(["Item","Weight","Value"])
for x in range(0,n):
    table_wt_val.add_row([item_total[x],weight[x],value[x]])
print(table_wt_val)

max_value, fractions = fractional_knapsack(value, weight, capacity)
print("\n*****************************")
print("ACCORDING TO GREEDY ALGORITHM")
print('The maximum value of items that can be carried:', max_value)
print('The fractions in which the items should be taken are')
table_dynamic=PrettyTable(['Item','1=full weight'])
for y in range(0,n):
    table_dynamic.add_row([item_total[y],fractions[y]])
print(table_dynamic)

print("*********************************\n")
print("*********************************")
print("ACCORDING TO DYNAMIC PROGRAMMING")
dynamic_prog(capacity, weight, value)
print("*********************************")
