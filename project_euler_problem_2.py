##
#Author: Nishanth C N
#15/05/2017
##

##Execution time

import time
start_time = time.time()

##initialization

fib_n_1 = 0
fib_n_2 = 1
fib_new = 0
fib_end = 4000000
fib_even_sum = 0

##loop to execute the solution to sum all the even numbered fibonacci numbers within 4mil

while(fib_new<fib_end):
    fib_new = fib_n_1 + fib_n_2
    if(fib_new%2 == 0):
        fib_even_sum += fib_new
    fib_n_1 = fib_n_2
    fib_n_2 = fib_new

    ##print(fib_new)##can print if needed to see the fibonacci numbers

##printing the output sum
    
print("final_even_sum: ", fib_even_sum)

##printing total execution time

print("--- %s seconds ---" % (time.time() - start_time))
