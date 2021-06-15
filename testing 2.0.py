x = 0
max_x = 10
day = 0
for i in range(max_x):
    day +=1
    x = x - (x*.1)
    x += 100

    print("day", day, 'x', x)