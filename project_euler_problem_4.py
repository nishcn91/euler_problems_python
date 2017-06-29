##
#Author: Nishanth C N
#29/06/2017

import time

#initialization and inputs
start_time = time.time()    ##Execution time
pal_list= []

#solution loop
for x in range(10000,998002):       ##since we know its a product of two 3 digit numbers this could be min and max range
    x = str(x)                      ##convert so that comparison is not possible in integer
    if(x == x[::-1]):                 ##checking the reverse of numbers
       pal_list.append(x)          ##adding the palindrome to the list
print("The highest palindrome number resulted from product of two 3 digit nmumbers is: ")
print(pal_list[-1])                 ##printing the last value since that would be the highest value


##printing total execution time
print("--- %s seconds ---" % (time.time() - start_time))


    
