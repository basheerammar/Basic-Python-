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
