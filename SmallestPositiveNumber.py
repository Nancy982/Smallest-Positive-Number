#Nancy Medina
#Math330 Section 2
#PE04

#Project Euler: Problem 5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#create a funtion named isPalindrome, we will use this to determine if
#the the reults create a palindrome or not
def isPalindrome(i):
    t = str(i)
    revString = ""

    #create a for loop to see if the result is read the same backward as forward
    for k in range (len(t) - 1, -1, -1):
        revString += t[k]

    return revString == t

#create another function named maxPalindrome, this will calculate the largest palindrome from
#the product of two 3-digit numbers, if a palindrome does not exist return -1
def maxPalindrome():
    palindrome = -1

    #create a for loop that includes all possible 3 diget numbers to
    #caluculate all possible results
    for x in range (999, 99, -1):
        for y in range (x, 99, -1):
            
            #create an if statement that keeps track of each palindrome
            #and compares them to see which one is the largest
            if isPalindrome(x * y) and x * y > palindrome:
                palindrome = x * y
    return palindrome;

#print the largest palindrome
print ("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is",maxPalindrome())
