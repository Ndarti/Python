try:
    a = int(input())
    b = int(input())
    c = int(input())
    solutions = []
    if a == 0:
        if b < 0:
            solutions = ["NO SOLUTION"]
        elif b == c ** 2:
            solutions = ["MANY SOLUTIONS"]
        else:
            solutions = ["NO SOLUTION"]
    else:
        if c < 0:
            solutions = ["NO SOLUTION"]
        else:
            x = (c ** 2 - b) / a
            if a * x + b < 0:
                solutions = ["NO SOLUTION"]
            else:
                solutions = [x]
    if a==0 and b<0:
        if b == c**2:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION ")
    if c >= 0:
        x=(c**2 - b) / a
        if a * x + b < 0:
            print("NO SOLUTION ")
        print(int(x))
    else:
        solutions.sort()
        for x in solutions:
            print(x)
except ValueError:
    exit(0)