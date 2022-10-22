def swap_case(S,T):
    result=[]
    length=len(S)
    for i in range(length-1):
        swap_word_S=S[:i]+S[i+1]+S[i]# swaping letters in word S 
        swap_word_T=T[:i]+T[i]+T[i+1] # letters in word T
        if swap_word_S==swap_word_T:
            result.append("Yes")
        else:
            result.append("No")
    return result

    
S= input()
T=input()
result=swap_case(S,T)
result=set(result)
if S==T:
    print("Yes")
elif "Yes" in result:
    print("Yes")
else:
     print("No")
