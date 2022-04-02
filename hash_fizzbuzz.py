def solution(n):
    output = []
    val_map = {3 : "Fizz", 5 : "Buzz"}
    
    for value in range(1,n+1):
        added_element = ""
        
        for key in val_map.keys():
            if value % key == 0:
                added_element += val_map[key]
        
        if not added_element:
            added_element = str(value)
            
        output.append(added_element)
    return output

print(solution(13))