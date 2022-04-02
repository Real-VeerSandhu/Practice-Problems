n = 12

output = []
for element in range(1, n + 1):
    if (element % 3 == 0) and (element % 5 == 0):
        output.append('FizzBuzz')
    elif (element % 3 == 0):
        output.append('Fizz')
    elif (element % 5 == 0):
        output.append('Buzz')
    else:
        output.append(str(element))

print(output)