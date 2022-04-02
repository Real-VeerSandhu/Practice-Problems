def convert(s, num_rows):
    print('Length', len(s))
    
    if num_rows == 1:
        return s
    
    x = []
    for i in range(len(s)):
        x.append(range(1, num_rows+1))
        x.append(range(num_rows-1, 1, -1))
        
    vals = []
    for i in x:
        for j in i:
            if len(vals) < len(s):
                vals.append(j)
    
    output = ''
    for i in range(1, num_rows+1):
        for j in range(len(vals)):
            if vals[j] == i:
                output += s[j]
    return output         