def reverse(self, x: int) -> int:
    if '-' in str(x):
        output = str(x)[1:][::-1]
        output = int(output) * -1
    else:
        output = int(str(x)[::-1])
    
    if -2**31 <= output <= 2**31 - 1:
        return output
    else:
        return 0