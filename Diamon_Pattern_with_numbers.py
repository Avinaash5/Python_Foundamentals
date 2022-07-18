n=int(input())
number=""
for i in range (1,n+1):
    spaces=" "*(n-i)
    number=number+str(i)+" "
    print(spaces+number)
k=str(i)
number=number.replace(k,"")
j=n-1
for i in range (j,0,-1):
    spaces=" "*(n-i)
    number=number+" "
    print(spaces+number)
    k=str(i)
    number=number.replace(k,"")
