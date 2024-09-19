***
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
***
x = int(input().strip())
y = int(input().strip())
z = int(input().strip())
n = int(input().strip())

suitable_labs = []

if x >= n:
    suitable_labs.append(('L1', x))
if y >= n:
    suitable_labs.append(('L2', y))
if z >= n:
    suitable_labs.append(('L3', z))

if suitable_labs:
    suitable_labs.sort(key=lambda lab: lab[1], reverse=True)
    print(suitable_labs[0][0])
else:
    print("No suitable lab")
