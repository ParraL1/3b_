#name: Lilliana Parra
#Github username: ParraL1
#Date: 1/19/2022
#Description: asks uses for positive integer then prints a list of all positive integers\


n = int(input("Please enter a positive integer:"))
print("The factors of ", n,"are:")
for i in range(1, n+1):
    if(n%i == 0):
        print(i)