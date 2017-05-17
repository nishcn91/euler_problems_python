##
#Author: Nishanth C N
#15/05/2017
##

##Execution time

import time
start_time = time.time()

##Initialization

set = range(1000)
sum_mul_3 = 0
sum_mul_5 = 0
sum_mul_15 = 0
tot_sum = 0

##Loop to execute the solution

for x in set:
    if x%3 == 0:
        sum_mul_3 +=x
    elif x%5 == 0:
        sum_mul_5 +=x
    elif x%15 == 0:
        sum_mul_15 +=x
tot_sum = sum_mul_3 +sum_mul_5 - sum_mul_15       

##Printintg the output sum

print("tot_sum", tot_sum)

##printing total execution time

print("--- %s seconds ---" % (time.time() - start_time))
 
    
  
    
