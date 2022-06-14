print("Practice 3. Standart modules")

import math
import statistics
import random

print("List output")
list_math = [82,8,23,97,92,44,17,39,11,12]
print(list_math)
print('')

print("Total sum")
res_sum = math.fsum(list_math)
print(res_sum)
print('')

print("Awerage")
res_mean = statistics.mean(list_math) 
print(res_mean)
print('')

print("Median")
res_median = statistics.median(list_math) 
print(res_median)
print('')

print("Standart bias")
res_stdev = statistics.stdev(list_math) 
print(res_stdev)
print('')

print("Random generation")
rnadom_int = random.randint(1, 100)
print(rnadom_int)
