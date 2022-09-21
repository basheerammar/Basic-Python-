#The Collatz conjecture is one of the most famous unsolved problems in mathematics.
#The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1
#A simple code to check this problem and the number of steps it takes to get to 1

def collatz_problem(n):
    count = 0
    while n != 1:
        print(n)
        count = count + 1
        if n%2 == 0:
            n = n//2
        else:
            n = ((3*n)+1)//2
    print("This is the number of steps it took to reach 1 ",count)
return n,count


new_value, steps = collatz_problem(26)
print(new_value, steps)
