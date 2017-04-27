### Write a program that counts up the number of 
### vowels contained in the string s

def vowels_in(s):
    
    numVowels = 0
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or \
            char == 'o' or char == 'u':
                numVowels += 1
    return print 'Number of vowels: ' + str(numVowels)


### Write a program that prints the number of 
### times the string 'bob' occurs in s

bob = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        bob +=1  

print('Number of times bob occurs is: ' + str(bob))



### Write a program that prints the longest substring of s 
### in which the letters occur in alphabetical order

start = 1
string = ''
real_string = ''
while start <= len(s) -1:

    if len(string) < 1:
        string = s[start - 1] 

    if s[start - 1] <= s[start]:
        string += s[start]
        if len(string) > len(real_string):
            real_string = string
    else:
        string = ''

    start += 1

if real_string == '':
    real_string = s[0]

print("Longest substring in alphabetical order is: " + real_string)



















