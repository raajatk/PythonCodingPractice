grid_size=int(input("Please input the size of the square grid\n"))

for i in range(grid_size+1):
    for j in range(grid_size):
        if j==grid_size-1:
            print('--- ')
        elif j==0:
            print(' ---',end =" "),
        else:
            print('---',end =" "),
    if i!=grid_size:
        for j in range(grid_size):
            if j==grid_size-1:
                print('|   |')
            else:
                print('|  ',end =" ")


# print(grid_size)
