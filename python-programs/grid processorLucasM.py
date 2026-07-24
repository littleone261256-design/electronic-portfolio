#ml.grid.processer.py
#Mary Lucas
#June 20. 2026
# To generate a 10x10 grid of random numbers and to calculate the total and the average and the difference of the grid

import random


grid = [[random.randint(0, 99) for _ in range(10)] for _ in range(5)]

for row in grid:
    print(row)

def main ():    
    numbersForGrid = random.randint(0 , 99)

for row in grid:
    print(row)
    
    
total = sum(sum(row) for row in grid)
    
rowsAndColumsInGrid = 10 * 10

average = total / rowsAndColumsInGrid


print(f"Total Sum : {total}")
print(f"Average : {average}")


    
main ()
    

