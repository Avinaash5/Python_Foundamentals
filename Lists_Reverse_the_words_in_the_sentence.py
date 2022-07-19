n=input()
list_of_n= n.split()
length_of_list_n=len(list_of_n)

index=""
reverse_of_n=""
for i in range(length_of_list_n):
    index=list_of_n[i]
    reverse = index[::-1]
    reverse_of_n=reverse_of_n+reverse+" "
print(reverse_of_n)
