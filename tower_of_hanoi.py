def hanoi(n,a,c,b):
    if n==1:
        print("Move disk "+str(n)+" from pole "+a+" to pole "+c)
    else:
        hanoi(n-1,a,b,c)
        print("Move disk "+str(n)+" from pole "+a+" to pole "+c)

        hanoi(n-1,b,c,a)

n = int(input("Please input the number of disks\n"))
hanoi(n,'A','C','B')
