##
#Author: Nishanth C N
#17/05/2017
##

import time

#Initialization and inputs

number_ip = input("Enter number: ")
start_time = time.time()    ##Execution time
n = int(number_ip)
i = 2

#Solution Loop

while i * i < n:        ## since squared the number of searches is exponentially decreased
    while n % i == 0:   ## this condition enables to check if it divides the given number
        n = int(n / i)  ## this condition gets through only if the number is divisible by the iterator 
    i = i + 1
    
for x in range(2, n-1): ## This loop checks for cases like even square numbers are involved and returns the highest prime factor
    if n%x==0:
        n = int(n/x)

print("The highest prime HCF of given number is: ", n)

##printing total execution time

print("--- %s seconds ---" % (time.time() - start_time))
