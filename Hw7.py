def troichka(number, max_degree):
    degree = 0
    number = 3
    for num in range(max_degree):
        yield number**degree
        degree += 1

result = troichka(3, 13)

for value in result:
    print(value)
