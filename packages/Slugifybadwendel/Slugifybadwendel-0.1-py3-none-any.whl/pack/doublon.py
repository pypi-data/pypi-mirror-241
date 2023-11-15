def retire_doublon(chen,ranplasman):
    i=0
    while i<len(chen)-1:
        chen_list = list(chen)
        if chen[i]==ranplasman and chen[i-1]==ranplasman:            
            chen_list.pop(i)
            chen = ''.join(chen_list)
            i=0     
        i+=1
    return chen