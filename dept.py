***
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
***
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if a <= b and a <= c:
    print("L1")
elif b <= a and b <= c:
    print("L2")
else:
    print("L3")
