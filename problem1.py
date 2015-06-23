values=[]
for x in range(1,1000):
    if x%3 == 0:
        values.append(x)
    if x%5 == 0:
        values.append(x)

values = list(set(values))
total = sum(values)
print(total)