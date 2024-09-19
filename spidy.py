***
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
***
char = input().strip()

if char.isalpha() and len(char) == 1:
    if char.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
